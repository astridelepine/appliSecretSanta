import sqlite3, random

conn = conn = sqlite3.connect('appliNoel.db')


#cur.execute("SELECT * FROM compatibilite where prenom = 'Astrid'")
#row = cur.fetchone()
#row = row[0]
#print(row)


cursor = conn.cursor()


# cursor.execute("""
# DROP TABLE IF EXISTS personne
# """)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS personne(
#     prenom VARCHAR PRIMARY KEY UNIQUE,
#     cadeaua TEXT, 
#     aqlqun BOOLEAN DEFAULT False         
# )
# """)
# conn.commit()

# conn.commit()
# user = []
# user.append(("Astrid",""))
# user.append(("Anouk",""))
# user.append(("Frank",""))
# user.append(("Sandrine",""))
# user.append(("Denise",""))
# user.append(("Remy",""))
# user.append(("Christelle",""))
# user.append(("Philippe",""))
# user.append(("Camille",""))
# user.append(("Luca",""))
# user.append(("Orane",""))
# user.append(("Hadrien",""))
# user.append(("Stephanie",""))
# user.append(("Bruno",""))
# user.append(("Arnaud",""))
# user.append(("Julie",""))
# user.append(("Maelie",""))
# user.append(("Marielle",""))
# user.append(("Maryane",""))
# user.append(("Thibaut",""))
# user.append(("Charly",""))
# user.append(("Valery",""))
# user.append(("Romain",""))

# cursor = conn.cursor()
# cursor.executemany("""
# INSERT INTO personne(prenom,cadeaua) VALUES(?,?)""", user)

# conn.commit()




# cur = conn.cursor()
# cur.execute("SELECT * FROM personne")
# rows = cur.fetchall()
# for row in rows:
#     print(row)


# cur = conn.cursor()
# cur.execute("SELECT prenom FROM personne where prenom = 'Astri'")
# row = cur.fetchone()
# if (row != None) :
#     print(row[0])
# else :
#     print('existe pas')

# mot = 'bui'
# mot = list(mot.strip())
# print(mot)

# table = "personne"
# nomcol ="prenom"
# listgens = []
# cursor.execute("SELECT ? FROM %s", (nomcol,) %table )
# rows = cursor.fetchall()
# for row in rows:
#     listgens.append(row[0])

# print(listgens)

def remplirlistfromtable(table, numcol, cur) :
    liste = []
    cur.execute("SELECT * FROM %s" %table)
    rows = cur.fetchall()
    for row in rows:
      #verifier que numcol soit un entier !!! ??
      liste.append(row[numcol])
    return liste

def tirehasard(tableinfo, tablecompatible, cur, connection, liste) :   
    for i in liste :
        tabpossible = []
        cur.execute("SELECT * FROM %s where lower(prenom) = lower(?)" %tablecompatible, (i,))
        result = cur.fetchone()
        prenomi = result[0]
        cptblei = result[1]
        cptblei = list(cptblei.strip())
        # cur.execute("SELECT * FROM %s where lower(prenom) = lower(?)" %tableinfo, (i,))
        # result = cur.fetchone()
        
        cur.execute("SELECT * FROM %s" %tablecompatible)
        rows = cur.fetchall()
        for row in rows:
            possible = True
            prenomj = row[0]
            cptblej = row[1]
            cptblej = list(cptblej.strip())
            cur.execute("SELECT * FROM %s where lower(prenom) = lower(?)" %tableinfo, (prenomj,))
            rep = cur.fetchone()
            estattribuer = rep[3]
              
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
            
            sql = "UPDATE %s SET cadeaua = ? where lower(prenom) = lower(?) " %tableinfo
            info = (personneattribuer, prenomi)
            cur.execute(sql, info)

            sql = "UPDATE %s SET aqlqun = ? where lower(prenom) = lower(?) " %tableinfo
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