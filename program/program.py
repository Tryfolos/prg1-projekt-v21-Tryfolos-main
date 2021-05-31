#Importing things.
import os
import sys
import time
import pygame

#Primitive Variables and lists.
running = 1 #1 means the program is running and 0 means the program will shut down.
current_status = "welcome" #This describes what part of the program will run in the big while loop below.
cm = "Press space to continue: " #This is used to tell the user to press spacebar in order to continue to the next part of the program. cm stands for "continue message"
input_space = 0 #1 means the spacebar has just been pressed.
thing = 1 #Used for all sorts of random things.
filename = "" #This is the name of the file to be read.
read_list = [[]] #2d list that contains data from file that is read.


#Initilizing pygame. The only part of pygame that will be used is keyboard input.
pygame.init()

#Creating a pygame window. This is neccesary for input to work. This will not be used for anything else.
window = pygame.display.set_mode((60, 50))


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
        if thing == 1:
            print("Welcome!")
            print(cm)
            thing = 0
        if input_space == 1:
            input_space = 0
            current_status = "program_purpose"
            thing = 1


    #Program_purpose. This comes after welcome message.
    if current_status == "program_purpose":
        if thing == 1:
            os.system("cls")
            print("This program will read a text file and create usernames and passwords based on the names you provided.")
            print(cm)
            thing = 0
        if input_space == 1:
            input_space = 0
            thing = 1
            current_status = "program_purpose_2"



    #Program_purpose_2. This comes after the first program_purpose message.
    if current_status == "program_purpose_2":
        if thing == 1:
            os.system("cls")
            print("The structure of the text file must be as follows:\n")
            print("- - - - - - - - - - - - - - - - - - - -")
            print("Firstname Lastname Birthyear")
            print("Johan Sundqvist 1999")
            print("Milan Sanchez 2007")
            print("Filip Hedman 2002")
            print("Sara Dahlberg 1985")
            print("Michael Smith 1960")
            print("Dorothy Miller 2010")
            print("Bella Nelson 2000")
            print("- - - - - - - - - - - - - - - - - - - -")
            print(cm)
            thing = 0
        if input_space == 1:
            input_space = 0
            thing = 1
            current_status = "enter_file_name"

    #Enter name of text file.
    if current_status == "enter_file_name":
        if thing == 1:
            os.system("cls")
            print("Enter the name of the text file you would like to use:")
            filename = input()
            thing = 0
        if input_space == 1:
            input_space = 0
            thing = 1
            current_status = "processing"

    #Reading the text file and making list of usernames and passwords.
    #Then creating new file and writing list of usernames and passowords to it.
    if current_status == "processing":
        os.system("cls")
        print("Processing...")
        file = open(filename, "r")
        file.read()







    #Updating the graphical pygame window. This is kind of useless but whatever.
    pygame.display.flip()


