import sqlite3

conn = conn = sqlite3.connect('appliNoel.db')

cursor = conn.cursor()
cursor.execute(""" DROP TABLE IF EXISTS personne""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS personne(
    prenom VARCHAR PRIMARY KEY UNIQUE,
    mdp TEXT,
    cadeaua TEXT, 
    aqlqun BOOLE DEFAULT False         
)
""")
conn.commit()
cursor.execute(""" DROP TABLE IF EXISTS compatibilite""")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS compatibilite(
    prenom VARCHAR PRIMARY KEY UNIQUE,
    groupe TEXT       
)
""")
conn.commit()

users = []
users.append(("Astrid", "1"))
users.append(("Anouk", "1"))
users.append(("Frank", "1"))
users.append(("Sandrine","1"))
users.append(("Denise", "2"))
users.append(("Remy", "2"))
users.append(("Christelle", "3"))
users.append(("Philippe", "3"))
users.append(("Camille", "34"))
users.append(("Luca", "4"))
users.append(("Orane", "35"))
users.append(("Hadrien", "5"))
users.append(("Stephanie", "6"))
users.append(("Bruno", "6"))
users.append(("Arnaud", "6"))
users.append(("Julie", "6"))
users.append(("Maelie", "6"))
users.append(("Marielle", "7"))
users.append(("Maryane", "78"))
users.append(("Thibaut", "8"))
users.append(("Charly", "7"))
users.append(("Valery", "7"))
users.append(("Romain", "7"))
users.append(("Laurence", "0"))

cursor.executemany("""
INSERT INTO compatibilite(prenom, groupe) VALUES(?, ?)""", users)

conn.commit()
user = []
user.append(("Astrid","dakor",""))
user.append(("Anouk","fourmillon",""))
user.append(("Frank","trortiner",""))
user.append(("Sandrine","vrombille",""))
user.append(("Denise","sakado",""))
user.append(("Remy","barbrousse",""))
user.append(("Christelle","pampaille",""))
user.append(("Philippe","grabulde",""))
user.append(("Camille","crumulus",""))
user.append(("Luca","carambolage",""))
user.append(("Orane","farambule",""))
user.append(("Hadrien","barbidule",""))
user.append(("Stephanie","turtuf",""))
user.append(("Bruno","srockett",""))
user.append(("Arnaud","teufteuf",""))
user.append(("Julie","mascroc",""))
user.append(("Maelie","crafouille",""))
user.append(("Marielle","salloutassions",""))
user.append(("Maryane","dortance",""))
user.append(("Thibaut","distresse",""))
user.append(("Charly","varandole",""))
user.append(("Valery","tourloupage",""))
user.append(("Romain","barbotin",""))
user.append(("Laurence","luminoyer",""))

cursor = conn.cursor()
cursor.executemany("""
INSERT INTO personne(prenom,mdp,cadeaua) VALUES(?,?,?)""", user)

conn.commit()


