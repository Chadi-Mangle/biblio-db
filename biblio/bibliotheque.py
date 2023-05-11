#!/usr/bin/env python3

"""Code gérant les differantes méthodes de la classe Bibliotheque"""

import json
from pathlib import Path
from biblio import livre

class Bibliotheque:
	"""La classe bibliothèque permet de crée un object bibliothèque 
	contenant une liste d'objet livre et de chaine de caractère de nom de genre"""
	def __init__(self):
		self.livre = []
		self.bdd = "{}/biblio.json".format(Path.home())
		#permet de modifier le fichier de chargement et de sauvgarde de la bibliothèque.
		#path.home() permet de mettre le fichier dans le dossier de l'utilisateur.

		try: #charge la base de donnée si existante
			with open(self.bdd, 'r', encoding="utf-8") as fichier:
				print("Chargement de la base de donnée situé dans le fichier '{}'...".format(self.bdd))
				#load permet de transformer un fichier json en dictionaire python
				dico = json.loads(fichier.read())
				#load crée une erreur si le fichier n'existe pas
				self.genre = list(dico['genre'])
				for each_livre in dico['livre']:
					self.ajoute_livre(each_livre['titre'], each_livre['annees'], each_livre["genre"])
		except FileNotFoundError:
			self.genre = []

	def genre_existe(self, genre:str)->bool:
		"""Vérifie si un genre est déjà dans la liste des genres de la bibliothèque.
		genre: chaine de caractère correspondant au genre de livres de la bibliothèque 
		"""
		if genre in self.genre:
			return True
		return False

	def ajoute_genre(self, genre):
		"""Ajoute un genre a la liste self.genre.
		Crée une erreur si le genre existe déjà
		genre: chaine de caractère correspondant au genre de livres de la bibliothèque 
		"""
		if not self.genre_existe(genre):
			self.genre.append(genre)
		else:
			raise ValueError # creer une erreur

	def ajoute_livre(self, titre, annee, genre):
		"""Ajoute un objet livre a la liste self.livre.
		titre: titre du nouveau livre 
		annee: année du nouveau livre
		genre: genre du nouveau livre
		"""
		new_livre = livre.Livre(titre, annee, genre)
		if len(self.livre) > 0: #pour pouvoir ajouter le première élément
			for index, livre_item in enumerate(self.livre):
				if new_livre < livre_item:
					#si un livre est inferieur à un autre il prend sa position dans la liste self.list
					#si le livre est inférieur a aucun autre il sera donc le dernier élément de la liste
					self.livre.insert(index, new_livre)
					return
		self.livre.append(new_livre)

	def affiche_genre(self)->str:
		"""
		Retourne la liste des genres sous forme de chaine de caractères
		"""
		genre_str =''
		#enumerate donne un objet qui contient l'élément d'une liste ainsi que sony index.
		for index, genre_item in enumerate(self.genre):
			genre_str += "\n{}. {}".format(index+1, genre_item)
		return genre_str

	def supp_genre(self, genre):
		"""Supprime un genre le la liste self.genre
		genre: chaine de caractère correspondant au genre de livres de la bibliothèque 
		"""
		self.genre.remove(genre) #crée une erreur si le genre n'est pas dans la liste
		for livre_item in self.livre:
			if livre_item.genre == genre:
				livre_item.genre = ""

	def supp_livre(self, obj_livre)->livre:
		"""Supprime un livre le la liste self.livre
		livre: objet livres appartenant à la bibliothèque 
		renvoie l'objet livre supprimer
		"""
		for livre_item in self.livre:
			if livre_item.titre == obj_livre:
				self.livre.remove(livre_item)
				return livre_item
		return None

	def save(self):
		"""Sauvegarde la bibliothèque dans un fichier json.	"""
		biblio_dictionary = {"livre": [], "genre": self.genre}
		for i in self.livre:
			biblio_dictionary['livre'].append(i.dictionaire())
		# print(biblio_dictionary)
		with open(self.bdd, "w" ,encoding="utf-8") as file:
			file.write(json.dumps(biblio_dictionary, indent=4))

	def __str__(self)->str:
		bibliotheque_str ="Tout les livres de la bibliothèque ({}) :".format(str(len(self.livre)))
		for i in self.livre:
			bibliotheque_str+= "\n" + str(i)
		return bibliotheque_str
