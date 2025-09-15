from model.image_document import ImageDocument

def save_image(file, mongo):
    # Création d'une instance du modèle ImageDocument avec les infos du fichier
    image = ImageDocument(
        name=file.filename,
        content_type=file.content_type,
        image_data=file.read()
    )
    # Insertion du document image dans la collection 'images' de MongoDB
    result = mongo.db.images.insert_one(image.to_dict())
    # Retourne l'identifiant unique généré par MongoDB
    return str(result.inserted_id)