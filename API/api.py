from fastapi import FastAPI, Path, Query, HTTPException, status
import fonction
import sqlite3

bd = r'appliNoel.db'
#conn = sqlite3.connect('appliNoel.db')
#cursor = conn.cursor()
fonction.create_connection(bd)

app = FastAPI()
@app.get("/beneficiaire/{prenom}")
@app.get("/mdp/{prenom}")
@app.get("/prenom/{prenom}")
@app.get("/compatibilite/{prenom}")

def getbeneficiaire(prenom) :
    conn = fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupcadeaua(prenom, cursor)
    return result

def getmdp(prenom) :
    conn = fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupmdp(prenom, cursor)
    return result

def getprenom(prenom) :
    conn =fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recuprenom(prenom, cursor)
    return result

def getcompatibilite(prenom) :
    conn =fonction.create_connection(bd)
    cursor = conn.cursor()
    result = fonction.recupcadeaua(prenom, cursor)
    result = list(result.strip())
    return result 