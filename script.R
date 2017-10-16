# Script permettant la visualisation de la distribution de la présence de lipides en fonction de la distance parcourue latéralement pour une fenetre de temps donnée


# lecture du fichier CSV
# /!\ mettre son propre path /!\
data = read.csv("/Users/Anatole/Downloads/diffusion.csv", header=TRUE, sep=";")

# calcul de l’effectif total par fenetre
sum = aggregate(data$effectif, by=list(fenetre=data$fenetre), FUN=sum)

# calcul de la probabilité de présence pour chaque interval de distance
data = merge(data, sum, by="fenetre")
data = transform(data, p = effectif / x)

# suppression des données non pertinentes (supérieur à une distance de 40)
#data = data[!(data$distance>40),]


# représentation graphique de la probabilité de présence pour chaque interval de temps et pour chaque fenêtre, en utilisant ggplot
graph = ggplot(data = data, aes(x=distance, y=p, colour=as.factor(fenetre), shape=as.factor(fenetre))) + geom_line(size=0.5) + geom_point(size=2) + scale_shape_manual(values=as.factor(fenetre)) + ggtitle("Distribution de la presence de lipides en fonction de la distance parcourue pour une fenetre de temps donnee")

# affichage
print(graph)


