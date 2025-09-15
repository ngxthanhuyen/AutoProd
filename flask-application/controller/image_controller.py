from flask import Blueprint, request, jsonify
from service.image_service import save_image
from mailer.mail_service import create_email

# Création d'un Blueprint pour organiser les routes liées aux images
bp = Blueprint('images', __name__)

# Fonction pour initialiser les routes avec les services injectés
def init_routes(app, mongo, mail):
    @bp.route('/upload', methods=['POST'])  # Définition de la route d'upload d'image
    def upload_image():
        # Récupération du fichier envoyé dans la requête
        file = request.files['file']
        print(f"📥 Fichier reçu : {file.filename}")
        # Enregistrement de l'image en base de données
        image_id = save_image(file, mongo)

        # Création de l'e-mail à envoyer après upload
        msg = create_email("nthanhuyen1411@gmail.com", "Image Upload", f"Image ID: {image_id}")

        try:
            # Tentative d'envoi de l'e-mail via Flask-Mail
            mail.send(msg)
            print("📧 Email envoyé avec succès")
        except Exception as e:
            # Affichage d'une erreur si l'envoi échoue
            print("❌ Erreur envoi mail:", e)

        # Retourne un message JSON avec l'ID de l'image
        return jsonify({"message": f"✅ Image uploaded with ID: {image_id}"})

    # Enregistrement du Blueprint sous le préfixe /api/images
    app.register_blueprint(bp, url_prefix='/api/images')
