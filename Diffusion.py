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

print("Chargement de la trajectoire des lipides\n")
#Stockage de la trajectoire dans une variable
trajectoire = md.load_xtc("E:/MODELISATION/input/md_200ns_OK.xtc",
                top="E:\MODELISATION\input\start.pdb")
#Stockage de la position de notre atome de reference a la frame 0
#Atome de reference = phosphate du premier residu
ref_origin = trajectoire.xyz[0, 8]
coordinate_array = 

print('\nMENU :')
menu = {}
menu[2] = "-> Faire des trucs"
menu[3] = "-> Afficher des coordonees"
menu[4] = "-> Afficher des coordonees"
menu[5] = "-> Afficher des coordonees"
menu[6] = "-> Afficher des coordonees"
menu[1] = "-> Quitter"

while True:
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])

    selection = input("Choisissez l'une des options : ")

    if selection == 1:
        print("Au revoir !")
        break
    elif selection == 2:
        break
    elif selection == 3:
        print(trajectoire)
    elif selection == 4:
        #selection du phosphate du residu numero 1
        for i in range(1, 10):
            array = []
            #print('x: %s\ty: %s\tz: %s' % tuple(trajectoire.xyz[i, 8, :]))
            print(trajectoire.xyz[i, 8])
            #array.append(tuple(trajectoire.xyz[i, 8, :])
    elif selection == 5:
        break
    elif selection == 6:
        break
    else:
        print("L'option choisie n'existe pas!")



#atom_distances = md.compute_distances(t, atom_pairs, periodic=True, opt=True)
#atom_pairs = np.ndarray(shape = (num_pairs, 2), dtype = int)