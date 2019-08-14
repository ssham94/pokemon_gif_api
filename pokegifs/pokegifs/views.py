from django.http import JsonResponse
import requests
import os
import json
def show_pokemon(request, id):
    api_url = f'http://pokeapi.co/api/v2/pokemon/{id}'
    res = requests.get(api_url)
    body = json.loads(res.content)
    poke_types = []
    for i in range(len(body['types'])):
        poke_types.append(body["types"][i]['type']['name']) 
    key = os.environ.get('GIPHY_KEY')
    url = (f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={body['name']}&rating=g")
    giphy_res = requests.get(url)
    giphy_body = json.loads(giphy_res.content)
    return JsonResponse(
        {'id': body['id'],
         'name': body['name'],
         'types': poke_types,
         'giph': giphy_body['data'][0]['url']
         }
    )
