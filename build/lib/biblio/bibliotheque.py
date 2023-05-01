#!/usr/bin/env python3 
import json
from biblio import livre
from pathlib import Path

class Bibliotheque:
	def __init__(self):
		self.livre = []
		self.bdd = "{}/bib.json".format(Path.home())

		try: 
			f = open(self.bdd)
			print("Chargement de la base de donnée '{}'...".format(self.bdd))
			d = json.loads(f.read())
			self.genre = list(['Genre'])
			for l in d['Livre']: 
				self.livre.append(livre.Livre(l['titre'], l['annee'], l["genre"]))
		except: 
			self.genre = []
			
	def genre_existe(self, genre): 
		if genre in self.genre: 
			return True
		return False
	def ajoute_genre(self, genre): 
		if not self.genre_existe(genre):
			self.genre.append(genre) 
		else:
			print("Le genre '{}' existe déjà !".format(genre))
	
	def ajoute_livre(self, titre, annee, genre): 
		if not self.genre_existe(genre): 
			print("Le genre n'existe pas")
			return
		l = livre.Livre(titre, annee, genre)	
		self.livre.append(l)
	
	def affiche_genre(self): 
		p = "Tout les genres de livres dans la biblioothèque ({}) :".format(len(self.genre))
		for i in range(len(self.genre)):
			p += "\n{}. {}".format(i+1, self.genre[i]) 
		return p

	def supp_livre(self, livre):
		try:
			self.livre.remove(livre)
			print("Le livre '{}' a bien été supprimé.".format(livre))
		except ValueError:
			print("Le livre n'est pas dans la bibliothèque.") 

	def supp_genre(self, genre):
		try:
			self.genre.remove(genre)
			print("Le genre '{}' a bien été supprimé.".format(genre))
		except ValueError:
			print("Le genre n'est pas dans la bibliothèque.")
	def save(self):
		biblio_dictionary = {"livre": [], "genre": self.genre}
		for i in self.livre: 
			biblio_dictionary['livre'].append(i.dictionaire())
		print(biblio_dictionary)
		with open(self.bdd, "w") as file: 
			file.write(json.dumps(biblio_dictionary, indent=4))

	def __str__(self):
		p="Tout les livres de la bibliothèque ({}) :".format(str(len(self.livre))) 
		for i in self.livre:
			p+= "\n" + str(i)
		return p