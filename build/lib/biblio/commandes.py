def affiche_menu():
	print("""*************
[M] Menu principal
[LG] Liste des Genres
[LL] Liste des Livres
[NG] Nouveau Genre
[NL] Nouveau Livre
[SG] Suppresion d'un Genre
[SL] Suppresion d'un Livre
[Q] Quitter le programme
*************""") 

def nouveau_genre(obj_bibli:object):
	genre = input("Donnez un nouveau genre: ")
	obj_bibli.ajoute_genre(genre)

def nouveau_livre(obj_biblio:object): 
	titre = input("Titre :") 
	annee = input("Année :") 
	genre = input("Genre :") 
	
	obj_biblio.ajoute_livre(titre, annee, genre)

def affiche_genre(obj_biblio:object):
	print(obj_biblio.affiche_genre()) 

def supp_genre(obj_biblio:object): 
	genre = input("Quel genre voulez vous supprimer: ")
	obj_biblio.supp_genre(genre)

def supp_livre(obj_biblio:object): 
	livre = input("Quel livre voulez vous supprimer: ")
	obj_biblio.supp_livre(livre)

def save(obj_biblio:object):
	obj_biblio.save() 
