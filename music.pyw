from glob import glob
from tkinter import Tk, Button, Label, mainloop, PhotoImage, Entry
from tkinter import filedialog
from random import randrange, choice
from os import _exit
from vlc import MediaPlayer
from mutagen import File
from time import sleep
from threading import Thread
timer = command = but = None
info_box = ['','','','']


def get_files():  # Get all mp3 players in input address
    colors = ['red','pink','purple','orange','yellow','green','blue','white','brown'] # Colors for warning show
    destroy = True # Destroyed first Gui page 1 time
    sleep(0.5)
    welcome_win = Tk() # First Gui window
    welcome_win.geometry('424x81+600+0')
    massage = Label(welcome_win, text = "<<  welcome  >>\n    Please select ur directory    ")
    massage.config(font = ("Times",25,'bold') ,fg = '#000066', bg='#ffb6ff')
    massage.grid(row = 0,column = 0)
    while True:
        List_of_files = glob(Select_Dir()) # Get the Directore mp3 files
        if destroy == True: 
            welcome_win.destroy()
            warining_win = Tk() # Make second Gui window that if dirctory be ampty will come up
            destroy = False
        if len(List_of_files) == 0: # Directory is empty
            warining_win.title("warning")
            warning = Label(warining_win,text = "Directory is empty ...")
            warning.config(font = ("Times",25,'bold'), fg = choice(colors), bg = '#00004d')
            warning.grid(row = 0,column = 0)
            sleep(1)
        else: # Directory is not empty
            warining_win.destroy() # Destroyed second Gui window
            Thread(target = Open_GUI).start() # Open main Gui
            Thread(target = next_music).start() # Open timer for mp3 files
            return List_of_files


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
    Label(win, text="🎵 welcome to my music player 🎵", bg = '#000d33',fg= '#40ff00', font=("Times",24,'bold')).grid(row = 0,column=1,columnspan = 5)
    Label(win,text = '|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|',fg = '#ffcc00',font=("Helvetica",24,'bold'),bg = '#000d33').grid(row = 1,column=0,columnspan = 50)
    def show_info(): # show the informations
        name_file.config(text=info_box[0], fg= '#ff0000', font=("Times",18,'bold'), bg = '#000d33')
        name_file.grid(row = 2, column = 0, columnspan = 8)
        time_file.config(text=info_box[1], fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        time_file.grid(row = 3, column = 1, columnspan = 5)
        volume.config(text=info_box[2], fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        volume.grid(row = 4, column = 1, columnspan = 5)
        number.config(text=info_box[3], fg= '#ff0000', font=("Times",20,'bold'), bg = '#000d33')
        number.grid(row = 5, column = 1, columnspan = 5)
    def GUI_control(but): # Make commands
        global command
        command = but
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
    Button(win,height = 55, width = 60, bd=16,bg='#000099', image = photo_ch, command=lambda: GUI_control('cha')).grid(row = 7,column=0)
    Button(win,height = 55, width = 60, bd=16,bg='#000099', image = photo_ba, command=lambda: GUI_control('bac')).grid(row = 7,column=2)
    Button(win,height = 55, width = 60, bd=16,bg='#000099', image = photo_pu, command=lambda: GUI_control('pau')).grid(row = 7,column=1)
    Button(win,height = 55, width = 60, bd=16,bg='#000099', image = photo_ne, command=lambda: GUI_control('nex')).grid(row = 7,column=3)
    Button(win,height = 55, width = 60, bd=16,bg='#000099', image = photo_vd, command=lambda: GUI_control('vl+')).grid(row = 7,column=4)
    Button(win,height = 55, width = 60, bd=16,bg='#000099', image = photo_vu, command=lambda: GUI_control('vl-')).grid(row = 7,column=5)
    Button(win,height = 55, width = 60, bd=16,bg='#000099', image = photo_ex, command=lambda: GUI_control('exi')).grid(row = 7,column=6)
    GUI_control('none')
    sleep(0.2)
    global but
    but = Button(win, command=lambda: GUI_control('none')) # The unshow but for show name when program go to next music by timer
    but.invoke() # Put the button automatically
    win.bind('<G>', Pressing_G) # IF G presses go to this function
    win.bind('<g>', Pressing_G) # IF G presses go to this function
    win.mainloop()


def player(play): # MAin player
    global info_box, command
    command = 'none' # Avoid running a command twice
    file = MediaPlayer(List_of_files[play])
    file.play()
    volume = file.audio_get_volume()
    time_file = size_file(play)
    name = file_name(play)
    info_box = [name, play+1, time_file, volume] # Add informations to the list for showing
    commands(file, play, volume, time_file)
    

def file_name(play): # Get the name of the file
    name = List_of_files[play].split("\\")
    name = name[-1].split('.')
    name.pop(-1)
    return ".".join(name)    


def commands(file, play, volume, time_file): #Check commands
    global command , info_box
    pause = True # Pause and unpa
    while True:
        if command in ["bac","nex","cha","exi"]:
            file.stop()
            change(command, play)
            command = 'pau'
        if command == 'GoTo':
            GoTo(file)       
        elif command == 'vl+' or command == 'vl-':
            volume = chVolume(command, volume)
            file.audio_set_volume(volume)
            command = 'none'
            info_box[3] = volume
        elif command == 'pau':
            command = 'none'
            if pause == True:
                file.pause()
                pause = False
                continue
            else:
                file.play()
                pause = True
        else:
            continue


def GoTo(file):
    def accept(event):
        file.stop()
        play = int(Enter.get()) - 1
        Go_win.destroy()
        Thread(target=change_info).start()
        player(play)
    def Cancel():
        global command
        command = 'none'
        Go_win.destroy()
    Go_win = Tk()
    Go_win.resizable(False,False)
    Go_win.title('GO_TO')
    Go_win['background'] = 'pink'
    Label(Go_win,text='Enter number : ',font=("Times",15,'bold'),bg='pink').grid(row = 0,column=0)
    Label(Go_win,bg='pink',text='-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-',font=("Times",7,'bold')).grid(row = 1,column=0,columnspan=3)
    Label(Go_win,text='🎼',font=("Times",30,'bold'),bg='pink').grid(row = 2,column=0)
    Enter = Entry(Go_win,font=("Times",15,'bold'))
    Enter.grid(row = 0,column=1,columnspan=2)
    Button(Go_win,bd=6,text='go',command = lambda:accept('none'),font=("Times",13,'bold')).grid(row = 2,column=1)
    Button(Go_win,bd=6,text = 'cancel',command=Cancel,font=("Times",13,'bold')).grid(row = 2,column=2)
    
    Go_win.bind('<Return>', accept)
    Go_win.mainloop()


def change(command, play):  # Change mp3 file
    if command == 'cha':  # get random file
        rand = randrange(0, len(List_of_files))
        player(rand)
    if command == 'nex':  # go to next file
        if play == len(List_of_files) - 1:
            player(0)
        else:
            player(play + 1)
    if command == 'bac':  # go to pervios file
        if play == 0:
            player(play)
        else:
            player(play - 1)
    if command == 'exi':
        _exit(0)


def chVolume(command, vol):  # Change the volume
    if command == 'vl+':
        if vol < 250:
            return vol + 5
        else:
            return vol
    if command == 'vl-':
        if vol > 0:
            return vol - 5
        else:
            return vol


def size_file(play):  # Get time of any file
    global timer
    time = File(List_of_files[play])
    time = int(time.info.length)  # Get the files time in secound
    timer = [int(time), play] # Send it for timer function
    minu = str(time // 60)  # get minute
    sec = str(time % 60)  # get second
    if len(sec) == 1:  # make it final style
        sec = '0' + sec
    return ("⌛ " + minu + ":" + sec + " ⌛")


def next_music():  # When music over go to next
    global command
    while True: # A timer
        sleep(1)
        timer[0] -= 1
        if timer[0] == 0:
            timer[0] -= 1
            command = 'nex'
            change_info()
    

def Open_GUI():  # If GUI closed this open it again
    while True:
        graphic()


def Pressing_G(event):
    global command
    command = 'GoTo'


def change_info():
    sleep(0.1)
    but.invoke()


List_of_files = get_files()
player(0)