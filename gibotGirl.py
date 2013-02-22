#!/usr/bin/env python2
# -*- coding: utf8 -*-
 
import irclib
import ircbot
import time 
import re
from random import randrange

class BotManon(ircbot.SingleServerIRCBot):
	
	def __init__(self):
		ircbot.SingleServerIRCBot.__init__(self, [("irc.freenode.net", 6667)], "gibotGirl", "Bot réalisé en Python avec ircbot")
		self.mots = ["&help", "&list_plugins"]
		self.punch = ["donne un coup de fouet à", "donne un coup de poing à", "donne un coup de pied à", "casse les cotes de", "donne un coup de fouet à", "donne un coup de pelle à", "donne un coup de tête à"]
		self.plugins = ["&volka", "&coffee", "&punch", "&fuck", "&ff", "&tea", "&recherche"]		

	def on_welcome(self, serv, ev):
		serv.join("#crunchbang-fr")
		
	def on_pubmsg(self, serv, ev):
		auteur = irclib.nm_to_n(ev.source())
		canal = ev.target()
		arg1 = ev.arguments()[0].lower() 	
		arg2 = arg1.split(" ")
		nombreArg = len(arg2)
		
		for mot in self.mots:

			if mot in arg2[0]:
				
				if (mot == "&help"):
					if nombreArg < 2:
						serv.action(canal, "<&help>  <plugins> ")
						serv.action(canal, "<&list_plugins>")
						break
					else:
						for mot2 in self.plugins:
							if mot2 in arg2[0]:
								serv.action(canal, "{0} <speudo>".format(mot2))
								break
							else:
								serv.action(canal, "Plugin non existant")
								break
				elif (mot == "&list_plugins"):
					serv.action(canal, "Plugins: {0}".format(self.plugins))
					break
				
		for mot in self.plugins:
			
			if mot in arg2[0]:
				
				if (mot == "&coffee"):
					if nombreArg < 2 :
						serv.action(canal, "gibotGirl paye son café à {0}".format(auteur))
						break
					else:
						serv.action(canal, "{0} paye son café à {1}".format(auteur, arg2[1]))
						break
						
				if (mot == "&punch"):
					if nombreArg >= 2:
						act  = randrange(0,len(self.punch))
						serv.action(canal, "{0} {1}".format(self.punch[act], arg2[1]))
						break
						
				if (mot == "&volka"):
					if nombreArg < 2:
						serv.action(canal, "gibotGirl trinque avec {0}".format(auteur))
						break
					else:
						droit = randrange(1,9)
						if (droit == 1) or (droit == 2):
							serv.action(canal, "Non {0} a trop prit de volka".format(arg2[1]))
							break
						elif (droit == 3):
							serv.action(canal, "plus de volka gibotGirl a tout bu ...")
							break
						else:
							serv.action(canal, "{0} paye une volka a {1}".format(auteur, arg2[1]))
							break
				if (mot == "&ff"):
					if nombreArg >= 2:
						serv.action(canal, "La solution pour {0} se trouve sur le wiki:".format(arg2[1]))
						serv.action(canal, "http://crunchbanglinux-fr.org/wiki/?do=search&id={0}".format(arg2[1]))
						serv.action(canal, "et sur le fofo")
						serv.action(canal, "http://crunchbanglinux-fr.org/forum/search.php?action=search&keywords={0}".format(arg2[1]))
						break
				if (mot == "&tea"):
					if nombreArg < 2:
						serv.action(canal, "gibotGirl met la bouilloire sur le feu...")
						time.sleep(2)
						serv.action(canal, "et ça chauffe")
						serv.action(canal, "et ça infuse")
						time.sleep(4)	
						serv.action(canal, "gibotGirl sert du thé à {0}".format(auteur))
						break
				if (mot == "&recherche"):
					if nombreArg >= 3 :
						
						if re.match("w", arg2[2]):
							serv.action(canal, "dans le wiki: http://crunchbanglinux-fr.org/wiki/?do=search&id={0}".format(arg2[1]))
							pass
						if re.match("f", arg2[2]):
							serv.action(canal, "http://crunchbanglinux-fr.org/forum/search.php?action=search&keywords={0}".format(arg2[1]))
							pass
						if re.match("e", arg2[2]):
							serv.action(canal, "http://crunchbang.org/forums/search.php?action=search&keywords={0}".format(arg2[1]))
							pass 
						break 
					else:
						serv.action(canal, "usage: &search  <sujet< w[iki] f[orum] e[nglish] keyword1+keyword2+....")
						break
							
	def on_action(self, serv, ev):
		auteur = irclib.nm_to_n(ev.source())
		canal = ev.target()
		message = ev.arguments()[0].lower()
		if "fessée" in message:
			serv.action(canal, "donne un coup de fouet à {0} pour le calmer".format(auteur))
				
	def on_kick(self, serv, ev):
		serv.join("crunchbang-fr")
		serv.action(canal, "Bha non tu peux pas me sortir")
		
if __name__ == "__main__":
    BotManon().start()		
										
