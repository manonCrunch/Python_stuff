#!/usr/bin/env python2
# -*- coding: utf8 -*-
 
import irclib
import ircbot
import time
import re
import os
import optparse
from random import randrange
from os import chdir

NOM = os.environ['USER']
chdir("/home/{0}/".format(NOM))

try:
	os.mkdir(".gibotGirl")
except OSError:
	pass 
	
chdir(".gibotGirl")

class BotManon(ircbot.SingleServerIRCBot):

	def __init__(self):
		ircbot.SingleServerIRCBot.__init__(self, [("irc.freenode.net", 6667)],
							"gibotGirl", "Bot réalisé en Python avec ircbot")
		self.plugins = ["&help", "&list_plugins", "&recherche", "&vodka", "&coffee",
						"&punch", "&tea", "&kiss", "&donuts", "&spam"]
		self.punch = ["donne un coup de fouet à", "donne un coup de poing à", "donne un coup de pied à", 
						"casse les cotes de", "donne un coup de fouet à", "donne un coup de pelle à", 
						"donne un coup de tête à"]
	  	
	def on_welcome(self, serv, ev):
		serv.join("#crunchbang-fr")
	
	def on_pubmsg(self, serv, ev):
		auteur = irclib.nm_to_n(ev.source())
		canal = ev.target()
		message = ev.arguments()[0].lower() 	
		arguments = message.split(" ")
		nombreArg = len(arguments)
		print "{0} : {1}".format(auteur, message)
		historique = open('log.txt','a')
		historique.write("{0} : {1} \n".format(auteur, message))
		historique.close()
		
		if re.match("^bonjour", message) or re.match("^salut", message):
			if nombreArg >= 2 :
				if (arguments[1] == "gibotgirl") or (arguments[1] == "gibotGirl"):
					serv.privmsg(canal, "bonjour {0}".format(auteur))
			
		if re.match("^&recherche", message):
			if nombreArg >= 3 :

				if re.match('.*w.*', arguments[-1]):
					serv.action(canal, 
                                "dans le wiki: http://crunchbanglinux-fr.org/wiki/?do=search&id={0}".format(arguments[1]))

				if re.match('.*f.*', arguments[-1]):
					serv.action(canal, 
                                "http://crunchbanglinux-fr.org/forum/search.php?action=search&keywords={0}".format(arguments[1]))

				if re.match('.*e.*', arguments[-1]):
					serv.action(canal, 
                                "http://crunchbang.org/forums/search.php?action=search&keywords={0}".format(arguments[1]))
			else:
				serv.action(canal, "usage: &recherche  <sujet> w[iki] f[orum] e[nglish] keyword1+keyword2+....")
		
		for mot in self.plugins:
			if mot in arguments[0]:
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
											
				if (mot == "&list_plugins"):
					serv.action(canal, "Plugins: {0}".format(self.plugins))
					break
		
				if (mot == "&punch"):
					if nombreArg >= 2:
						act  = randrange(0,len(self.punch))
						if (arguments[1] == "gibotgirl") or (arguments[1] == "gibotGirl"):
							serv.action(canal, "donne un gros coup de pelle à {0}".format(auteur))
							break
						else:
							serv.action(canal, "{0} {1}".format(self.punch[act], arguments[1]))
							break
				
				if (mot == "&kiss"):
					if nombreArg >= 2:
						if (arguments[1] == "*") or (arguments[1] == "all"):
							serv.privmsg(canal, "Je suis pas une fille facile")
							break
						elif (arguments[1] == "gibotgirl") or (arguments[1] == "gibotGirl"):
							break
						else:	
							serv.action(canal, "fait un bisous à {0}".format(arguments[1]))
							break
					else :
						serv.action(canal, "fait un bisous à {0}".format(auteur))
						break
				
				if (mot == "&tea"):
					if nombreArg >= 2:
						serv.action(canal, "met la bouilloire sur le feu...")
						time.sleep(2)
						serv.action(canal, "et ça chauffe")
						serv.action(canal, "et ça infuse")
						time.sleep(4)
						if (arguments[1] == "*") or  (arguments[1] == "all"):
							serv.action(canal, "sert du thé à tout le monde")
							break
						serv.action(canal, "sert du thé à {0}".format(arguments[1]))
						break
				
				if (mot == "&vodka"):
					if nombreArg < 2:
						serv.action(canal, "prend une volka avec {0}".format(auteur))
						break
					else:
						if (arguments[1] == "*") or (arguments[1] == "all") :
							serv.action(canal, "paye sa tournée de vodka")
							break
						droit = randrange(1,9)
						if (droit == 1) or (droit == 2):
							serv.action(canal, "Non {0} a trop prit de vodka".format(arguments[1]))
							break
						elif (droit == 3):
							serv.action(canal, "plus de voldka gibotGirl a tout bu ...")
							break
						else:
							serv.action(canal, "{0} paye une vodka a {1}".format(auteur, arguments[1]))
							break
				
				if (mot == "&coffee"):
					if nombreArg < 2 :
						serv.action(canal, "paye son café à {0}".format(auteur))
						break
					else:
						if (arguments[1] == "*") or (arguments[1] == "all"):
							serv.action(canal, "paye sa tournée de café")
							break
						serv.action(canal, "{0} paye son café à {1}".format(auteur, arguments[1]))
						break
				
				if (mot == "&donuts"):
					if nombreArg < 2 :
						serv.action(canal, "&donuts + <speudo>")
						break
					else:
						act  = randrange(1,6)
						if (act == 1) or (act == 2):
							serv.privmsg(canal, "Homer a tout mangé")
							break
						elif (arguments[1] == "*") or (arguments[1] == "all"):
							serv.action(canal, "paye sa tournée de Donuts")
							break
						else:
							serv.action(canal, "{0} paye son Donuts à {1}".format(auteur, arguments[1]))
							break

				if(mot == "&spam"):
					if nombreArg >= 2 :
						spam = 0
						
						if (arguments[1] == "Manon_crunch") or (arguments[1] == "manon") :
							serv.privmsg(canal, "On ne peut pas faire ça a Manon")
							break
						if (arguments[1] == "gibotgirl") or (arguments[1] == "gibotGirl") :
							serv.privmsg(canal, "Attention !!!")
							while spam < 10 :
								spam += 1
								serv.privmsg("{0}".format(auteur), "On ne spam pas gibotGirl!!!")
								time.sleep(2)
							break	
							
						else :
							serv.privmsg(canal, "Mission Spam enclenchée")
							while spam < 10 :
								spam += 1
								serv.privmsg("{0}".format(arguments[1]), "spam spam spam")
								time.sleep(2)
							break		
				
	def on_action(self, serv, ev):
		auteur = irclib.nm_to_n(ev.source())
		canal = ev.target()
		message = ev.arguments()[0].lower()
		
		print "{0} : {1}".format(auteur, message)
		historique = open('log.txt','a')
		historique.write("{0} : {1} \n".format(auteur, message))
		historique.close()
		if "fessée" in message:
			serv.action(canal, "donne un coup de fouet à {0} pour le calmer".format(auteur))

			
	def on_kick(self, serv, ev):
		serv.join("crunchbang-fr")
		serv.action(canal, "Bha non tu peux pas me sortir")



if __name__ == "__main__":
    BotManon().start()		
