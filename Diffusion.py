#!/usr/bin/env python2.7
# coding=utf-8
###############################################################################
##############################PROJET MODELISATION##############################
###############################################################################
import mdtraj as md
import csv
import math

def get_distance(trajectory, atom, frame, frame_window):
    """
    Pour un atome et une fenetre de temps donnee, calcule la distance entre
    la position de l'atome de reference au debut de la fenetre et sa position
    a la fin.
    :param trajectory:
    :param atom:
    :param frame:
    :return:
    """
    return (
        # La racine carree a ete ignore car elle ralenti le script et ne
        # change pas les distances relatives
        math.sqrt(
            ((trajectory.xyz[frame, atom][0] - trajectory.xyz[frame +
                                                              frame_window,
                                                              atom][0]
          ) ** 2)
        + ((trajectory.xyz[frame, atom][1] - trajectory.xyz[frame +
                                                            frame_window,
                                                            atom][1]
            ) ** 2)
        )
    )

def get_distances_list(trajectory, frame_window, atoms_list, atom):
    """
    Genere les distances pour une fenetre de temps, pour un atome de reference
    et les empile dans la liste atoms_list dans les arguments
    :param trajectory:
    :param frame_window:
    :param atom:
    :return:
    """
    # Parcours de l'ensemble des frames
    # print("Nombre total de frames : ", trajectory.n_frames - frame_window)
    frame = 0
    last_frame = trajectory.n_frames - frame_window
    while frame < last_frame:
        # print(frame)
        atoms_list.append(
            get_distance(trajectory, atom, frame, frame_window)
        )
        frame += 10

    return 1

def get_atoms_list(trajectory, topology, frame_window):
    """
    Genere une liste des distances pour chaque atomes pour 1 fenetre donnee
    :param trajectory:
    :param topology:
    :param frame_window:
    :return:
    """
    atoms_list = []
    for atom in topology.atoms:
        if atom.name == "P1":
            get_distances_list(trajectory, frame_window, atoms_list,
                               atom.index)
    return atoms_list

def get_clusters(list, slice_range):
    """

    :param list:
    :param slice_range:
    :return:
    """
    slice_start = 0
    # declaration de la liste des clusters
    hist = []
    while slice_start <= max(list):
        hist.append([value for value in list if (
            value > slice_start and value <= slice_start + slice_range)])
        slice_start += slice_range
    return hist


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
#atoms_dict = get_atoms_dict(trajectory, topology, 50)
#print(atoms_dict)

# Initialisation de la liste des intervalles de fenetres
# On a 2001 frames pour une trajectoire de 200 ns
frame_windows = [10, 50, 100, 200, 300, 500, 700, 1000, 2000]

# Test liste de distances pour 1 fenetre mais pour tous les atomes de phosphate
frames_dict = {}
for window in frame_windows:
    frames_dict[window] = get_atoms_list(trajectory, topology, window)

with open('output\diffusion.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)
    for key in frames_dict.keys():
        #fenetre cluster effectif
        clusters_list = get_clusters(frames_dict[key], slice_range = 0.1)
        for index in range(0, len(clusters_list)):
            # Calcul du nombre de valeurs dans le cluster
            length = len(clusters_list[index])
            writer.writerow([
                key,
                index,
                length
            ])