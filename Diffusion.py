# -*- coding: cp1252 -*-
################################################################################
##############################PROJET MODELISATION###############################
################################################################################

# -*- coding: Utf8 -*-




def ReadPositions(filename):
    """
        Extrait la liste des s�quences d'un fichier Fasta
        Argument : 
    """

    chdir("E:/MODELISATION/input/DataDiffusion" )
    obj = open(nom, 'r')
    regle = re.compile(r"[OUI]", re.MULTILINE) #mettre la r�gle de parsing ici
    rep = []
    seq = ""
    while 1:
        ligne = obj.readline()
        if (ligne ==""):
            break
        elif (regle.match(ligne)):
            rep.append(seq)
            seq=""
    rep.append(seq)
    obj.close()
    chdir("E:/MODELISATION/input/DataDiffusion" )
    return(rep[1:])
