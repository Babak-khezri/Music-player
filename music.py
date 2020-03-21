from glob import glob
from random import randrange
from click import getchar
from os import system
from getpass import getuser
from vlc import MediaPlayer
def find(): # find telegram Desktop directory
    user = getuser()
    address = "C:\\Users\\" + user + "\\Downloads\\Telegram Desktop\\*.mp3"
    return address
def player():
    while True:
        global p # make it global variable
        system('cls')
        # get random mp3 file
        rand = randrange(0,len(lst))
        show_name(rand)
        p = MediaPlayer(lst[rand])
        p.play()
        change()
def change(): # change mp3 file
    while True:
        print("want to change : ")
        change = getchar()
        if change == "y":
            p.stop()
            player()
def show_name(rand):
    name = lst[rand].split("\\")
    name = name[len(name)-1].split('.')
    name.pop(len(name)-1)
    #name.remove(".mp3")
    print("file number : {}".format(rand))
    print("file name : {}".format(name[len(name)-1]))

# get all mp3 players in telegram Desktop
lst = glob(find())
#start program
player()