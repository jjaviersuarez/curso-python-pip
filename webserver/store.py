import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #obtener la información de la api
    print(r.status_code) #ver el código de estado
    print(r.text) #muestra la información que está dando la api
    categories = r.json() #transformar esa información obtenida en str pasarla  a json
    
    for category in categories:
        print(f'El nombre: {category['name']}')