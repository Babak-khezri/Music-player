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
from threading import *
play = time = file = first = volume = 0  # Global variables
timer = 100000
init(convert=True)
print(Style.DIM + Fore.LIGHTCYAN_EX +"Welcome to my music play :\nSelect your Directory")


def get_file():  # Get all mp3 players in input address
    sleep(0.5)
    while True:
        lst = glob(find())
        if len(lst) == 0:
            system('cls')
            print("Directory is empty")
            sleep(2)
        else:
            thread = Thread(target=next_music)
            thread.start()
            return lst


def find():  # Met the directory and make it findable
    tkin = Tk()
    tkin.withdraw()
    address = filedialog.askdirectory()
    address = address.split('\\')
    address = "\\".join(address) + "\\*.mp3"  # just find mp3 files
    return address


def player():  # Main player
    # start from the first file when app start
    global first
    if first == False:
        global play
        play = 0
        first = True
    while True:
        system('cls')
        global file
        global volume
        file = MediaPlayer(lst[play])
        volume = file.audio_get_volume()
        file.play()
        # get the time of file
        time_file = size()
        puse = True
        while True:
            show_name(time_file)
            event = getchar()
            if event == "p" or event == "g" or event == "n" or event == "c" or event == "e" or event == "P" or event == "G" or event == "N" or event == "C" or event == "E":
                play = change(event)
                break
            if event == 'w' or event == 's' or event == 'W' or event == 'S':
                volume = chVolume(event, volume)
                file.audio_set_volume(volume)
            if ord(event) == ord(" "):
                if puse == True:
                    file.pause()
                    puse = False
                    print("||poused")
                    continue
                if puse == False:
                    file.play()
                    puse = True


def change(event):  # Change mp3 file
    if event == 'c' or event == 'C':  # get random file
        file.stop()
        rand = randrange(0, len(lst))
        file.stop()
        return rand
    if event == 'n' or event == 'N':  # go to next file
        file.stop()
        if play == len(lst) - 1:
            file.stop()
            return 0
        else:
            file.stop()
            return play + 1
    if event == 'p' or event == 'P':  # go to pervios file
        file.stop()
        if play == 0:
            file.stop()
            return play
        else:
            file.stop()
            return play - 1
    if event == 'g' or event == 'G':  # go to input file
        while True:
            go = input("||goto : ")
            # check its acceptable input
            if not go.isdigit():
                continue
            if int(go) > 0 and int(go) <= len(lst):
                break
        file.stop()
        return (int(go) - 1)
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


def show_name(time_f):  # Print informations
    system('cls')
    print(Fore.LIGHTMAGENTA_EX +"||C = Change | N = Next | P = Previous | G = Goto | W = Vl+ | S = Vl- | E = Exit")
    print(Fore.RED + "||-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    name = lst[play].split("\\")
    name = name[len(name)-1].split('.')
    name.pop(len(name)-1)
    name = "".join(name)
    print(Fore.GREEN + "||File number : {}".format(play + 1).ljust(20), end=time_f.rjust(6))
    print("\n||File name : {}".format(name))
    print("||Vloume : {}".format(volume))


def size():  # Get time of any file
    global timer
    time = File(lst[play])
    time = int(time.info.length)  # get the files time in secound
    timer = int(time)
    minu = str(time // 60)  # get minute
    sec = str(time % 60)  # get second
    if len(sec) == 1:  # make it good style
        sec = '0' + sec
    return minu + ":" + sec


def next_music():  # When music over go to next
    global play
    global timer
    global file
    global volume
    while True:
        sleep(1)
        timer -= 1
        if timer == 0:
            timer -= 1
            play += 1
            file = MediaPlayer(lst[play])
            file.stop()
            timer = int(File(lst[play]).info.length)
            show_name(size())
            file.play()


lst = get_file()
player()
