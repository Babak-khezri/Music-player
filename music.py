from glob import glob
from tkinter import Tk, Button, Label, mainloop, PhotoImage
from tkinter import filedialog
from random import randrange, choice
from click import getchar
from os import system, _exit
from vlc import MediaPlayer
from mutagen import File
from time import sleep
from threading import Thread
from tqdm import tqdm


timer = event = but = None
box_info = ['','','','']


def get_files():  # Get all mp3 players in input address
    colors = ['red','pink','purple','orange','yellow','green','blue','white','brown'] # Colors for warning show
    destroy = True # Destroyed first Gui page 1 time
    sleep(0.5)
    welcome_mas = Tk() # First Gui window
    massage = Label(welcome_mas,text = "<<  welcome  >>\n    Please select ur directory    ")
    massage.config(font = ("Times",25,'bold') , fg = '#000066',bg='#ffb6ff')
    massage.grid(row=0,column=0)
    while True:
        List_files = glob(Select_Dir()) # Get the Directore mp3 files
        if destroy == True: 
            welcome_mas.destroy()
            warining_page = Tk() # Make second Gui window that if dirctory be ampty will come up
            destroy = False
        if len(List_files) == 0: # Directory is empty
            warining_page.title("warning")
            massage = Label(warining_page,text = "Directory is empty ...")
            massage.config(font = ("Times",25,'bold'), fg = choice(colors), bg = '#00004d')
            massage.grid(row=0,column=0)
            sleep(1)
        else: # Directory is not empty
            warining_page.destroy() # Destroyed second Gui window
            Thread(target = Open_GUI).start() # Open main Gui
            Thread(target=next_music).start() # Open timer for mp3 files
            return List_files


def Select_Dir():  # Met the directory and make it findable
    address = filedialog.askdirectory()
    address +=  "\\*.mp3"  # just find mp3 files
    return address


def graphic(): # Graphic by tkinter
    win = Tk()  
    win.resizable(False,False) # Lock change size
    win.title('music player')
    app_icon = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ico.png')
    win.iconphoto(False , app_icon) # Change icon
    win['background']='#000d33' # Change main background
    Label(win, text="welcome to my music player", bg = '#000d33',fg= '#40ff00', font=("Times",24,'bold')).grid(row = 0,column=1,columnspan = 5)
    Label(win,text = '|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|',fg = '#ffcc00',font=("Helvetica",24,'bold'),bg = '#000d33').grid(row = 1,column=0,columnspan = 50)
    def show_info(): # show the informations
        name_file.config(text=box_info[0],fg= '#ff0000', font=("Times",18,'bold'), bg = '#000d33')
        name_file.grid(row = 2,column=0,columnspan = 8)
        time_file.config(text=box_info[1],fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        time_file.grid(row = 3,column=1,columnspan = 5)
        volume.config(text=box_info[2], fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        volume.grid(row = 4,column=1,columnspan = 5)
        number.config(text=box_info[3], fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        number.grid(row = 5,column=1,columnspan = 5)
    def GUI_control(but): # Make commands
        global event
        event = but
        sleep(0.1)
        show_info()
    name_file = Label(win)
    time_file = Label(win)
    volume = Label(win)
    number = Label(win)
    photo_ne = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ne.png') 
    photo_ex = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ex.png') 
    photo_ba = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ba.png') 
    photo_ch = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ch.png') 
    photo_vu = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\vu.png') 
    photo_vd = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\vd.png') 
    photo_pu = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\pu.png') 
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_ch, command=lambda: GUI_control('cha')).grid(row = 7,column=0)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_ba, command=lambda: GUI_control('bac')).grid(row = 7,column=2)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_pu, command=lambda: GUI_control('pau')).grid(row = 7,column=1)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_ne, command=lambda: GUI_control('nex')).grid(row = 7,column=3)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_vd, command=lambda: GUI_control('vl+')).grid(row = 7,column=4)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_vu, command=lambda: GUI_control('vl-')).grid(row = 7,column=5)
    Button(win,height = 55, width = 60, bd=16,bg='#000099',image = photo_ex, command=lambda: GUI_control('exi')).grid(row = 7,column=6)
    GUI_control('none')
    global but
    but = Button(win,command=lambda: GUI_control('none')) # The unshow but for show name when program go to next music by timer
    but.invoke() # Put the button automatically
    win.mainloop()


def player(play): # MAin player
    global box_info, event
    event = 'none' # Avoid running a command twice
    file = MediaPlayer(List_files[play])
    file.play()
    volume = file.audio_get_volume()
    time_file = size_file(play)
    name = file_name(play)
    box_info = [name,play+1,time_file,volume] # Add informations to the list for showing
    commands(file, play, volume, time_file)


def file_name(play): # Get the name of the file
    name = List_files[play].split("\\")
    name = name[-1].split('.')
    name.pop(-1)
    return ".".join(name)    


def commands(file, play, volume, time_file): #Check commands
    global event , box_info
    pause = True # Pause and unpa
    while True:
        global event , box_info
        if event == "bac" or event == "g" or event == "nex" or event == "cha" or event == "exi":
            file.stop()
            change(event, play)
        elif event == 'vl+' or event == 'vl-':
            volume = chVolume(event, volume)
            file.audio_set_volume(volume)
            event = 'none'
            box_info[3] = volume
        elif event == 'pau':
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
    if event == 'cha':  # get random file
        rand = randrange(0, len(List_files))
        player(rand)
    if event == 'nex':  # go to next file
        if play == len(List_files) - 1:
            player(0)
        else:
            player(play + 1)
    if event == 'bac':  # go to pervios file
        if play == 0:
            player(play)
        else:
            player(play - 1)
    if event == 'exi':
        _exit(0)


def chVolume(event, vol):  # Change the volume
    if event == 'vl+':
        if vol < 250:
            return vol + 5
        else:
            return vol
    if event == 'vl-':
        if vol > 0:
            return vol - 5
        else:
            return vol


def size_file(play):  # Get time of any file
    global timer
    time = File(List_files[play])
    time = int(time.info.length)  # Get the files time in secound
    timer = [int(time), play] # Send it for timer function
    minu = str(time // 60)  # get minute
    sec = str(time % 60)  # get second
    if len(sec) == 1:  # make it final style
        sec = '0' + sec
    return ("< " + minu + ":" + sec + " >")


def next_music():  # When music over go to next
    global event, but
    while True: # A timer
        sleep(1)
        timer[0] -= 1
        if timer[0] == -1:
            timer[0] -= 1
            event = 'nex'
            sleep(0.1) # Get time to informations change
            but.invoke() # Push to extra button for showing informations


def Open_GUI():  # If GUI closed this open it again
    while True:
        graphic()


List_files = get_files()
player(0)