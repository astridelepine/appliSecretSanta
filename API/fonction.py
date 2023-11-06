import sqlite3, random
from sqlite3 import Error
conn = conn = sqlite3.connect('appliNoel.db')

cursor = conn.cursor()


def create_connection(db_file):
  """Créer une connexion à un fichier de base de données"""
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as e:
    print(e)
  return conn

def recupinfoviaprenom (prenom,nomtable, numcol, cur) :
    cur.execute("SELECT * FROM %s where lower(prenom) = lower(?)" %nomtable, (prenom,))
    row = cur.fetchone()
    rep = row[numcol]
    return rep

# def recupmdp(prenom,cur):
#     cur.execute("SELECT mdp FROM personne where lower(prenom) = lower(?)", (prenom,))
#     row = cur.fetchone()
#     rep = row[0]
#     return rep

# def recuprenom(prenom,cur):
#     cur.execute("SELECT prenom FROM personne where lower(prenom) = lower(?)", (prenom,))
#     row = cur.fetchone()
#     rep = row[0]
#     return rep

# def recupcompatibilite(prenom,cur):
#     cur.execute("SELECT compatible FROM compatibilite where lower(prenom) = lower(?)", (prenom,))
#     row = cur.fetchone()
#     rep = row[0]
#     return rep

def remplirlistfromtable(table, numcol, cur) :
    liste = []
    cur.execute("SELECT * FROM %s" %table)
    rows = cur.fetchall()
    for row in rows:
      #verifier que numcol soit un entier !!! ??
      liste.append(row[numcol])
    return liste

prenom = "prenom"
compatibiliter = "groupe"  
dejaattribuer = "aqlqun"
beneficiaire = "cadeaua"

def tirehasard(tableinfo, tablecompatible, cur, connection, liste) :
    prenom = "prenom"
    compatibiliter = "groupe"  
    dejaattribuer = "aqlqun"
    beneficiaire = "cadeaua"   
    for i in liste :
        tabpossible = []
        cur.execute(f"SELECT {prenom}, {compatibiliter} FROM %s where lower(prenom) = lower(?)" %tablecompatible, (i,))
        result = cur.fetchone()
        prenomi = result[0]
        cptblei = result[1]
        cptblei = list(cptblei.strip())
        # cur.execute("SELECT * FROM %s where lower(prenom) = lower(?)" %tableinfo, (i,))
        # result = cur.fetchone()
        
        cur.execute(f"SELECT {prenom}, {compatibiliter} FROM %s" %tablecompatible)
        rows = cur.fetchall()
        for row in rows:
            possible = True
            prenomj = row[0]
            cptblej = row[1]
            cptblej = list(cptblej.strip())
            cur.execute(f"SELECT {dejaattribuer} FROM %s where lower(prenom) = lower(?)" %tableinfo, (prenomj,))
            rep = cur.fetchone()
            estattribuer = rep[0]
            
              
            for c in cptblej :
                if c in cptblei :
                    possible = False 

            if possible == True and estattribuer == 0:
                tabpossible.append(prenomj)
                print(tabpossible)
            
        nbgens = len(tabpossible)
        if nbgens == 0 :
            tirehasard(tableinfo, tablecompatible, cur, connection, liste)
        else :
            n = random.randint(0,nbgens-1)
            personneattribuer = tabpossible[n]
            
            sql = f"UPDATE %s SET {beneficiaire} = ? where lower(prenom) = lower(?) " %tableinfo
            info = (personneattribuer, prenomi)
            cur.execute(sql, info)

            sql = f"UPDATE %s SET {dejaattribuer} = ? where lower(prenom) = lower(?) " %tableinfo
            info = (1, personneattribuer)
            cur.execute(sql, info)

            cur = conn.cursor()
            cur.execute("SELECT * FROM %s" %tableinfo)
            rows = cur.fetchall()
            for row in rows:
                print(row)


def remplirbd(tableinfo, tablecompatible, cur, connection) :
    listegens = remplirlistfromtable(tableinfo,0,cur)
    tirehasard(tableinfo, tablecompatible, cur, connection, listegens)
    connection.commit()

remplirbd("personne", "compatibilite", cursor, conn)

cur = conn.cursor()
cur.execute("SELECT * FROM personne")
rows = cur.fetchall()
for row in rows:
    print(row)