from glob import glob
from tkinter import filedialog, Tk
from random import randrange
from click import getchar
from os import system, _exit
from getpass import getuser
from vlc import MediaPlayer
from colorama import init, Fore, Style
from mutagen import File
from time import sleep
from threading import Thread
timer = None
system('mode con:cols=77 lines=15')
init(convert=True)
print(Style.DIM + Fore.LIGHTCYAN_EX +"Welcome to my music play :\nSelect your Directory")
event = 'none'

def get_file():  # Get all mp3 players in input address
    sleep(0.5)
    while True:
        lst = glob(find())
        if len(lst) == 0:
            system('cls')
            print("Directory is empty")
            sleep(2)
        else:
            Thread(target=next_music).start()
            Thread(target=add_event).start()
            return lst


def find():  # Met the directory and make it findable
    tkin = Tk()
    tkin.withdraw()
    address = filedialog.askdirectory()
    address = address.split('\\')
    address = "\\".join(address) + "\\*.mp3"  # just find mp3 files
    return address


def player(play):
    global event
    event = 'none'
    play = int(play)
    file = MediaPlayer(lst[play])
    volume = file.audio_get_volume()
    file.play()
    time_file = size_file(play)
    puse = True
    show_name(time_file,play,volume)
    events(file,play,volume,time_file)


def events(file,play,volume,time_file):
    while True:
        global event
        if event == "b" or event == "g" or event == "n" or event == "c" or event == "e" or event == "B" or event == "G" or event == "N" or event == "C" or event == "E":
            file.stop()
            change(event,play)
        elif event == 'w' or event == 's' or event == 'W' or event == 'S':
            volume = chVolume(event, volume)
            file.audio_set_volume(volume)
            event = 'none'
            show_name(time_file,play,volume)
        else:
            continue


def change(event,play):  # Change mp3 file
    if event == 'c' or event == 'C':  # get random file
        rand = randrange(0, len(lst))
        player(rand)
    if event == 'n' or event == 'N':  # go to next file
        if play == len(lst) - 1:
            player(0)
        else:
            player(play + 1)
    if event == 'b' or event == 'B':  # go to pervios file
        if play == 0:
            player(play)
        else:
            player(play - 1)
    if event == 'g' or event == 'G':  # go to input file
        while True:
            go = input("||goto : ")
            # check its acceptable input
            if not go.isdigit():
                continue
            if int(go) > 0 and int(go) <= len(lst):
                break
        player(int(go) - 1)
    if event == 'e' or event == 'E':
        _exit(0)


def chVolume(event, vol):  # Change the volume
    if event == "w" or event == 'W':
        if vol < 350:
            return vol + 5
        else:
            return vol
    if event == "s" or event == 'S':
        if vol > 0:
            return vol - 5
        else:
            return vol


def show_name(time_file,play,volume):  # Print informations
    #system('cls')
    print(Fore.LIGHTMAGENTA_EX +"||C = Change | N = Next | B = Back | G = Goto | W = Vl+ | S = Vl- | E = Exit")
    print(Fore.RED + "||-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    name = lst[play].split("\\")
    name = name[len(name)-1].split('.')
    name.pop(len(name)-1)
    name = "".join(name)
    print(Fore.GREEN + "||File number : {}\t".format(play + 1).ljust(20) +  time_file, end = "")
    print("\n||File name : {}".format(name))
    print("||Vloume : {}".format(volume))


def size_file(play):  # Get time of any file
    global timer
    time = File(lst[play])
    time = int(time.info.length)  # get the files time in secound
    timer = [int(time),play]
    minu = str(time // 60)  # get minute
    sec = str(time % 60)  # get second
    if len(sec) == 1:  # make it good style
        sec = '0' + sec
    return "< " + minu + ":" + sec + " >"


def next_music():  # When music over go to next
    global event
    while True:
        sleep(1)
        timer[0] -= 1
        if timer[0] == -1:
            timer[0] -= 1
            event = 'n'


def add_event():
    global event
    while True:
        event = getchar()
        if event == 'g':
            while True:
                if event == 'none':
                    break

lst = get_file()
player(0)