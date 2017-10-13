# coding=utf-8
###############################################################################
##############################PROJET MODELISATION##############################
###############################################################################
import mdtraj as md
import math

def get_distance(trajectory, atom, frame):
    """
    Pour un atome et une fenetre de temps donnee, calcule la distance entre
    la position de l'atome de reference au debut de la fenetre et sa position
    a la fin.
    :param trajectory:
    :param atom:
    :param frame:
    :return:
    """
    step = 10
    return (
        # La racine carree a ete ignore car elle ralenti le script et ne
        # change pas les distances relatives
        ((trajectory.xyz[frame, atom][0] - trajectory.xyz[frame + step,
                                                          atom][0]
          ) ** 2)
        + ((trajectory.xyz[frame, atom][1] - trajectory.xyz[frame + step,
                                                            atom][1]
            ) ** 2)
    )

def get_distances_list(trajectory, frame_window, atom):
    """
    Genere les distances pour une fenetre de temps, pour un atome de reference
    :param trajectory:
    :param frame_window:
    :param atom:
    :return:
    """
    distances_list = []
    # Parcours de l'ensemble des frames
    # print("Nombre total de frames : ", trajectory.n_frames - frame_window)
    frame = 0
    last_frame = trajectory.n_frames - frame_window
    while frame < last_frame:
        # print(frame)
        distances_list.append(
            get_distance(trajectory, atom, frame)
        )
        frame += 10

    return distances_list

def get_atoms_dict(trajectory, topology, frame_window):
    atoms_dict = {}
    for atom in topology.atoms:
        if atom.name == "P1":
            print(atom.index)
            atoms_dict[atom.index] = get_distances_list(trajectory,
                                                          frame_window,
                                                          atom.index)
    return atoms_dict

######################################MAIN#####################################
print("""
    PROJET DE MODELISATION n°8
    Diffussion des lipides au sein d'une membrane
    Par Anatole et Pierre                                         
""")

print("Chargement de la trajectoire des lipides...")
# Stockage de la trajectoire dans une variable
trajectory = md.load_xtc("E:/MODELISATION/input/md_200ns_OK.xtc",
                         top="E:\MODELISATION\input\start.pdb")
print(trajectory)
print("Chargement de la topologie a partir de la trajectoire...")
# Stockage de la topologie
topology = trajectory.topology
print(topology)

# Test de liste de distance pour 1 atome et 1 fenetre:
#distances_list = get_distances_list(trajectory, 50, 61)
#print(distances_list)

# Test liste de distances pour 1 fenetre mais pour tous les atomes de phosphate
atoms_dict = get_atoms_dict(trajectory, topology, 50)
print(atoms_dict)

# Initialisation de la liste des intervalles de fenêtres
# On a 2002 frames pour une trajectoire de 200 ns
frame_windows = [10, 50, 100, 200, 300, 500, 700, 1000, 2000]

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