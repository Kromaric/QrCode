import qrcode
from PIL import Image

# Créer un code QR avec le texte souhaité
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data("geniusgroups.ci")
qr.make(fit=True)

# Générer une image du code QR
qr_image = qr.make_image(fill_color="black", back_color="white")

# Charger l'icône à utiliser au milieu du code QR
icon = Image.open("geniuslogo.png")

# Calculer la position de l'icône au milieu de l'image du code QR
icon_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
icon_position = ((qr_image.size[0] - icon_size[0]) // 2, (qr_image.size[1] - icon_size[1]) // 2)

# Redimensionner l'icône à la taille souhaitée
icon = icon.resize(icon_size)

# Ajouter l'icône au milieu de l'image du code QR
qr_image.paste(icon, icon_position)

# Sauvegarder le code QR avec l'icône dans un fichier
qr_image.save("code_qr.png")
