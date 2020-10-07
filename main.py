from fastapi import FastAPI
import uvicorn
import sqlite3
import json

#JSON RESPONSE
from fastapi.responses import JSONResponse

# //Access-Control-Allow-Headers: *
# //Access-Control-Allow-Headers: x-requested-with

# import json
# from fastapi.middleware.cors import CORSMiddleware

conn = sqlite3.connect('scrap_game.db')
c = conn.cursor()
app = FastAPI()
headers = {'Access-Control-Allow-Origin':'*'}


# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://127.0.0.1:8000/",
#     "https://simplon-alien.000webhostapp.com/",
#     "https://simplon-alien.000webhostapp.com/"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/games")
async def one_game ():
    c.execute("SELECT * FROM games;")
    game = c.fetchall()
    conn.commit()
    return game

@app.get("/test")
async def test():
    return JSONResponse(content=[{"name":"PS4","pourcent":39.04109589041096},{"name":"PS5","pourcent":3.4246575342465753},{"name":"SWI","pourcent":32.87671232876712},{"name":"XBX","pourcent":0.684931506849315},{"name":"XONE","pourcent":23.972602739726025}], headers=headers)


@app.get("/games/count/pourcent")
async def pourcent_platform():
    c.execute("SELECT Plateforme, COUNT(Plateforme) FROM games GROUP BY Plateforme;")
    count = c.fetchall()
    total = 0
    for i in count :
        total += i[1]
    pourcentage = []
    for plat in count :
        p = plat[1] / total * 100
        pour = {}
        pour["name"] = plat[0]
        pour["pourcent"] = p
        pourcentage.append(pour)
    conn.commit()
    print(pourcentage)
    return pourcentage
