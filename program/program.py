#Importing things.
import os
import sys
import time
import pygame

#Primitive Variables and lists.
running = 1 #1 means the program is running and 0 means the program will shut down.
current_status = "welcome" #This describes what part of the program will run in the big while loop below.
current_message = "" #This is used to store the strings usually printed to the screen.
cm = "Press space to continue: " #This is used to tell the user to press spacebar in order to continue to the next part of the program. cm stands for "continue message"
input_space = 0 #1 means the spacebar has just been pressed.
thing = 0 #Used for all sorts of random things.

#Initilizing pygame. The only part of pygame that will be used is keyboard input.
pygame.init()

#Creating a pygame window. This is neccesary for input to work. This will not be used for anything else.
window = pygame.display.set_mode((100, 100))


#Clearing the terminal since it looks like shit.
os.system("cls")


#Main program loop.
while running == 1:



    #Resetting input each tick of the frame.
    input_space = 0

    #Taking input from pygame.
    for f in pygame.event.get():
        if f.type == pygame.KEYDOWN:
            if f.key == pygame.K_SPACE:
                input_space = 1



    #This is the mandatory and unskippable welcomeing/startup sequence.
    if current_status == "welcome":
        current_message = "Welcome!"
        print(current_message)
        current_status = "space_1"


    #Press the spacebar to continue.
    if current_status == "space_1":
        if thing == 0:
            print(cm)
            thing = 1
        if input_space == 1:
            current_status = "program_purpose"
            thing = 0

    #Program_purpose. This comes after welcome message.
    if current_status == "program_purpose":
        running = 0

    #Updating the graphical pygame window. This is kind of useless but whatever.
    pygame.display.flip()


