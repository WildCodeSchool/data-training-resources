from dotenv import load_dotenv
import os
import google.generativeai as genai
from preprompts import PREPROMPTS

load_dotenv()
class Gepetto:
    def __init__(
            self,
            name_model = "gemini-1.5-flash",
            temperature=1.5,
            top_p=0.95,
            top_k=40,
            max_output_token = 8192, 
            preprompt_key="None"):
        """
            :param name_model (str): nom du modèle de langage à utiliser,

            :param temperature (float): Contrôle la créativité du texte généré.
            Des valeurs plus élevées (proches de 1) produisent des textes plus créatifs et variés,
            tandis que des valeurs plus faibles (proches de 0) produisent des textes plus prévisibles.

            :param top_p (float): Utilise l'échantillonnage nucléaire pour sélectionner les tokens les plus probables.
            Une valeur plus élevée permet une plus grande diversité de tokens, tandis qu'une valeur plus faible
            se concentre sur les tokens les plus probables.

            :param top_k (int): Utilise l'échantillonnage top-k pour sélectionner les k tokens les plus probables.
            Une valeur plus élevée permet une plus grande diversité, tandis qu'une valeur plus faible
            se concentre sur les tokens les plus probables.
        """
        self.chat_session = None
        self.history = []
        self.genai = genai
        self.genai.configure(api_key=os.getenv("API_GEMINI_KEY"))
        self.preprompt(preprompt_key)
        self.__new_chat([], name_model, temperature, top_p, top_k, max_output_token)


    def preprompt(self, key):
        
        self.__preprompt_text = PREPROMPTS[key]


    def talk(self, message):   
        response = self.chat_session.send_message(message).text
        return response
   
    def __new_chat(self, history = [], name_model = "gemini-1.5-flash",temperature=1.3,top_p=0.95, top_k=40, max_output_token = 8192):
        generation_config = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_token,
            "response_mime_type": "text/plain",
        }
        safety_disabled = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            }
        ]
        model = self.genai.GenerativeModel(
            model_name=name_model,
            generation_config=generation_config,
            safety_settings=safety_disabled, 
            system_instruction=self.__preprompt_text
        )
        self.chat_session = model.start_chat(history=history)


