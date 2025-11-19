import sqlite3, random
from sqlite3 import Error


def create_connection(db_file):
  """Créer une connexion à un fichier de base de données"""
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as e:
    print(e)
  return conn

def recupinfoviaprenom (groupe, prenom,nomtable, nomcol, cur) :
    try :
      cur.execute(f"SELECT {nomcol} FROM %s where lower(prenom) = lower(?) and nomgroupe = ?" %nomtable, (prenom, groupe, ))
      row = cur.fetchone()
      rep = row[0]
    except :
        rep = 'nulleeee'
    return rep

def recupNomsGroupes(cur) :
   try :
      cur.execute("SELECT nomgroupe FROM personne group by nomgroupe")
      rows = cur.fetchall()
      listgp = []
      for row in rows : 
         listgp.append(row[0])
      rep = listgp
      
   except :
        rep = 'null'
   return rep
   
# def recupmdp(prenom,cur):
#     cur.execute("SELECT mdp FROM personne where lower(prenom) = lower(?)", (prenom,))
#     row = cur.fetchone()
#     rep = row[0]
#     return rep

# def recupcompatibilite(prenom,cur):
#     cur.execute("SELECT compatible FROM compatibilite where lower(prenom) = lower(?)", (prenom,))
#     row = cur.fetchone()
#     rep = row[0]
#     return rep

def remplirlistfromtable(table, nomgp, numcol, cur) :
    liste = []
    cur.execute("SELECT * FROM %s where nomgroupe = ?" %table, (nomgp, ))
    rows = cur.fetchall()
    for row in rows:
      #verifier que numcol soit un entier !!! ??
      liste.append(row[numcol])
    return liste


def tirehasard(tableinfo, tablecompatible, nomgp, cur, connection, liste) :
    prenom = "prenom"
    compatibiliter = "groupe"  
    dejaattribuer = "aqlqun"
    beneficiaire = "cadeaua"   
    for i in liste :
        tabpossible = []
        cur.execute(f"SELECT {prenom}, {compatibiliter} FROM {tablecompatible} where lower(prenom) = lower(?) and nomgroupe = ?", (i, nomgp, ))
        result = cur.fetchone()
        prenomi = result[0]
        cptblei = result[1]
        cptblei = list(cptblei.strip())
        # cur.execute("SELECT * FROM %s where lower(prenom) = lower(?)" %tableinfo, (i,))
        # result = cur.fetchone()
        
        cur.execute(f"SELECT {prenom}, {compatibiliter} FROM {tablecompatible} where nomgroupe = ?  ", (nomgp,))
        rows = cur.fetchall()
        for row in rows:
            possible = True
            prenomj = row[0]
            cptblej = row[1]
            cptblej = list(cptblej.strip())
            cur.execute(f"SELECT {dejaattribuer} FROM {tableinfo} where lower(prenom) = lower(?) and nomgroupe = ? ", (prenomj, nomgp))
            rep = cur.fetchone()
            estattribuer = rep[0]
            
            for c in cptblej :
                if c in cptblei :
                    possible = False 

            if possible == True and estattribuer == 0:
                tabpossible.append(prenomj)
            
        nbgens = len(tabpossible)
        if nbgens == 0 :
            tirehasard(tableinfo, tablecompatible, nomgp, cur, connection, liste)
        else :
            n = random.randint(0,nbgens-1)
            personneattribuer = tabpossible[n]
            
            sql = f"UPDATE {tableinfo} SET {beneficiaire} = ? where lower(prenom) = lower(?) "
            info = (personneattribuer, prenomi)
            cur.execute(sql, info)

            sql = f"UPDATE {tableinfo} SET {dejaattribuer} = ? where lower(prenom) = lower(?) "
            info = (1, personneattribuer)
            cur.execute(sql, info)

            # cur = conn.cursor()
            # cur.execute("SELECT * FROM %s" %tableinfo)
            # rows = cur.fetchall()
            # for row in rows:
            #     print(row)


def remplirbd(tableinfo, tablecompatible, nomgp, cur, connection) :
    listegens = remplirlistfromtable(tableinfo, nomgp, 0,cur)
    print(listegens)
    tirehasard(tableinfo, tablecompatible, nomgp, cur, connection, listegens)
    connection.commit()


# conn = sqlite3.connect('appliNoel2025.db')
# cur = conn.cursor()
# remplirbd("personne", "compatibilite", 'Delepine', cur, conn)


# conn = sqlite3.connect('appliNoel2025.db')
# cur = conn.cursor()
# cur.execute("SELECT prenom FROM personne")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
