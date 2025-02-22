import barcode
from barcode.writer import ImageWriter

# Tableau contenant les codes et les noms des propriétaires
codes_proprietaires = [
    {'code': 'G-2023014KKR', 'proprietaire': 'Romaric'},
    {'code': 'G-2023005CEO', 'proprietaire': 'Jeremie'},
    {'code': 'G-2023010NGJM', 'proprietaire': 'Marc'},
    {'code': 'G-2023013NKZM', 'proprietaire': 'Fidel'},
    {'code': 'G-2023006KNMR', 'proprietaire': 'Roxane'},
    {'code': 'G-20230007BMR', 'proprietaire': 'Mbene'},
    {'code': 'G-2023012LEKP', 'proprietaire': 'Paul'},
    {'code': 'G-2023008KLAGE', 'proprietaire': 'Grace'},
    {'code': 'G-2023009KWAY', 'proprietaire': 'Yannick'},
    {'code': 'G-2023011LGMT', 'proprietaire': 'Timothee'},
    {'code': 'G-2023014AOGD', 'proprietaire': 'Ossey'},
    {'code': 'G-2023015KKFA', 'proprietaire': 'Audrey'},
    {'code': 'G-2023017EKYGA', 'proprietaire': 'Ettien'},
    {'code': 'G-2023016SKNE', 'proprietaire': 'Sehi'}

]

# Parcourir le tableau et générer un code barre pour chaque propriétaire
for item in codes_proprietaires:
    code = item['code']
    proprietaire = item['proprietaire']

    ean = barcode.get('code128', code, writer=ImageWriter())
    filename = ean.save(proprietaire)

    print(f"Le code barre pour {proprietaire} a été généré et sauvegardé dans le fichier {filename}.png")
