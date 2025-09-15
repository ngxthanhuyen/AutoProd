# Classe représentant le modèle de données pour une image stockée dans MongoDB
class ImageDocument:
    def __init__(self, name, content_type, image_data):
        # Nom original du fichier (ex: "photo.jpg")
        self.name = name
        # Type MIME du fichier (ex: "image/jpeg")
        self.content_type = content_type
        # Données binaires du fichier (le contenu de l’image elle-même)
        self.image_data = image_data

    # Méthode pour convertir l'objet en dictionnaire utilisable par MongoDB
    def to_dict(self):
        return {
            "name": self.name,                   # Nom du fichier
            "content_type": self.content_type,   # Type MIME
            "image_data": self.image_data        # Données binaires de l'image
        }