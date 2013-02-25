#!/usr/bin/env python2
# -*- coding: utf8 -*-
 
import irclib
import ircbot
import time
import re
from random import randrange

class BotManon(ircbot.SingleServerIRCBot):
	'''-------------------------------------'''
	
	def __init__(self):
		ircbot.SingleServerIRCBot.__init__(self, [("irc.freenode.net", 6667)], "gibotGirl", "Bot réalisé en Python avec ircbot")
		self.plugins = ["&help", "&list_plugins", "&recherche", "&volka", "&coffee", "&punch", "&tea", "&kiss", "&donuts"]
		self.punch = ["donne un coup de fouet à", "donne un coup de poing à", "donne un coup de pied à", "casse les cotes de", "donne un coup de fouet à", "donne un coup de pelle à", "donne un coup de tête à"]
		
	'''----------------------------------------------------------------'''	  	
	def on_welcome(self, serv, ev):
		serv.join("#crunchbang-fr")
		
	'''----------------------------------------------------------------'''	
	def on_pubmsg(self, serv, ev):
		auteur = irclib.nm_to_n(ev.source())
		canal = ev.target()
		message = ev.arguments()[0].lower() 	
		arguments = message.split(" ")
		nombreArg = len(arguments)
		'''------------------------------------------------------------------------'''
		if re.match("^bonjour", message) or re.match("^salut", message):
			if nombreArg >= 2 :
				if (arguments[1] == "gibotgirl") or (arguments[1] == "gibotGirl"):
					serv.action(canal, "bonjour {0}".format(auteur))
		'''--------------------------------------------------------------------------'''			
		if re.match("^&recherche", message):
			if nombreArg >= 3 :
						
				if re.match("w", arguments[2]):
					serv.action(canal, "dans le wiki: http://crunchbanglinux-fr.org/wiki/?do=search&id={0}".format(arguments[1]))
							
				if re.match("f", arguments[2]):
					serv.action(canal, "http://crunchbanglinux-fr.org/forum/search.php?action=search&keywords={0}".format(arguments[1]))
							
				if re.match("e", arguments[2]):
					serv.action(canal, "http://crunchbang.org/forums/search.php?action=search&keywords={0}".format(arguments[1]))
		 
			else:
				serv.action(canal, "usage: &recherche  <sujet> w[iki] f[orum] e[nglish] keyword1+keyword2+....")
		'''--------------------------------------------------------------------------------------------------------------------------------------'''		
		for mot in self.plugins:
			if mot in arguments[0]:
				'''--------------------------------------------------------------------'''
				if (mot == "&help"):
					if nombreArg < 2:
						serv.action(canal, "<&help>  <plugins> ")
						serv.action(canal, "<&list_plugins>")
						break
					else:
						for mot2 in self.plugins:
							if mot2 in arguments[0]:
								serv.action(canal, "{0} <speudo>".format(mot2))
								break
							else:
								serv.action(canal, "Plugin non existant")
								break
				'''------------------------------------------------------------------------------'''			
				if (mot == "&list_plugins"):
					serv.action(canal, "Plugins: {0}".format(self.plugins))
					break
				'''------------------------------------------------------------------------------'''
				if (mot == "&punch"):
					if nombreArg >= 2:
						act  = randrange(0,len(self.punch))
						if (arguments[1] == "gibotgirl") or (arguments[1] == "gibotGirl"):
							serv.action(canal, "donne un gros coup de pelle à {0}".format(auteur))
							break
						else:
							serv.action(canal, "{0} {1}".format(self.punch[act], arguments[1]))
							break
				'''------------------------------------------------------------------------------'''
				if (mot == "&kiss"):
					if nombreArg >= 2:
						if (arguments[1] == "*") or (arguments[1] == "all"):
							serv.privmsg(canal, "Je suis pas une fille facile")
							break
						elif:	
							serv.action(canal, "fait un bisous à {0}".format(arguments[1]))
							break
					else :	
						serv.action(canal, "fait un bisous à {0}".format(auteur))
						break
				'''------------------------------------------------------------------------------'''
				if (mot == "&tea"):
					if nombreArg >= 2:
						serv.action(canal, "met la bouilloire sur le feu...")
						time.sleep(2)
						serv.action(canal, "et ça chauffe")
						serv.action(canal, "et ça infuse")
						time.sleep(4)	
						serv.action(canal, "sert du thé à {0}".format(arguments[1]))
						break
				'''-------------------------------------------------------------------------------'''
				if (mot == "&volka"):
					if nombreArg < 2:
						serv.action(canal, "prend une volka avec {0}".format(auteur))
						break
					else:
						if (arguments[1] == "*") or (arguments[1] == "all") :
							serv.action(canal, "paye sa tournée de volka")
							break
						droit = randrange(1,9)
						if (droit == 1) or (droit == 2):
							serv.action(canal, "Non {0} a trop prit de volka".format(arguments[1]))
							break
						elif (droit == 3):
							serv.action(canal, "plus de volka gibotGirl a tout bu ...")
							break
						else:
							serv.action(canal, "{0} paye une volka a {1}".format(auteur, arguments[1]))
							break
				'''--------------------------------------------------------------------------------------------'''
				if (mot == "&coffee"):
					if nombreArg < 2 :
						serv.action(canal, "gibotGirl paye son café à {0}".format(auteur))
						break
					else:
						if (arguments[1] == "*") or (arguments[1] == "all"):
							serv.action(canal, "paye sa tournée de café")
							break
						serv.action(canal, "{0} paye son café à {1}".format(auteur, arguments[1]))
						break
				'''------------------------------------------------------------------------------------
				if (mot == "&ff"):
					if nombreArg >= 2:
						serv.action(canal, "La solution pour {0} se trouve sur le wiki:".format(arguments[1]))
						serv.action(canal, "http://crunchbanglinux-fr.org/wiki/?do=search&id={0}".format(arguments[1]))
						serv.action(canal, "et sur le fofo")
						serv.action(canal, "http://crunchbanglinux-fr.org/forum/search.php?action=search&keywords={0}".format(arguments[1]))
						break
						
			-----------------------------------------------------------------------------'''
	'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''									
	def on_action(self, serv, ev):
		auteur = irclib.nm_to_n(ev.source())
		canal = ev.target()
		message = ev.arguments()[0].lower()
		if "fessée" in message:
			serv.action(canal, "donne un coup de fouet à {0} pour le calmer".format(auteur))
			
	
	'''------------------------------------------------------------------------------------------'''			
	def on_kick(self, serv, ev):
		serv.join("crunchbang-fr")
		serv.action(canal, "Bha non tu peux pas me sortir")
		
		
	'''-------------------------------------------------------------------------------------------'''
	
	
if __name__ == "__main__":
    BotManon().start()		
										
