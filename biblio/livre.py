#!/usr/bin/env python3 

"""Script contenant la classe livres"""

class Livre: 
	def __init__(self, titre, annees, genre):
		self.titre = titre
		self.annees = annees
		self.genre = genre
	
	def __str__(self)->str: 
		"""
		Renvoie un l'objet livre sous forme de livre sous la forme: \n
		annees [genre] titre
		si le livre n'as pas de genre il sera ajouté sous la forme: \n
		annees titre
		"""
		if self.genre != "": 
			return  str(self.annees) + " [" + self.genre +  "] " + self.titre
		return self.annees + self.titre
	
	def dictionaire(self)->dict: 
		"""Crée un dictionaire a partir d'un objet livre
		"""
		return {'titre': self.titre, 'annees': self.annees, "genre": self.genre}

	def __lt__(self, other)->bool: 
		"""Permet de comparer deux objets livre entre eux. 
		On commpare en premier l'année, ensuite le genre et puis le titre		
		"""
		livre = [self.annees, self.genre, self.titre]
		livre_other = [other.annees, other.genre, other.titre]

		for i in range(len(livre)): #si les élements sont égaux on retourne la comparaison entre les éléments suivant
			if livre[i] != livre_other[i]: 
				return  livre[i] < livre_other[i]
			
			
