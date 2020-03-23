from glob import glob
from tkinter import filedialog , Tk
from random import randrange
from click import getchar
from os import system
from getpass import getuser
from vlc import MediaPlayer
from colorama import init, Fore, Style
from mutagen import File
from time import sleep
init(convert=True)
print(Style.DIM + Fore.LIGHTCYAN_EX + "Welcome to my music play :\nSelect your Directory")
def get_file():# get all mp3 players in input address
    sleep(0.5)
    while True:
        lst = glob(find())
        if len(lst) == 0:
            system('cls')
            print("Directory is empty")
        else:
            return lst
def find(): # get the directory and make it findable 
    tkin = Tk()
    tkin.withdraw()
    address = filedialog.askdirectory()
    address = address.split('\\')
    address = "\\".join(address) + "\\*.mp3" # just find mp3 files
    return address
def player():#main player
    #start from the first file when app start 
    first = False
    if first == False:
        play = 0
        first = True
    while True: 
        #global file # make it global variable
        system('cls')
        file = MediaPlayer(lst[play])
        volume = file.audio_get_volume()
        file.play()
        #get the time of file
        time = timer(play)
        while True:
            show_name(play,volume,time)
            event = getchar()
            if event == "p" or event == "g" or event == "n" or event == "y" or event == "e" or event == "P" or event == "G" or event == "N" or event == "Y" or event == "E":
                play = change(event,file,play)
                break
            if event == 'w' or event == 's' or event == 'W' or event == 'S':
                volume = chvolume(event,file,volume)
                file.audio_set_volume(volume)
def change(event,file,play): # change mp3 file
    if event == 'y':#get random file
        rand = randrange(0,len(lst))
        file.stop()
        return rand
    if event == 'n':#go to next file
        file.stop()
        return play + 1
    if event == 'p':# go to pervios file
        file.stop()
        return play - 1
    if event == 'g':#go to input file
        while True:
            go = input("||goto : ")
            #check its acceptable input
            if not go.isdigit():
                continue
            if int(go) > 0 and int(go) <= len(lst):
                break
        file.stop()
        return (int(go) - 1)
    if event == 'e':
        exit(0)
def chvolume(event,file,vol):#change the volume
    if event == "w":
        if vol < 350:
            return vol + 5
        else:
            return vol
    if event == "s":
        if vol > 0:
            return vol - 5 
        else:
            return vol 
def show_name(play,volume,time):#print informations
    system('cls')
    print(Fore.BLUE + "||Y = Change | N = Next | P = Previous | G = Goto | W = Vl+ | S = Vl- | E = Exit")
    print(Fore.RED + "||-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    name = lst[play].split("\\")
    name = name[len(name)-1].split('.')
    name.pop(len(name)-1)
    name = "".join(name)
    print(Fore.GREEN + "||File number : {}".format(play + 1).ljust(20),end = time.rjust(6))
    print("\n||File name : {}".format(name))
    print("||Vloume : {}".format(volume))
def timer(play):#get time of any file
    time = File(lst[play])
    time = int(time.info.length)#get the files time in secound
    minu = str(time // 60)# get minute
    sec = str(time % 60)#get second
    if len(sec) == 1: # make it good style
        sec = '0' + sec
    return minu + ":" + sec
lst = get_file()
player()