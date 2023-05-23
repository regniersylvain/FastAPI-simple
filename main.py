from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
import requests
import random
import json
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/val")
async def read_val(nb: Union[int, None] = None):
    if nb :
        tableau = random.sample(range(-1000, 1000), nb)
        return tableau
    if not nb :
        return(random.randint(0, 100))


@app.get("/calc/add")
async def read_add(n1:int , n2:int):
	return(n1+n2)


@app.get("/calc/prod", response_class=HTMLResponse)
async def read_prod(n1:int , n2:int):
	resultat = n1*n2
	page = f"<html><head></head><body><h1> {n1} x {n2} = {resultat}</h1></body></html>"
	return(page)


@app.get("/img", response_class=Response)
async def read_img(num:int):
	url = f"https://www.juleshaag.fr/devIA/devAPI/{num}.png"
	img = requests.get(url, stream=True).content
	return Response(content=img, media_type="image")


@app.get("/stations_velo")
async def read_velo(id:str, 
                    addr:Union[str, None]=None,
                    cap:Union[str, None]=None) :
    url = "https://www.juleshaag.fr/devIA/devAPI/station_information.json"
    stations = requests.get(url)
    stations = eval(stations.text)["data"]["stations"]

    if id =="toutes" and cap == "":
        cap_total = 0
        for station in stations :
            cap_total += station["capacity"]
        return cap_total

    else :
        for station in stations :             # "station" contient le dico  
            if station["station_id"] == id :  #  de la station dont 
                break                         #  "id_station" == id
        
        if addr == "" :
            return str(station["address"])
        elif cap == "" :
            return int(station["capacity"])
        else :
            return station

@app.get("/stations_velo/{id}/{info}")
async def read2_velo(id : str, info : Union[str, None] = None) :
    url = "https://www.juleshaag.fr/devIA/devAPI/station_information.json"
    stations = requests.get(url)
    stations = eval(stations.text)["data"]["stations"]
    dico = {}
    
    if id == "toutes" and info == "cap":
        dico["total"] = 0
        for station in stations :
            dico[station["station_id"]] = station["capacity"]
            dico["total"] += station["capacity"]
        return dico

    else :
        for station in stations :             # "station" contient le dico  
            if station["station_id"] == id :  #  de la station dont 
                break                         #  "id_station" == id

        if info == "addr" :
            return station["address"]
        elif info == "cap" :
            return station["capacity"]


if __name__ == "__main__" :
    uvicorn.run(app)                           # sur localhost
    #uvicorn.run(app, host=0.0.0.0, port=8000) # sur le reseau