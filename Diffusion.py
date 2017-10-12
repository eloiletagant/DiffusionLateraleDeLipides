# coding=utf-8
###############################################################################
##############################PROJET MODELISATION##############################
###############################################################################
import re
from os import chdir
import mdtraj as md



def ReadPositions(filename):
    """
    Lecture des positions initiales des atomes de references.
    :param filename:
    :return:
    """

    chdir("E:/MODELISATION/input/start.pdb" )
    obj = open(filename, 'r')
    regle = re.compile(r"OUI", re.MULTILINE) #mettre la regle de parsing ici
    rep = []
    data = ""
    while 1:
        ligne = obj.readline()
        if ligne == "":
            break
        elif (regle.match(ligne)):
            rep.append(data)
            data = ""
    rep.append(data)
    obj.close()
    chdir("E:/MODELISATION/input/DataDiffusion" )
    return(rep[1:])


######################################MAIN#####################################
print("""
    PROJET DE MODELISATION n°8
    Diffussion des lipides au sein d'une membrane
    Par Anatole et Pierre                                         
""")

print('MENU :')
menu = {}
menu['1'] = "-> Faire un truc"
menu['2'] = "-> Faire quelque chose d'autre"
menu['3'] = "-> Quitter"

while True:
    options = menu.keys()
    for entry in options:
      print(entry, menu[entry])

    selection = input("Choisissez l'une des options : ")

    if selection == 1:
        t = md.load("E:/MODELISATION/input/md_200ns_OK.xtc",
                "E:\MODELISATION\input\start.pdb")
    elif selection == 2:
        print("Bonjour !")
    elif selection == 3:
        print("Au revoir !")
        break
    else:
        print("L'option choisie n'existe pas!")