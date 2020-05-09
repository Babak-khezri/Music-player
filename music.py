from glob import glob
from tkinter import *
from tkinter import filedialog
from random import randrange
from click import getchar
from os import system, _exit
from vlc import MediaPlayer
from mutagen import File
from time import sleep
from threading import Thread
timer = [1000,10]
event = None
box_info = ['0', '0', '0', '0']

def get_files():  # Get all mp3 players in input address
    destroy = True
    sleep(0.5)
    welcome_mas = Tk()
    Label(welcome_mas,text = "<<  welcome  >>\n    Please select ur directory    ",font = ("Times",25,'bold')).pack()
    while True:
        List_files = glob(Select_Dir())
        if destroy == True:
            welcome_mas.destroy()
            destroy = False
        tkin = Tk()
        tkin.title("warning")
        if len(List_files) == 0:
            Label(tkin,text = "Directory is empty ...",font = ("Times",25,'bold')).pack()
            sleep(1)
        else:
            Thread(target=next_music).start()
            Thread(target=add_event).start()
            return List_files


def Select_Dir():  # Met the directory and make it findable
    address = filedialog.askdirectory()
    address = address.split('\\')
    address = "\\".join(address) + "\\*.mp3"  # just find mp3 files
    return address


def graphic(): # Graphic by tkinter
    win = Tk()
    win.resizable(False,False)
    win.title('music player')
    app_icon = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ico.png')
    win.iconphoto(False , app_icon)
    win['background']='#000d33'
    Label(win, text="welcome to my music player", bg = '#000d33',fg= '#40ff00', font=("Times",24,'bold')).grid(row = 0,column=1,columnspan = 5)
    Label(win,text = '|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|',fg = '#ffcc00',font=("Helvetica",24,'bold'),bg = '#000d33').grid(row = 1,column=0,columnspan = 50)
    def Show_name():
        name_file.config(text=box_info[0],fg= '#ff0000', font=("Times",18,'bold'), bg = '#000d33')
        name_file.grid(row = 2,column=0,columnspan = 8)
        time_file.config(text=box_info[1],fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        time_file.grid(row = 3,column=1,columnspan = 5)
        volume.config(text=box_info[2], fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        volume.grid(row = 4,column=1,columnspan = 5)
        number.config(text=box_info[3], fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        number.grid(row = 5,column=1,columnspan = 5)
    def GUI_control(but):
        global event
        event = but
        sleep(0.1)
        Show_name()
    name_file = Label(win)
    time_file = Label(win)
    volume = Label(win)
    number = Label(win)
    photo_n = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\n.png') 
    photo_e = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\e.png') 
    photo_b = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\b.png') 
    photo_c = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\c.png') 
    photo_vu = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\vu.png') 
    photo_vd = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\vd.png') 
    photo_pu = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\pu.png') 
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_c , command=lambda: GUI_control('c')).grid(row = 7,column=0)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_b , command=lambda: GUI_control('b')).grid(row = 7,column=2)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_pu ,command=lambda: GUI_control(' ')).grid(row = 7,column=1)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_n , command=lambda: GUI_control('n')).grid(row = 7,column=3)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_vd, command=lambda: GUI_control('w')).grid(row = 7,column=4)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_vu, command=lambda: GUI_control('s')).grid(row = 7,column=5)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_e , command=lambda: GUI_control('e')).grid(row = 7,column=6)
    GUI_control('none')
    win.mainloop()


def player(play): # MAin player
    global box_info
    global event
    event = 'none'
    play = int(play)
    file = MediaPlayer(List_files[play])
    volume = file.audio_get_volume()
    file.play()
    time_file = size_file(play)
    name = List_files[play].split("\\")
    name = name[-1].split('.')
    name.pop(-1)
    name = ".".join(name)
    box_info = [name,play+1,time_file,volume]
    commands(file, play, volume, time_file)
    graphic()


def commands(file, play, volume, time_file): #Check commands
    pause = True
    while True:
        global event , box_info
        if event == "b" or event == "g" or event == "n" or event == "c" or event == "e" or event == "B" or event == "G" or event == "N" or event == "C" or event == "E":
            file.stop()
            change(event, play)
        elif event == 'w' or event == 's' or event == 'W' or event == 'S':
            volume = chVolume(event, volume)
            file.audio_set_volume(volume)
            event = 'none'
            box_info[3] = volume
        elif event == ' ':
            event = 'none'
            if pause == True:
                file.pause()
                pause = False
                continue
            else:
                file.play()
                pause = True
        else:
            continue


def change(event, play):  # Change mp3 file
    if event == 'c' or event == 'C':  # get random file
        rand = randrange(0, len(List_files))
        player(rand)
    if event == 'n' or event == 'N':  # go to next file
        if play == len(List_files) - 1:
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
            if int(go) > 0 and int(go) <= len(List_files):
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


def size_file(play):  # Get time of any file
    global timer
    time = File(List_files[play])
    time = int(time.info.length)  # get the files time in secound
    timer = [int(time), play]
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


def add_event(): # Add commands
    global event
    while True:
        event = getchar()
        if event == 'g':
            while True:
                if event == 'none':
                    break


def Open_GUI():  # If gui closed this open it again
    while True:
        graphic()

Thread(target = Open_GUI).start()
List_files = get_files()

player(0)
