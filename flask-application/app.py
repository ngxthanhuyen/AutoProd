from flask import Flask, render_template
from config import ConfigSingleton
from controller.image_controller import init_routes

# Récupération des services configurés via le Singleton
config = ConfigSingleton.instance()
app = config["app"]
mongo = config["mongo"]
mail = config["mail"]

# Définition d'une route d'accueil pour vérifier que le service tourne
@app.route('/')
def home():
    return render_template('upload.html')

# Enregistrement des routes spécifiques aux images
init_routes(app, mongo, mail)

# Lancement de l'application en mode debug
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
