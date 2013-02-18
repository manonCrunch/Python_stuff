#!/usr/bin/env python2
# -*- coding: utf8 -*-
 
import irclib
import ircbot
from random import randrange

class BotManon(ircbot.SingleServerIRCBot):
	
	def __init__(self):
		ircbot.SingleServerIRCBot.__init__(self, [("irc.freenode.net", 6667)], "gibotGirl", "Bot réalisé en Python avec ircbot")
		self.mots = ["bonjour", "salut", "!volka", "!coffee", "!punch", "bye", "!help", "!tea"]
		self.actions = ["donne un coup de fouet à", "donne un coup de poing à", "donne un coup de pied à", "casse les cotes de", "donne un coup de fouet à", "donne un coup de pelle à", "donne un coup de tête à"] 		

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
				
				if (mot == "bonjour") or (mot == "salut"):
					serv.action(canal, "Salut {0}".format(auteur))
					break 
					
				if (mot == "!coffee"):
					if nombreArg < 2 :
						serv.action(canal, "gibotGirl paye son café à {0}".format(auteur))
						break
					else:
						serv.action(canal, "{0} paye son café à {1}".format(auteur, arg2[1]))
						break
						
				if (mot == "!punch"):
					if nombreArg >= 2:
						act  = randrange(0,len(self.actions))
						serv.action(canal, "{0} {1}".format(self.actions[act], arg2[1]))
						break
						
				if (mot == "!volka"):
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
							
				if (mot == "!tea"):
					if nombreArg < 2:
						serv.action(canal, "gibotGirl met la bouilloire sur le feu...")
						serv.action(canal, "et ça chauffe")
						serv.action(canal, "gibotGirl sert du thé à {0}".format(auteur))
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
										
