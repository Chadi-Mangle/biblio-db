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

	def __lt__(self, other): 
		livre = [self.annees, self.genre, self.titre]
		livre_other = [other.annees, other.genre, other.titre]

		for i in range(0,2): 
			if livre[i] != livre_other[i]:
				return  livre[i] < livre_other[i]
			
			
