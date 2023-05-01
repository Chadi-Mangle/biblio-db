#!/usr/bin/env python3 

"""Code gérant les differantes méthodes de la classe Bibliotheque"""
import json
from biblio import livre
from pathlib import Path

class Bibliotheque:
	def __init__(self):
		self.livre = []
		self.bdd = "{}/biblio.json".format(Path.home()) #permet de modifier le fichier de chargement et de sauvgarde de la bibliothèque.
			#path.home() permet de mettre le fichier dans le dossier de l'utilisateur.

		try: #charge la base de donnée si existante
			f = open(self.bdd)
			print("Chargement de la base de donnée situé dans le fichier '{}'...".format(self.bdd))
			d = json.loads(f.read()) #load permet de transformer un fichier json en dictionaire python 
			#load crée une erreur si le fichier n'existe pas 
			self.genre = list(d['genre'])
			for l in d['livre']: 
				self.ajoute_livre(l['titre'], l['annees'], l["genre"])
		except: 
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
			for i in range(len(self.livre)): 
				if new_livre < self.livre[i]: #si un livre est inferieur à un autre il prend sa position dans la liste self.list
					#si le livre est inférieur a aucun autre il sera donc le dernier élément de la liste
					self.livre.insert(i, new_livre)
					return
		self.livre.append(new_livre) 
	
	def affiche_genre(self)->str: 
		"""
		Retourne la liste des genres sous forme de chaine de caractères
		"""
		p =''
		for i in range(len(self.genre)):
			p += "\n{}. {}".format(i+1, self.genre[i]) 
		return p

	def supp_genre(self, genre):
		"""Supprime un genre le la liste self.genre
		genre: chaine de caractère correspondant au genre de livres de la bibliothèque 
		"""
		self.genre.remove(genre) #crée une erreur si le genre n'est pas dans la liste
		for l in self.livre: 
			if l.genre == genre: 
				l.genre = ""

	def supp_livre(self, livre)->livre:
		"""Supprime un livre le la liste self.livre
		livre: objet livres appartenant à la bibliothèque 
		renvoie l'objet livre supprimer
		"""		
		for l in self.livre:
			if l.titre == livre:
				self.livre.remove(l)
				return l
			
	def save(self):
		"""Sauvegarde la bibliothèque dans un fichier json.	"""
		biblio_dictionary = {"livre": [], "genre": self.genre}
		for i in self.livre: 
			biblio_dictionary['livre'].append(i.dictionaire())
		# print(biblio_dictionary)
		with open(self.bdd, "w") as file: 
			file.write(json.dumps(biblio_dictionary, indent=4))

	def __str__(self)->str:
		p="Tout les livres de la bibliothèque ({}) :".format(str(len(self.livre))) 
		for i in self.livre:
			p+= "\n" + str(i)
		return p
