import math
import random
import pygame
from pygame import mixer



# Classes
#==========================================================================================

class Game:
    '''
    Classe qui defini l'ensemble des paramètres d'une partie
    '''
    def __init__(self, width=0, height=0):

        #Screen
        self.width = width
        self.height = height
        self.resolution = None
        self.background = None
        self.caption =  pygame.display.set_caption("Space Invader")
        self.icon = pygame.image.load('ufo.png')
        self.disp_icon = pygame.display.set_icon(self.icon)   

        # score
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textX = 10
        self.testY = 10

        # Game Over
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)

        #-------------------------------------------------------------------

    def set_level_design(self):
        self.background = pygame.image.load("background.png")

    def set_resolution(self,width=800, height=600,):
        self.resolution = pygame.display.set_mode((width,height))

    def music_play(self):
        """
        Methode pour initialiser et jouer la music du jeu
        """
        mixer.music.load("background.wav")
        mixer.music.play(-1)
          
    def show_score(self, x, y):
        """
        Méthode affichant le score du joueur
        Args:
           x (_type_): position x du texte
           y (_type_): position y du texte
         """
        
        score = self.font.render("Score : " + str(self.score_value), True, (255, 255, 255))
        self.resolution.blit(score, (x, y))

    def game_over_text(self, x=200, y=250):
        """
        Méthode affichant le message Game Over
        """
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        self.resolution.blit(over_text, (x, y))

#==========================================================================================

class Char_entity:

    """
    Classe Jeu paramètrant les differents éléments interactifs d'une partie 
    - Joueur
    - Ennemis
    - Armes
    """

    def __init__(self, pos_X=0, pos_Y=0, posX_change=0, posY_change=0, char_type="Default", lvl=0, status ="ready"):

        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.posX_change = posX_change
        self.posY_change = posY_change
        self.char_type = char_type
        self.char_sprt = None
        self.char_snd = None
        self.lvl = lvl
        self.status = status

#====== Héritage =================================================================

class Human_player(Char_entity):
    def __init__(self, pos_X=370, pos_Y=480):
        super().__init__(pos_X, pos_Y, posX_change=0, posY_change=0, char_type="Player", lvl=0, status = "ready")
        self.char_sprt = pygame.image.load("player.png")

class Weapon(Char_entity):
    def __init__(self, pos_X=0, pos_Y=480):
        super().__init__(pos_X, pos_Y, posX_change=0, posY_change=10, char_type="Weapon", lvl=0, status = "ready")
        self.char_sprt = pygame.image.load("bullet.png")
        self.char_snd = pygame.mixer.Sound("laser.wav")
        self.bullet_state = "ready" 

class Invader(Char_entity):
    def __init__(self, pos_X= 0, pos_Y= 0):
        super().__init__(pos_X, pos_Y, posX_change=4, posY_change=40,char_type="Invader", lvl=0, status = "ready")
        self.char_sprt = pygame.image.load("enemy.png")
        
#==========================================================================================

class Swarm:
    """
    Classe qui va gerer un ensemble de classes "Invader"
    """
    def __init__(self, swarm_size = 6, invader_list=[], enemyImg_list=[], pos_X_list=[], pos_Y_list=[], posX_change_list=[], posY_change_list=[] ): 
        self.swarm_size = swarm_size
        self.invader_list = invader_list
        self.enemyImg_list = enemyImg_list
        self.pos_X_list = pos_X_list
        self.pos_Y_list = pos_Y_list
        self.posX_change_list = posX_change_list
        self.posY_change_list = posY_change_list

        #==========================================================================================

    def deploy(self):
        for mob in range(self.swarm_size):
            current_invader = Invader(random.randint(0, 736),random.randint(50, 150))  
            self.invader_list.append(current_invader)
            self.enemyImg_list.append(current_invader.char_sprt)          
            self.pos_X_list.append(current_invader.pos_X)
            self.pos_Y_list.append(current_invader.pos_Y)
            self.posX_change_list.append(current_invader.posX_change)
            self.posY_change_list.append(current_invader.posY_change)


# Intialize the pygame
pygame.init()

# Intialize a game instance
game = Game()
game.set_resolution()           # create the screen
game.set_level_design()         # Background

# Go DJay !
game.music_play()               # lance la musique

# Player
human_player = Human_player()   # crée une instance de classe "Human_player" 

# Enemy
swarm = Swarm()                 # crée une cohorte de classe "invader"
swarm.deploy()

# Bullet
current_weapon = Weapon()       # crée une instance de classe "Weapon"

def player_motion(x, y):
    game.resolution.blit(human_player.char_sprt, (x, y))

def enemy_motion(x, y, i):
    game.resolution.blit(swarm.enemyImg_list[i], (x, y))

def fire_bullet(x, y):
    # global bullet_state
    current_weapon.bullet_state = "fire"
    game.resolution.blit(current_weapon.char_sprt, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    
    game.resolution.fill((0, 0, 0))
    game.resolution.blit(game.background, (0, 0))       # Background Image 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:                # verification de l'etat des touches du clavier
            if event.key == pygame.K_LEFT:
                human_player.posX_change = -5
            if event.key == pygame.K_RIGHT:
                human_player.posX_change = 5
            if event.key == pygame.K_SPACE:
                if current_weapon.bullet_state is "ready":
                    current_weapon.char_snd.play()
                    current_weapon.pos_X = human_player.pos_X     # aligne le sprite de l'arme sur la position du joueur
                    fire_bullet(current_weapon.pos_X, current_weapon.pos_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                human_player.posX_change = 0

    human_player.pos_X += human_player.posX_change

    if human_player.pos_X <= 0:
        human_player.pos_X = 0
    elif human_player.pos_X >= 736:
        human_player.pos_X = 736

    # Enemy Movement
    for invader in range(swarm.swarm_size):

        # Game Over
        if swarm.pos_Y_list[invader] > 440:
            game.game_over_text()
            break

        swarm.pos_X_list[invader] += swarm.posX_change_list[invader]

        if swarm.pos_X_list[invader] <= 0:
            swarm.posX_change_list[invader] = 4
            swarm.pos_Y_list[invader] += swarm.posY_change_list[invader]
        elif swarm.pos_X_list[invader] >= 736:
            swarm.posX_change_list[invader] = -4
            swarm.pos_Y_list[invader] += swarm.posY_change_list[invader]

        # Collision
        collision = isCollision(swarm.pos_X_list[invader], swarm.pos_Y_list[invader], current_weapon.pos_X, current_weapon.pos_Y)

        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            current_weapon.pos_Y = 480
            current_weapon.bullet_state = "ready"
            game.score_value += 1
            swarm.pos_X_list[invader] = random.randint(0, 736)
            swarm.pos_Y_list[invader] = random.randint(50, 150)

        enemy_motion(swarm.pos_X_list[invader], swarm.pos_Y_list[invader], invader)

    # Bullet Movement
    if current_weapon.pos_Y <= 0:
        current_weapon.pos_Y = 480
        current_weapon.bullet_state = "ready"

    if current_weapon.bullet_state == "fire":
        fire_bullet(current_weapon.pos_X, current_weapon.pos_Y)
        current_weapon.pos_Y -= current_weapon.posY_change

    player_motion(human_player.pos_X, human_player.pos_Y)
    game.show_score(game.textX, game.testY)
    pygame.display.update()