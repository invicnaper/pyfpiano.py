#!/usr/bin/python
#	@author : hamza
#	a tiny piano written in python
#
#                   GNU LESSER GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
#
#
#  This version of the GNU Lesser General Public License incorporates
#the terms and conditions of version 3 of the GNU General Public
#License, supplemented by the additional permissions listed below.
#
#  0. Additional Definitions.
#
#  As used herein, "this License" refers to version 3 of the GNU Lesser
#General Public License, and the "GNU GPL" refers to version 3 of the GNU
#General Public License.
#
#  "The Library" refers to a covered work governed by this License,
#other than an Application or a Combined Work as defined below.
#
#  An "Application" is any work that makes use of an interface provided
#by the Library, but which is not otherwise based on the Library.
#Defining a subclass of a class defined by the Library is deemed a mode
#of using an interface provided by the Library.
#
#  A "Combined Work" is a work produced by combining or linking an
#Application with the Library.  The particular version of the Library
#with which the Combined Work was made is also called the "Linked
#Version".
#
import os
import sys
import pyglet
import Tkinter as tk
import pygame
import argparse
from pygame.locals import *
import time
from mingus.containers.note import Note
import mingus.core.notes as notes
from mingus.midi import fluidsynth
from mingus.containers import NoteContainer 
#from mingus import MidiFileOut

#=================
#	Util
#=================

RED 	= "\033[31m"
GREEN 	= "\033[32m"
BLUE 	= "\033[34m"
YELLOW 	= "\033[35m"
DEFAULT = "\033[0m"


ACTION 	= BLUE 	 + "[+] " + DEFAULT 
ERROR	= RED 	 + "[!] " + DEFAULT
OK 	= GREEN  + "[O] " + DEFAULT

SONG    = "sound/forever_in_love.mp3"

#=================
#	Parser
#=================

parser = argparse.ArgumentParser(description='pyfpiano.py is a tiny piano written in python')
parser.add_argument('--verbose',
    action='store_true',
    help='verbose flag' )
parser.add_argument('--play', nargs=1, help="start playing")
parser.add_argument('--pyf', nargs=1, help="playing note from a pyf file")
parser.add_argument('--methode',nargs=1,help="set a methode")
parser.add_argument('--save',nargs=1,help="save play to mdi file")
parser.add_argument('--note',nargs=1,help="set a note")

#=================
#	Notes
#=================

PIANO_A    = "sound/piano_A.mp3"
PIANO_A_SH = "sound/piano_A_sharp.mp3"
PIANO_B    = "sound/piano_B.mp3"
PIANO_C    = "sound/piano_C.mp3"
PIANO_C_SH = "sound/piano_C_sharp.mp3"
PIANO_D    = "sound/piano_D.mp3"
PIANO_D_SH = "sound/piano_D_sharp.mp3"
PIANO_E    = "sound/piano_E.mp3"
PIANO_F    = "sound/piano_F.mp3"
PIANO_F_SH = "sound/piano_F_sharp.mp3"
PIANO_G    = "sound/piano_G.mp3"
PIANO_G_SH = "sound/piano_G_sharp.mp3"
PIANO_M_C  = "sound/piano_middle_C.mp3"

#=================
#	Load
#=================
args = parser.parse_args()
#check args
if args.play is None or args.play[0] == "":
        print ERROR + "pyfpiano.py needs arguments , please use --help"
        exit(1)
music = "" #pyglet.media.load(SONG)
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pyfpiano.py | Naper')
pygame.mouse.set_visible(0)
pygame.mixer.init()
#pygame.mixer.music.load(SONG)
""" load background """
background = pygame.image.load('background.jpeg')
white = (255,64,64)
def play():
	""" playing note """
	pygame.mixer.music.unpause()

def onKeyPress(event):
    if event is None:
	pygame.mixer.music.pause()
    text.insert('end', 'Playing\n')
    pygame.mixer.music.unpause()
    #play()    

def pause():
	print "not playing"
	pygame.mixer.music.pause()


def binder():
	root = tk.Tk()
	root.geometry('300x200')
	text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
	text.pack()
	root.bind('<KeyPress>', onKeyPress, pause)
	print "test"
	root.mainloop()

def playNote(note):
	""" load and play note """
	pygame.mixer.music.load(note)
	pygame.mixer.music.play(-1,15)
	#time.sleep(0.5)

def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

def loadSf(type):
	""" load sf2 files """
	if type == "piano":
		return "instrument/Claudio_Piano.SF2"	
	if type == "guitar":
		return "instrument/Saber_5ths_and_3rds.SF2"
def header():
	""" header informations """
	print RED + "@ Pyfpiano.py" + DEFAULT + " version 0.1"
	print YELLOW + "@ author " + DEFAULT + "Naper"

#=================
#       Others
#=================
header()
type = 1
fluidsynth.init(loadSf(args.play[0]),"alsa")
if type == 2:
	pygame.mixer.music.play()
	pygame.mixer.music.pause()
	playstat = 0
if args.save:
	""" create new Notecontainer """
	nc = NoteContainer()
while True:
	#pygame.mixer.music.pause()
	screen.fill((white))
	screen.blit(background,(0,0))
	pygame.display.flip()
	if pygame.key.get_focused():
		playstat = 1
	else:
		playstat = 0
	events = pygame.event.get()
	event = pygame.event.poll()
	for event in events:
		note = ""
		note_type = 0
		if type == 1:
			""" play notes , A,B,C.. """
			if event.type == KEYDOWN:
				note = event.unicode
				if event.unicode == '0':
					note = "C#"
					note_type = 2
				if event.unicode == '1':
                                        note = "D#"
                                        note_type = 4
				if event.unicode == '2':
                                        note = "F#"
                                        note_type = 7
				if event.unicode == '3':
                                        note = "G#"
                                        note_type = 9
				if event.unicode == '4':
                                        note = "A#"
                                        note_type = 11
				if event.unicode == '5':
                                        note = "C#"
                                        note_type = 14
				if event.unicode == '6':
                                        note = "D#"
                                        note_type = 16
				if event.unicode == '7':
                                        note = "F#"
                                        note_type = 19
				if event.unicode == '8':
                                        note = "G#"
                                        note_type = 21
				if event.unicode == '9':
                                        note = "A#"
                                        note_type = 23
				if args.note:
                       			 note_type = int(args.note[0],10)
				if note != "" and  notes.is_valid_note(note) == False:
					print ERROR + "invalid note"
				else:
					if note == "":
						break;
					n = Note()
					if note == "k":
						n.set_Note('B')
					else:
						if note_type == 0:
							n.set_note(note)
						else:
							n.set_note(note,note_type)
					print ACTION + "playing Note : " + note
					fluidsynth.play_Note(n)
					#saving the play
					if args.save:
						nc.add_note(n)
			
				if event.unicode == 's':
					print ACTION + "saving file .."	
		else:
			if keyPressed(K_SPACE) == True or keyPressed(K_w) or keyPressed(K_a) or keyPressed(K_b) or keyPressed(K_c) or keyPressed(K_d) or keyPressed(K_e):
				play()
				print "playing"
			else:
				pause()
				print "not playing"
print ERROR + "closing .."
