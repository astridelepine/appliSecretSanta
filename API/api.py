from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import fonction
import sqlite3
import os


bd = r'../appliNoel2025.db'
#conn = sqlite3.connect('appliNoel.db')
#cursor = conn.cursor()
#fonction.create_connection(bd)
print(bd)   
print(type(bd))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/beneficiaire/{groupe}/{prenom}")
def getbeneficiaire(groupe, prenom) :
    conn = fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(groupe, prenom, "personne", "cadeaua",cursor)
    return result

@app.get("/mdp/{groupe}/{prenom}")
def getmdp(groupe, prenom) :
    conn = fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(groupe, prenom, "personne", "mdp",cursor)
    return result

@app.get("/prenom/{groupe}/{prenom}")
def getprenom(groupe, prenom) :
    conn =fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(groupe, prenom, "personne", "prenom",cursor)
    return result

@app.get("/user/{groupe}/{prenom}/{mdp}")
def getuser(groupe, prenom, mdp) :
    conn =fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(groupe, prenom, "personne", "mdp",cursor)
    if result == mdp :
        return fonction.recupinfoviaprenom(groupe, prenom, "personne", "cadeaua",cursor)
    else :
        return False

@app.get("/compatibilite/{groupe}/{prenom}")
def getcompatibilite(groupe, prenom) :
    conn =fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupinfoviaprenom(groupe, prenom, "compatibilite", "compatible",cursor)
    result = list(result.strip())
    return result 

@app.get("/nomgroupe/")
def getcompatibilite() :
    conn = fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupNomsGroupes(cursor)
    return result 