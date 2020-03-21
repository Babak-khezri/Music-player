from glob import glob
from random import randrange
from click import getchar
from os import system
from getpass import getuser
from vlc import MediaPlayer
import colorama as co
def find(): # find telegram Desktop directory
    user = getuser()
    address = "C:\\Users\\" + user + "\\Downloads\\Telegram Desktop\\*.mp3"
    return address
def player():
    play = 0
    while True:
        #global file # make it global variable
        system('cls')
        # get random mp3 file
        show_name(play)
        file = MediaPlayer(lst[play])
        file.play()
        play = change(file,play)
        continue
def change(file,play): # change mp3 file
    while True:
        change = getchar()
        if change == "y":
            rand = randrange(0,len(lst))
            file.stop()
            return rand
        if change == "n":
            file.stop()
            return play + 1
        if change == "p":
            file.stop()
            return play - 1
        if change == "g":
            while True:
                change = int(input("goto : "))
                if change > 0 and change <= len(lst):
                    break
            file.stop()
            return change - 1
def show_name(play):
    print(co.Style.BRIGHT + co.Fore.BLUE + "y = change | n = next | p = Previous | g = goto")
    print(co.Fore.RED + "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    name = lst[play].split("\\")
    name = name[len(name)-1].split('.')
    name.pop(len(name)-1)
    #name.remove(".mp3")
    print(co.Fore.CYAN + "file number : {}".format(play + 1))
    print("file name : {}".format(name[(len(name) - 1)]))
# get all mp3 players in telegram Desktop
lst = glob(find())
#start program
player()