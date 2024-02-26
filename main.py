import requests
import json


"""
    Request simple a un personaje y su status
"""

url = 'https://rickandmortyapi.com/api/character/12'
r = requests.get(url)
print(r)

j = r.json()  # convert to JSON format

print(j)
print(j.keys()) # print keys of the JSON object

# Accessing values by key
name = j['name']
status = j['status']

print(name)
print(status)

characters_info = {}  # list to store the characters from API
i = 1
while i < 10:
    url = 'https://rickandmortyapi.com/api/character/12' + str(i)
    character_request = requests.get(url)   # request to the API
    character = character_request.json()   # convert to JSON format
    character_status = character['status']  # access the status of the character
    characters_info[character['name']] = character_status # store the status of the character

    print('El personaje {} tiene status {}'.format(character['name'], character_status))
    i += 1

print(characters_info)


"""
    Request al primer episodio
"""
url = 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
episode = r.json()
personajes = episode['characters']


list_names_episode = [requests.get(personaje).json()['name'] for personaje in personajes]

print(list_names_episode)

#Vamos a separar los personajes por especie

list_name_human = [requests.get(personaje).json()['name'] for personaje in personajes if requests.get(personaje).json()['species'] == 'Human']
list_name_alien = [requests.get(personaje).json()['name'] for personaje in personajes if requests.get(personaje).json()['species'] == 'Alien']
        
