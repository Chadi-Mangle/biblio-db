#!/usr/bin/env python3 
import json
from biblio import livre
from pathlib import Path

class Bibliotheque:
	def __init__(self):
		self.livre = []
		self.bdd = "{}/biblio.json".format(Path.home())

		try: 
			f = open(self.bdd)
			print("Chargement de la base de donnée situé à '{}'...".format(self.bdd))
			d = json.loads(f.read())
			self.genre = list(['Genre'])
			for l in d['Livre']: 
				self.livre.ajoute_livre(l['titre'], l['annee'], l["genre"])
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
			raise ValueError
	
	def ajoute_livre(self, titre, annee, genre): 
		new_livre = livre.Livre(titre, annee, genre)
		if len(self.livre) > 0:
			for i in range(len(self.livre)): 
				if new_livre < self.livre[i]:
					self.livre.insert(i, new_livre)
					return
		self.livre.append(new_livre)
	
	def affiche_genre(self): 
		p =''
		for i in range(len(self.genre)):
			p += "\n{}. {}".format(i+1, self.genre[i]) 
		return p

	def supp_livre(self, livre):
		for l in self.livre:
			if l.titre == livre:
				self.livre.remove(l)
				return l

	def supp_genre(self, genre):
		# try:
		self.genre.remove(genre)
		for l in self.livre: 
			if l.genre == genre: 
				l.genre = ""

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
