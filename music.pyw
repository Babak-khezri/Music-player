from tkinter import Tk, Button, Label, mainloop, PhotoImage, Entry, Menu # GUI
from glob import glob # Get files
from tkinter import filedialog
from random import randrange, choice
from os import _exit # Close program and all Threads
from vlc import MediaPlayer
from mutagen import File # Get time file
from time import sleep
from threading import Thread
from tkinter.messagebox import showerror 

timer = command = but = List_of_files = None # Global variables
info_box = ['','','',''] # Main list

def get_files(): # Get all mp3 players in input address
    colors = ['red','pink','purple','orange','yellow','green','blue','white','brown'] # Colors for warning show
    destroy = True # Destroyed first Gui page 1 time
    sleep(0.5)
    welcome_win = Tk() # First Gui window
    welcome_win.geometry('424x81+600+0')
    welcome_win.protocol("WM_DELETE_WINDOW",lambda:_exit(0)) # Turn off close window
    massage = Label(welcome_win, text = "<<  welcome  >>\n    Please select ur directory    ")
    massage.config(font = ("Times",25,'bold') ,fg = '#000066', bg='#ffb6ff')
    massage.grid(row = 0,column = 0)
    while True:
        List_of_files = glob(Select_Dir()) # Get the Directore mp3 files
        if destroy == True: 
            welcome_win.destroy()
            warining_win = Tk() # Make second Gui window that if dirctory be ampty will come up
            warining_win.protocol("WM_DELETE_WINDOW",lambda:_exit(0)) # Turn off close window
            destroy = False
        if len(List_of_files) == 0: # Directory is empty
            warining_win.title("warning")
            warning = Label(warining_win,text = "Directory is empty ...")
            warning.config(font = ("Times",25,'bold'), fg = choice(colors), bg = '#00004d')
            warning.grid(row = 0,column = 0)
            sleep(1)
        else: # Directory is not empty
            warining_win.destroy() # Destroyed second Gui window
            Thread(target = graphic).start() # Open main Gui
            Thread(target = next_music).start() # Open timer for mp3 files
            return List_of_files


def Select_Dir(): # Met the directory and make it findable
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
    Label(win, text="◤        🎵 welcome to my music player 🎵        ◥",fg = '#40ff00', bg = '#000d33', font = ("Times",24,'bold')).grid(row = 0,column=0,columnspan = 8)
    Label(win,text = '|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|',fg = '#ffcc00',bg = '#000d33',font = ("Helvetica",24,'bold')).grid(row = 1,column=0,columnspan = 50)
    def show_info(): # show the informations
        name_file.config(text=info_box[0], fg= '#ff0000', font = ("Times",18,'bold'), bg = '#000d33')
        name_file.grid(row = 2, column = 0, columnspan = 8)
        time_file.config(text=info_box[1], fg= '#ff0000', font = ("Times",20,'bold'), bg = '#000d33')
        time_file.grid(row = 3, column = 1, columnspan = 5)
        volume.config(text=info_box[2], fg= '#ff0000', font = ("Times",20,'bold'), bg = '#000d33')
        volume.grid(row = 4, column = 1, columnspan = 5)
        number.config(text=info_box[3], fg= '#ff0000', font = ("Times",20,'bold'), bg = '#000d33')
        number.grid(row = 5, column = 1, columnspan = 5)
    def GUI_control(but): # Make commands
        global command
        command = but
        sleep(0.1)
        show_info()
    def Right_click(event): # Show menu
        def menu_commands(get_command):
            global command
            command = get_command
            change_info()
        menu_bar = Menu(win,tearoff=0) # Make menu bar
        menu_bar.add_command(label='restart',command=Change_Directory) # Change the Dirctory and get another files
        menu_bar.add_command(label='change',command=lambda:menu_commands('cha'))
        menu_bar.add_command(label='next',command=lambda:menu_commands('nex'))
        menu_bar.add_command(label='back',command=lambda:menu_commands('bac'))
        menu_bar.add_command(label='GoTo',command=lambda:menu_commands('GoTo'))
        menu_bar.add_command(label='exit',command=lambda:_exit(0)) # close the program
        menu_bar.tk_popup(event.x_root,event.y_root) # Create menu in mouse place
    name_file = Label(win)
    time_file = Label(win)
    volume = Label(win)
    number = Label(win)
    photo_nex = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ne.png') 
    photo_exi = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ex.png') 
    photo_bac = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ba.png') 
    photo_cha = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ch.png') 
    photo_vou = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\vu.png') 
    photo_vod = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\vd.png') 
    photo_pua = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\pu.png') 
    Button(win,height=55, width=60, bd=16,bg='#000099', image=photo_cha, command=lambda: GUI_control('cha')).grid(row = 7,column=0)
    Button(win,height=55, width=60, bd=16,bg='#000099', image=photo_bac, command=lambda: GUI_control('bac')).grid(row = 7,column=2)
    Button(win,height=55, width=60, bd=16,bg='#000099', image=photo_pua, command=lambda: GUI_control('pau')).grid(row = 7,column=1)
    Button(win,height=55, width=60, bd=16,bg='#000099', image=photo_nex, command=lambda: GUI_control('nex')).grid(row = 7,column=3)
    Button(win,height=55, width=60, bd=16,bg='#000099', image=photo_vod, command=lambda: GUI_control('vl+')).grid(row = 7,column=4)
    Button(win,height=55, width=60, bd=16,bg='#000099', image=photo_vou, command=lambda: GUI_control('vl-')).grid(row = 7,column=5)
    Button(win,height=55, width=60, bd=16,bg='#000099', image=photo_exi, command=lambda: GUI_control('exi')).grid(row = 7,column=6)
    sleep(0.3)
    GUI_control('none')
    global but
    but = Button(win, command = lambda: GUI_control('none')) # The unshow but for show name when program go to next music by timer
    but.invoke() # Put the button automatically
    win.bind('<G>', Pressing_G) # If G presses go to this function
    win.bind('<g>', Pressing_G) # If G presses go to this function
    win.bind('<Button-3>',Right_click) # With right click menu show
    win.protocol("WM_DELETE_WINDOW",lambda:0) # Turn off close window
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
    name = ".".join(name)
    if len(name) > 45:
        return name[0:45] + " ..."
    else:
        return name    


