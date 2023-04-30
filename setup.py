#!/usr/bin/env python3 

"""Script d'instalation du paquet biblio."""
import biblio
from setuptools import setup

setup(
	name="biblio",
	version=biblio.version,
	description="un paquet pour gérer des bibliothèques",
	packages=["biblio"], 
	scripts=["bibliodb"]
)
