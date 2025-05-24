from fastapi import FastAPI, Query
import requests

app = FastAPI()
 
@app.get('/api/hello') #utiliza {} no return pra reconhecer como json
def hello():
    '''

        Amazing test    

    '''
    return {'mensagem': 'ola, tudo certo?'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json()
        dados_restaurante = {}
        for item in dados_json:
            nome_do_restaurante = item['Company']
            if nome_do_restaurante not in dados_restaurante:
                dados_restaurante[nome_do_restaurante] = []

            dados_restaurante[nome_do_restaurante].append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })
        
        return {'Restaurante':restaurante,'Cardapio':dados_restaurante} 
    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}