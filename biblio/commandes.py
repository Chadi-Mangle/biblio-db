#!/usr/bin/env python3

"""Lien entre les classes et le fichier bibliodb"""

def affiche_menu():
	"""
	Procédures permetant d'affichier le menu des commandes disponibles.
	"""
	print("""*************
[M] Menu principal
[LG] Liste des Genres
[LL] Liste des Livres
[NG] Nouveau Genre
[NL] Nouveau Livre
[SG] Suppresion d'un Genre
[SL] Suppresion d'un Livre
[Q] Quitter le programme et sauvgarder la base de donnée
*************""")

def nouveau_genre(obj_bibli:object):
	"""Ajoute un nouveau genre a l'object obj_bibli.
	Verifie si le genre n'existe pas déjà.
	obj_bibli: objet de la classe Bibliotheque
	"""
	genre = input("Donnez un nouveau genre: ")
	try:
		obj_bibli.ajoute_genre(genre)
	except ValueError:
		print("Le genre '{}' existe déjà !".format(genre))

def nouveau_livre(obj_biblio:object):
	"""Ajoute un nouveau livre a l'object obj_bibli.
	Vérifie si le livre qu'on ajoute à un genre existant.
	Utilise la méthode genre_existe et ajoute_genre de la classe bibliothèque
	obj_bibli: objet de la classe Bibliotheque
	
	"""
	titre = input("Titre :")
	annee = input("Année :")
	genre = input("Genre :")

	if not obj_biblio.genre_existe(genre):
		print("Le genre n'existe pas")
		choix = input("Voulez vous ajouter ce genre à la bibliothèque ? ")
		if choix.lower() in ["oui", "o",  "y", "yes"]:
			obj_biblio.ajoute_genre(genre)
		else:
			print("Le livre ne va donc pas être ajouté a la bibliothèque.")

	obj_biblio.ajoute_livre(titre, annee, genre)

def affiche_genre(obj_biblio:object):
	"""Affiche les genres de livre disponible dans la bibliothèque.
	obj_bibli: objet de la classe Bibliotheque
	Utilise la méthode affiche genre de la classe Bibliotheque
	"""
	print("""Tout les genres de livres dans la biblioothèque ({}):{}""".format(
		len(obj_biblio.genre),obj_biblio.affiche_genre()))

def supp_genre(obj_biblio:object):
	"""Supprime un genre d'une bibliothèque.
	Vérifie que le genre existe.
	obj_bibli: objet de la classe Bibliotheque
	"""
	genre = input("Quel genre voulez vous supprimer: ")
	try:
		obj_biblio.supp_genre(genre)
		print("Le genre '{}' a bien été supprimé.".format(genre))
	#la fonction remouve renvoie une ValueError si l'elemment n'est pas dans la liste
	except ValueError:
		print("Le genre n'est pas dans la bibliothèque.")

def supp_livre(obj_biblio:object):
	"""Supprime un livre de la bibliothèque
	Vérifie si le livre existe.
	obj_bibli: objet de la classe Bibliotheque	
	"""
	livre = input("Quel livre voulez vous supprimer: ")
	if obj_biblio.supp_livre(livre) is not None:
		print("Le livre '{}' a bien été supprimé.".format(livre))
	else: print("Le livre n'est pas dans la bibliothèque.")


def save(obj_biblio:object):
	"""Utilise la méthode save de la classe bibliotheque.
	Cette méthode permet de sauvgarder l'objet bibliothèque dans un fichier json.
	obj_bibli: objet de la classe Bibliotheque
	"""
	obj_biblio.save()
	print("Tout a bien été sauvegardé")

def quit_menu(obj_biblio:object):
	"""Quitte la bibliothèque et demmandes si on veut sauvegarder ou pas.
	obj_bibli: objet de la classe Bibliotheque.
	"""
	while 1:
		choix = input("Voulez vous sauvgarder la base de donné ? ")
		if choix.lower() in ["oui", "o", "y", "yes"]:
			save(obj_biblio)
			break
		if choix.lower() in ["n", "non", "no"]:
			print("Vous allez quiter sans sauvegarder")
			break
		print("Commande invalide.")
