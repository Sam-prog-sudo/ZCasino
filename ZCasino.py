#-*- coding: utf8 -*-
from random import randrange as rand
from math import ceil as arrondi

art = """

MMM°°°AMV         .g8°°bgd                     db                        
M'   AMV        .dP'     `M
'   AMV         dM'       `  ,6"Yb.  ,pP"Ybd `7MM  `7MMpMMMb.   ,pW"Wq.
   AMV          MM          8)   MM  8I   `"   MM    MM    MM  6W'   `Wb
  AMV   , mmmmm MM.          ,pm9MM  `YMMMa.   MM    MM    MM  8M     M8
 AMV   ,M       `Mb.     ,' 8M   MM  L.   I8   MM    MM    MM  YA.   ,A9
AMVmmmmMM         `"bmmmd'  `Moo9^Yo.M9mmmP' .JMML..JMML  JMML. `Ybmd9'

"""
    
def roule(num, argent):
    """La fonction roule compare le numéro parié
    au numéro sur lequel la bille s'arrête
    """
    bille = rand(50)
    print ("\n", "Rien ne va plus !","\n", "La bille est tombée sur le ", bille, "\n")
    if bille == num:
        r= argent * 3
    elif (num%2==0 and bille%2==0) or (num%2!=0 and bille%2!=0):
        r= argent / 2
    else:
        r=0
    return r

def main ():
    continuer = True
    gains=0
    pertes=0
    total_mise=0
    type(gains and pertes) is int
    
    while continuer:
        print ("""
________________________________________________________________

Veuillez saisir le numéro à miser:
(Rq: le nombre doit être un entier compris entre 0 et 49 inclus)
""")
        numero = int(input ())
        
        if 0 <= numero and numero < 50 :
            print("\n", "Veuillez saisir le montant de votre mise: ","\n","(Rq: le nombre doit être un entier strictement positif)","\n")
            mise = int(input ())
            total_mise +=mise
            
            if mise>0:
                x = arrondi(roule(numero, mise))
                
                if x == 0:
                    pertes += mise
                    print ("\n", "Malheureusement, vous ne remportez aucun gain.")
                else:
                    gains += x
                    print ("\n", "Félicitation !", "\n", "Vous venez de remportez: ", x, "$ !")
            
            elif mise==0:
                print ("\n", "Veuillez miser ne serait-ce qu'un peu d'argent.")
            
            else:
                print ("\n", "Veuillez miser un nombre entier strictement positif.")
        
        else:
            print ("\n", "Le numéro que vous avez saisi ne correspond pas à un numéro de la roulette.")
        
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O" or quitter == "0":
            print("\n", "Vous quittez le casino.")
            
            if gains<pertes:
                print("Votre scroce total est de ", gains-total_mise," $")
            elif gains>pertes:
                print("Votre scroce total est de +", total_mise-pertes," $")
            else:
                print("Vous n'avez rien gagné, ni rien perdu !")
                
            continuer = False


print(art)            
print("Bonjour et bienvenue au ZCasino, le casino qu'il vous faut.", '\n', "Si vous le voulez bien, nous allons jouer à la roulette.")
main()
print('\n', "Nous vous remercions pour votre confiance,", '\n', "et nous espérons vous revoir bientôt dans notre casino.", "\n")