def commands(file, play, volume, time_file): #Check commands
    global command , info_box
    pause = True # Pause and unpa
    while True:
        if command == 'bac' or command == 'nex' or command == 'cha' or command == 'exi':
            file.stop()
            change(command, play)
        elif command == 'GoTo':
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


def GoTo(file): # Make window to Enter the file number
    def accept(event): # Go to file
        play = Enter.get()
        if play.isdigit():
            play = int(play) - 1
            if play >= 0 and play < len(List_of_files):
                file.stop()
                Go_win.destroy()
                Thread(target=change_info).start()
                player(play)
            else:
                Go_win.destroy()
                showerror("error",'Can\'t find file')
        else:
            Go_win.destroy()
            showerror("error",'Wrong input')
    def Cancel(): # continue playing file
        global command
        command = 'none'
        Go_win.destroy() # Close window
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
        randome = randrange(0, len(List_of_files))
        player(randome)
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


def chVolume(command, volume): # Change the volume
    if command == 'vl+':
        if volume < 250:
            return volume + 5
        else:
            return volume
    if command == 'vl-':
        if volume > 0:
            return volume - 5
        else:
            return volume


def size_file(play): # Get time of any file
    global timer
    time = File(List_of_files[play])
    time = int(time.info.length)  # Get the files time in secound
    timer = [int(time), play] # Send it for timer function
    minute = str(time // 60)  # get minute
    second = str(time % 60)  # get second
    if len(second) == 1:  # make it final style
        second = '0' + second
    return ("⌛ " + minute + ":" + second + " ⌛")


def next_music(): # When music over go to next
    global command
    while True: # A timer
        sleep(1)
        timer[0] -= 1
        if timer[0] == 0:
            timer[0] -= 1
            command = 'nex'
            Thread(target=change_info).start()


def Pressing_G(event): # When press G this function go to Goto window
    global command
    command = 'GoTo'


def change_info(): # When use goto or music end change the informations
    sleep(0.2)
    but.invoke()


def Change_Directory(): # Change Direcotry and get new files
    global List_of_files
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
            destroy = False
        if len(List_of_files) != 0: # Directory is NOT empty
            break


def start(): # Start the program
    global List_of_files
    List_of_files = get_files()
    player(0)


start()