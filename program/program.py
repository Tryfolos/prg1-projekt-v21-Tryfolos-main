#Importing things.
import os
import keyboard
import copy
import random


#Primitive Variables and lists.
running = 1 #1 means the program is running and 0 means the program will shut down.
current_status = "welcome" #This describes what part of the program will run in the big while loop below.
cm = "Press space to continue: " #This is used to tell the user to press spacebar in order to continue to the next part of the program. cm stands for "continue message"
input_space = 0 #1 means the spacebar has just been pressed.
thing = 1 #Used for all sorts of random things.
filename = "" #This is the name of the file to be read.
read_list = [] #list that contains data from file that is read.
temp_list = [] #List used temporarily to generate usernames and passwords. It will contain firstnames, lastnames, and birthyears as three seperate elements in their own lists.
space = 0 #If this is 0. You can't enter another space.

#Adding many lists into temp_list.
for f in range(0, 200):
    temp_list.append([])

username_list = [] #list that contains the final generated usernames.
password_list = [] #List that contains the final generated passwords.

#Clearing the terminal since it looks like shit.
os.system("cls")


#Main program loop.
while running == 1:



    #Resetting input each tick of the frame.
    input_space = 0



    #Taking input from keyboard.
    if keyboard.is_pressed("space"):
        if space == 1:
            input_space = 1
            space = 0

    #Reclaiming the ability to input space as soon as the space key is stopped being pressed.
    if not keyboard.is_pressed("space"):
        space = 1




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
            print("")
            print(cm)
            thing = 0
        if input_space == 1:
            input_space = 0
            thing = 1
            current_status = "enter_file_name"


    #Enter name of text file.
    if current_status == "enter_file_name":
        if thing == 1:
            for f in range(0, 50): #This for loop is here to put a bunch of backspaces into the input functions buffer in order to make sure it is empty.
                keyboard.press_and_release("backspace")
            os.system("cls")
            print("Enter the name of the text file you would like to use:")
            filename = input("")
            print(cm)
            thing = 0
        if input_space == 1:
            input_space = 0
            thing = 1
            current_status = "processing"


    #Reading the text file and making list of usernames and passwords.
    #Then creating new file and writing list of usernames and passwords to it.
    if current_status == "processing":
        os.system("cls")
        print("Usernames and passwords has been generated!\n")
        print("")
        print("The new usernames and passwords will be saved in a text file inside the current working directory.")
        print("")

        #Creating list of usernames and passwords.
        #Creating file object from file and reading it. The read data is put into a list.
        file = open(filename, "r")
        read_list = file.readlines()
        file.close()

        #Iterating read_list and generating a new 2d array containing firstnames lastnames and birthyears as seperate elements.
        numb = 0
        for f in read_list:
            temp_list[numb] = f.split(" ")
            numb += 1

        #Removing unused/empty elements from temp_list.
        temp_list = filter(None, temp_list)

        #Making a deep copy of the temp list because for some reason it fixes a problem. This is the result of shotgun debugging. Don not ask.
        temp_list_2 = copy.deepcopy(temp_list)


        #Using temp_list to generate usernames and putting them in username_list.
        for f in temp_list:
            temp_string = copy.deepcopy(f[0]) + "_" + copy.deepcopy(f[1]) + str(random.randint(10, 99))
            username_list.append(temp_string)



        #Using temp_list to generate passwords and putting them in password_list.
        for f in temp_list_2:
            temp_string = copy.deepcopy(f[0][0:2]) + copy.deepcopy(f[1][0:2]) + random.choice(["#", "%", "&", "@", "!", "?"]) + copy.deepcopy(f[2])
            password_list.append(temp_string)



        #Printing list of usernames and passwords.
        print("- - - - - - - - - - - - - - - - - - - -")
        print("-Username- -Password-")
        print("")
        #Printing full list of usernames and passwords in for loop.
        for f in range(0, len(username_list)):
            print(username_list[f][0:-1] + " " + password_list[f][0:-1])
        print("- - - - - - - - - - - - - - - - - - - -")


        #Saving username and password lists in text file.
        file = open(filename[0:-4]+"_final.txt", "w+")

        for f in range(0, len(username_list)):
            file.write(username_list[f])
            file.write(" ")
            file.write(password_list[f])

        file.close()
        current_status = "final"
        thing = 1


        #Ending the program.
    if current_status == "final":
        if thing == 1:
            print("")
            print("Press space to exit:")
            thing = 0
            input_space = 0
        if input_space == 1:
            running = 0








