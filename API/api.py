from fastapi import FastAPI, Path, Query, HTTPException, status
import fonction
import sqlite3

bd = r'appliNoel.db'
#conn = sqlite3.connect('appliNoel.db')
#cursor = conn.cursor()
#fonction.create_connection(bd)

app = FastAPI()

@app.get("/beneficiaire/{prenom}")
def getbeneficiaire(prenom) :
    conn = fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(prenom, "personne", "cadeaua",cursor)
    return result

@app.get("/mdp/{prenom}")
def getmdp(prenom) :
    conn = fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(prenom, "personne", "mdp",cursor)
    return result

@app.get("/prenom/{prenom}")
def getprenom(prenom) :
    conn =fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(prenom, "personne", "prenom",cursor)
    return result

@app.get("/compatibilite/{prenom}")
def getcompatibilite(prenom) :
    conn =fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(prenom, "compatibilite", "compatible",cursor)
    result = list(result.strip())
    return result 