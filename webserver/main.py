import store
from fastapi import FastAPI #importamos la librería de FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #crear instancia de la aplicació

@app.get('/') #usar el decorador para indicar la ruta por el cual se va a acceder desde la web
def get_lsit():
    return [1,2,3,4,5,6,7,8,9]

@app.get('/contact')
def get_list():
    return {'name': 'Jenier'}

@app.get('/conact-html',response_class=HTMLResponse)
def get_list():
    return """
    <h4>Hola mundo</h4>
"""

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()


#Correr el servividor: uvicorn main:app --reload