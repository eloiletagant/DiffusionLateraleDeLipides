# coding=utf-8
###############################################################################
##############################PROJET MODELISATION##############################
###############################################################################
import mdtraj as md
import math

def GenerateDistances(FrameWindow, ):
    distance_list = []

    return(arg + 2)


######################################MAIN#####################################
print("""
    PROJET DE MODELISATION n°8
    Diffussion des lipides au sein d'une membrane
    Par Anatole et Pierre                                         
""")

print("Chargement de la trajectoire des lipides\n")
# Stockage de la trajectoire dans une variable
trajectory = md.load_xtc("E:/MODELISATION/input/md_200ns_OK.xtc",
                         top="E:\MODELISATION\input\start.pdb")
# Stockage de la topologie
topology = trajectory.topology
print(topology)


# Récupère les numeros des atomes de phosphate dans une liste
"""
    ref_list = []
    x = 8
    for i in range(1, 256):
        ref_list.append(x)
        x += 54
    print(ref_list)
"""
# Faire de maniere propre
reference_list = []
for atom in topology.atoms:
    if atom.name == 'P1':
        # print(atom.name)
        # print(atom.index)
        print(trajectory.xyz[0, atom.index])
        reference_list.append(trajectory.xyz[0, atom.index])

# Initialisation de la liste des intervalles de fenêtres
frame_list = [10, 50, 100, 200, 300, 500, 700, 1000, 2000]


"""
    for coordinate in coordinate_array:
        print(
            math.sqrt(
                ((coordinate[0] - ref_origin[0])**2) + ((
                coordinate[1] - ref_origin[1])**2)
            )
        )
"""

"""
    print('\nMENU :')
    menu = {}
    menu[2] = "-> Faire des trucs"
    menu[3] = "-> Faire des trucs"
    menu[4] = "-> Faire des trucs"
    menu[5] = "-> Faire des trucs"
    menu[6] = "-> Faire des trucs"
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
            break
        elif selection == 4:
            break
        elif selection == 5:
            break
        elif selection == 6:
            break
        else:
            print("L'option choisie n'existe pas!")
"""