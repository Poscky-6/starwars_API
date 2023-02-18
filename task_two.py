import requests
import json

from pprint import pprint
from utils.fetch_data import hit_url
first_film="https://swapi.dev/api/films/1/"

def write_data_in_file(data):
    with open("output.txt","w") as fp:
        fp.write(json.dumps(data))

def first_task():
    response=requests.get(first_film)
    result=response.json()
    write_data_in_file(result)
    return result

def second_task(data_):
    characters=data_.get("characters")
    names=[]
    for character in characters:
        result_ = hit_url(character)
        char=result_.json()
        names.append(char.get("name"))
    return names


def third_task(data1_):
    planets = data1_.get("planets")
    pprint(planets)
    names= []
    for planet in planets:
         result_ = hit_url(planet)
         pla = result_.json()
         names.append(pla.get("name"))
    return names

def fourth_task(data2_):
    vehicles = data2_.get("vehicles")
    pprint(vehicles)
    names = []
    for vehicle in vehicles:
        result_ = hit_url(vehicle)
        pla = result_.json()
        names.append(pla.get("name"))
    return names

if __name__=="__main__":
    #first task
    first_film_result=first_task()
    pprint(first_film_result)

    #second task
    single_character=second_task(first_film_result)
    pprint(single_character)

    #third task
    single_planet=third_task(first_film_result)
    pprint(single_planet)

    #fourth task
    single_vehicle=fourth_task(first_film_result)
    pprint(single_vehicle)