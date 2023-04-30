#!/usr/bin/env python3 

"""Script contenant la classe livres"""

class Livre: 
	def __init__(self, titre, annees, genre):
		self.titre = titre
		self.annees = annees
		self.genre = genre
	
	def __str__(self): 
		if self.genre != "": 
			return  str(self.annees) + " [" + self.genre +  "] " + self.titre
		return self.annees + self.titre
	
	def dictionaire(self): 
		return {'titre': self.titre, 'annees': self.annees, "genre": self.genre}
