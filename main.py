from fastapi import FastAPI
import uvicorn
import sqlite3
# import json
# from fastapi.middleware.cors import CORSMiddleware

conn = sqlite3.connect('scrap_game.db')
c = conn.cursor()
app = FastAPI()

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
    return [{
        name: 'Share',
        data: [
            { name: 'Chrome', y: 551.41 },
            { name: 'Internet Explorer', y: 11.84 },
            { name: 'Firefox', y: 10.85 },
            { name: 'Edge', y: 4.67 },
            { name: 'Safari', y: 4.18 },
            { name: 'Other', y: 7.05 }
        ]

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
