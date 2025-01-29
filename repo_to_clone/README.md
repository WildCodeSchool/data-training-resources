python -m venv docker_mage

.\docker_mage\Scripts\activate

git clone https://github.com/WildCodeSchool/data-training-resources.git repo_to_clone

cd .\repo_to_clone\

docker compose build

docker compose up
