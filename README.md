# TP2:TurtleBot3 Waffle Pi Navigation & Localization
## _Author: Antoaroo, Aumeer & Bhooto_

#### Partie 2

1.Rendez-vous sur la page Navigation du E-Manual de Robotis(pour noetic)

- Premierement il faut ouvrir un terminal et lancer le roscore

2.Lancer les nœuds de navigation et placer le robot sur la map que vous avez générée au TP précédent(ou lacarte corrigée)

- On ouvre un autre terminal et il faut connecter a la Raspeberry pi et connecte avec son adresse IP en utilisant la commande suivant:

```sh
ssh ubuntu@11.255.255.201
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

- Ensuite il faut lancer la navigation en utilisant le code suivant: 

```sh
export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=home/info/map_tb5/map_tb5_cleaned_full_pgm
```

5.Créer  un  package move_turtle,  dans  ce  package  vous  devrez  créer  un nœud qui vapublier sur move_base_simple/goal et envoyer des positions au turtlebot.

Car on avait deja notre workspace, on est aller dans notre fichier src pour creer le package en utilisant la commande suivant: 

```sh
catkin_create_pkg move_turtle rospy roscpp geometry_msgs std_msgs
```

a.Dans  un  premier  temps,  en  utilisant  rviz  et le  bouton  2D  pose  estimate, déterminer 3 coordonnées de point où vous enverrez le robot par la suite.

On doit chercher le 3 coordonées de point:

```sh
rostopic echo /initialPose
```
On doit utiliser rviz et il faut selectionner 3 points sur l'image [2d pose Estimate] [df1] qui va former un cycle

b.Créer un nœud goto.py    ce    dernier devra publier    sur    le    topic move_base_simple/goal. Tester le nœudavec un point de la question 5a

On utilise les commandes suivants pour creer un noeud et donner le droit d'execution au fichier:

```sh
nano goto.py 
chmod +x goto.py
```
Ensuite il faut faire source du fichier setup.bash qui situe dans le dossier devel

Maintenant il faut faire un rosrun pour faire le turtlebot deplacer un point.

```sh
rosrun move_turtle goto.py
```




