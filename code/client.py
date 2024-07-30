import requests

# Clé d'API Google Maps
api_key = 'AIzaSyC_Iq3Fiyrt1S61Uv19oRSABNKjC8oq4SQ'

# Nom du lieu
place_name = 'Bastos'

# URL de requête
url = f'https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key={api_key}'

# Envoyer la requête GET à l'API
response = requests.get(url)

# Vérifier le statut de la réponse
if response.status_code == 200:
    # Récupérer les données de réponse au format JSON
    data = response.json()
    print(data)

    # Vérifier si des résultats ont été retournés
    if data['status'] == 'OK':
        # Récupérer les coordonnées géographiques du premier résultat
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']

        # Traiter les coordonnées géographiques
        print(f'Latitude: {latitude}, Longitude: {longitude}')
    else:
        print('Aucun résultat trouvé pour ce lieu')
else:
    print('Erreur lors de la requête à l\'API Google Maps')
