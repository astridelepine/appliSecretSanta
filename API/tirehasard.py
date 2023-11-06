import random


dict1 = {
  "laurent": [1, 6],
  "blandine": [1, 3],
  "camille": [1, 8],
  "corentin": [1],
  "berenice": [2, 3],
  "georges": [2],
  "maelys": [2],
  "marie-dom": [3],
  "alain": [3],
  "florian": [3, 4],
  "stephanie": [4],
  "anne": [5, 6],
  "fred": [5],
  "thomas": [5],
  "juliette": [5,7],
  "jean-francois": [6],
  "francoise": [6],
  "remi": [7],
  "gregoire": [8]
}

dict2 = {
  "laurent": [None, False],
  "blandine": [None, False],
  "camille": [None, False],
  "corentin": [None, False],
  "berenice": [None, False],
  "georges": [None, False],
  "maelys": [None, False],
  "marie-dom": [None, False],
  "alain": [None, False],
  "florian": [None, False],
  "stephanie": [None, False],
  "anne": [None, False],
  "fred": [None, False],
  "thomas": [None, False],
  "juliette": [None, False],
  "jean-francois": [None, False],
  "francoise": [None, False],
  "remi": [None, False],
  "gregoire": [None, False]
}

tabgens = ["laurent", "blandine", "camille", "corentin", "berenice", "georges", "maelys", "marie-dom", "alain", "florian", "stephanie", "anne", "fred", "thomas", "juliette", "jean-francois", "francoise","remi","gregoire"]

def tirehasard(tab) :
    
    for i in tab :
        print(i)
        tabpossible = []
        for j in tab :
            possible = True
            for t in dict1[j] :
                if t in dict1[i] :
                    possible = False 

            if possible == True and dict2[j][1] == False:
                tabpossible.append(j)
            

        nbgens = len(tabpossible)
        if nbgens == 0 :
            tirehasard(tab)
        else :
            n = random.randint(0,nbgens-1)
            personneattribuer = tabpossible[n]
            dict2[personneattribuer][1]= True
            dict2[i][0] = personneattribuer

            

tirehasard(tabgens)

for i in dict2.items():
    print(i)       
            



