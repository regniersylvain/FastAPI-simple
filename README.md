# FastAPI-simple

## Ceci est un exemple simple de programmation d'une API via le framework FastAPI

## Elle intègre les endpoint suivants :

- `/val` qui retourne une valeur entière aléatoire comprise entre 0 et 100 <br></br> 
- `/val?nb=n` (où n est un nombre entier positif) qui retourne du code json contenant un tableau de n valeurs entières aléatoires comprises en -1000 et +1000<br></br>
- `/calc/add?n1=n&n2=m` (où n et m sont des nombres entiers positifs) retourne un simple texte contenant le résultat de l’addition de n et m<br></br>
- `/calc/prod?n1=n&n2=m` (où n et m sont des nombres entiers positifs) retourne un code HTML mis en forme qui présente dans un navigateur le calcul du produit de n et m sous la forme 4 x 5 = 20<br></br>
- `/img?num=n` (où n vaut un chiffre compris en 1 et 9) pour retourner une des 9 images possibles, que vous retournerez depuis le lien suivant : https://www.juleshaag.fr/devIA/devAPI/1.png (pour l’image n°1, par exemple) sans les télécharger et les intégrer à votre serveur local, car elles peuvent être amenées à changer...<br></br>
- `/stations_velo?id=n` retourne l’ensemble des infos sur la station n (sous forme d’un document json) prises dans le document json : https://www.juleshaag.fr/devIA/devAPI/station_information.json qui contient les infos des stations de vélo en libre service de Besançon. (le fichier devra être lu sur la source sans le télécharger pour l’intégrer à votre serveur local, car il peut être amené à changer...)<br></br>
- `/stations_velo?id=n&addr` qui retourne l’adresse de la station de vélo n, sous forme d’un texte<br></br>
- `/stations_velo?id=n&cap` qui retourne la capacité de la station de vélo n, sous forme d’un nombre entier<br></br>
- `/stations_velo?id=toutes&cap` qui retourne la capacité totale de l’ensemble des stations contenues dans le fichier<br></br>
- `/stations_velo/n/addr` c'est un endpoint qui est une variante du précédent) qui retourne l’adresse de la station de vélo n, sous forme d’un texte<br></br>
- `/stations_velo/n/cap` qui retourne la capacité de la station de vélo n, sous forme d’un nombre entier<br></br>
- `/stations_velo/toutes/cap` qui retourne un json contenant, par id, la capacité de chaque station ainsi que la capacité de l’ensemble des stations contenues dans le fichier<br></br>


# Installation :

### Installer les modules complémentaires :
`pip install -r requirements.txt`

# Lancement de l'API :
`python.exe .\main.py`

