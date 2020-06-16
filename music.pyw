from tkinter import Tk, Button, Label, mainloop, PhotoImage, Entry, Menu # GUI
from glob import glob # Get files
from tkinter import filedialog
from random import randrange, choice
from os import _exit # Close program and all Threads
from vlc import MediaPlayer
from mutagen import File # Get time file
from time import sleep
from threading import Thread
from tkinter.messagebox import showerror # Show Error for goto

Timer = command = Indicator_Button = List_of_files = None # Global variables
Info_Box = ['','','',''] # Main information list

def Get_Files(): # Get all mp3 players in selected directory
    Colors = ['red','pink','purple','orange','yellow','green','blue','white','brown'] # Colors for warning show
    Destroy = True # Destroyed first Gui page 1 time
    sleep(0.5)
    welcome_win = Tk() # First Gui window
    welcome_win.geometry('424x81+600+0')
    welcome_win.protocol("WM_DELETE_WINDOW",lambda:_exit(0)) # Turn off close window
    Massage = Label(welcome_win, text = "<<  welcome  >>\n    Please select ur directory    ")
    Massage.config(font = ("Times",25,'bold') ,fg = '#000066', bg='#ffb6ff')
    Massage.grid(row = 0,column = 0)
    while True:
        List_of_files = glob(Select_Dirctory()) # Get the Directore mp3 files
        if Destroy == True: 
            welcome_win.destroy()
            warining_win = Tk() # Make second Gui window that if dirctory be ampty will come up
            warining_win.protocol("WM_DELETE_WINDOW",lambda:_exit(0)) # Turn off close window
            Destroy = False
        if len(List_of_files) == 0: # Directory is empty
            warining_win.title("warning")
            warning = Label(warining_win,text = "Directory is empty ...")
            warning.config(font = ("Times",25,'bold'), fg = choice(Colors), bg = '#00004d')
            warning.grid(row = 0,column = 0)
            sleep(1)
        else: # Directory is not empty
            warining_win.destroy() # Destroyed second Gui window
            Thread(target = Graphics).start() # Open main Gui
            Thread(target = File_Timer).start() # Open timer for mp3 files
            return List_of_files


def Select_Dirctory(): # Get the directory
    Address = filedialog.askdirectory()
    Address +=  "\\*.mp3"  # just find mp3 files
    return Address


def Graphics(): # Graphic by using tkinter
    win = Tk()    
    def Gui_sitting(): # GUI main sittings
        win.resizable(False,False) # Lock change size
        win.geometry("655x355")
        win.title('music player')
        App_Icon = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ico.png')
        win.iconphoto(False , App_Icon) # Change icon
        win['background']='#000d33' # Change main background
        global Indicator_Button, command
        Indicator_Button = Button(win, command = lambda: GUI_control('none')) # The unshow but for show indormations when program go to next music by timer
        Label(win, text="◤ 🎵 Welcome to my music player 🎵 ◥",fg = '#40ff00', bg = '#000d33', font = ("Comic sans MS",24,'bold')).grid(row = 0,column=0,columnspan = 8)
        Label(win,text = '|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|',fg = '#ffcc00',bg = '#000d33',font = ("Comic sans MS",24,'bold')).grid(row = 1,column=0,columnspan = 50)
        win.bind('<G>',Keabord_Controll) # If G presses go to this function
        win.bind('<g>',Keabord_Controll) # If G presses go to this function
        win.bind('<c>',Keabord_Controll)
        win.bind('<C>',Keabord_Controll)
        win.bind('<b>',Keabord_Controll)
        win.bind('<B>',Keabord_Controll)
        win.bind('<n>',Keabord_Controll)
        win.bind('<N>',Keabord_Controll)
        win.bind('<s>',Keabord_Controll)
        win.bind('<S>',Keabord_Controll)
        win.protocol("WM_DELETE_WINDOW",lambda:0) # Turn off close window
        Top_Menu()
    def show_info(): # show the informations
        name_file.config(text = Info_Box[0], fg = '#ff0000', font = ("Times",18,'bold'), bg = '#000d33')
        time_file.config(text = Info_Box[1], fg = '#ff0000', font = ("Times",20,'bold'), bg = '#000d33')
        volume.config(text = Info_Box[2], fg = '#ff0000', font = ("Times",20,'bold'), bg = '#000d33')
        number.config(text = Info_Box[3], fg = '#ff0000', font = ("Times",20,'bold'), bg = '#000d33')
        name_file.grid(row = 2, column = 0, columnspan = 8)
        time_file.grid(row = 3, column = 1, columnspan = 5)
        volume.grid(row = 4, column = 1, columnspan = 5)        
        number.grid(row = 5, column = 1, columnspan = 5)
    def GUI_control(but): # Make commands
        global command
        command = but
        sleep(0.1)
        show_info()
    def Top_Menu(): # Show menu
        def Menu_commands(get_command):
            global command
            command = get_command
            Change_Info()
        Menu_bar = Menu(win) # Make Top main menu bar
        File_menu = Menu(Menu_bar, tearoff = 0) # Add first menu to menu bar
        File_menu.add_command(label='Restart',command=Change_Directory)
        File_menu.add_command(label='Change', command=lambda:Menu_commands('cha'))
        File_menu.add_command(label='Next',   command=lambda:Menu_commands('nex'))
        File_menu.add_command(label='Back',   command=lambda:Menu_commands('bac'))
        File_menu.add_separator() # Just line
        File_menu.add_command(label='Exit',   command=lambda:_exit(0))
        Search_menu = Menu(win, tearoff = 0)
        Search_menu.add_command(label='By name',   command=lambda:Menu_commands('search'))
        Search_menu.add_command(label='By number',   command=lambda:Menu_commands('GoTo'))
        Menu_bar.add_cascade(label = "File", menu = File_menu)
        Menu_bar.add_cascade(label = "Search", menu = Search_menu)    
        win.config(menu=Menu_bar)
    def Keabord_Controll(event):
        global command
        key = event.char
        if key in ['g' or 'G']:
            command = 'GoTo'
        if key in ['c' or 'C']:
            command = 'cha'
        if key in ['b' or 'B']:
            command = 'bac'
        if key in ['n' or 'N']:
            command = 'nex'
        if key in ['s' or 'S']:
            command = 'search'
        Change_Info()
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
    Gui_sitting()
    Change_Info() # Show First file when player open
    win.mainloop()


def Main_player(play): # MAin player
    global Info_Box, command
    command = 'none' # Avoid running a command twice
    file = MediaPlayer(List_of_files[play])
    file.play()
    volume = file.audio_get_volume()
    time_file = Size_File(play)
    name = File_Name(play)
    Info_Box = [name, play+1, time_file, volume] # Add informations to the list for showing
    commands(file, play, volume, time_file)
    

def File_Name(play): # Get the name of file
    name = List_of_files[play].split("\\")
    name = name[-1].split('.')
    name.pop(-1)
    name = ".".join(name)
    if len(name) > 45:
        return name[0:45] + " ..."
    else:
        return name    


def commands(file, play, volume, time_file): # Check commands
    global command, Info_Box, Timer
    pause = True # Pause and unpa
    while True:
        if command == 'bac' or command == 'nex' or command == 'cha' or command == 'exi':
            file.stop()
            Change(command, play)
        elif command == 'GoTo':
            GoTo(file)
        elif command == 'search':
            Search(file)
        elif command == 'vl+' or command == 'vl-':
            volume = Change_Volume(command, volume)
            file.audio_set_volume(volume)
            command = 'none'
            Info_Box[3] = volume
        elif command == 'pau':
            command = 'none'
            if pause == True:
                file.pause()
                pause = False
                pause_time = Timer # Get Timer for when unpause start from that
                Timer = (10**10)
                continue
            else:
                file.play()
                Timer = pause_time
                pause = True
        else:
            continue


def GoTo(file): # For goto command make window to Enter the file number
    def accept(event): # Go to file
        play = Enter.get()
        if play.isdigit():
            play = int(play) - 1
            if play >= 0 and play < len(List_of_files):
                file.stop()
                Go_win.destroy()
                Thread(target=Change_Info).start()
                Main_player(play)
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
    Button(Go_win,bd=6,text = 'cancel',command=Cancel,font=("Times",13,'bold')).grid(row = 2,column=2) # Cancel
    Go_win.bind('<Return>', accept) # Accept buy pressing Enter
    Go_win.mainloop()


def Change(command, play):  # Change mp3 file or Close program
    if command == 'cha':  # get random file
        Random = randrange(0, len(List_of_files))
        Main_player(Random)
    if command == 'nex':  # go to next file
        if play == len(List_of_files) - 1:
            Main_player(0)
        else:
            Main_player(play + 1)
    if command == 'bac':  # go to pervios file
        if play == 0:
            Main_player(play)
        else:
            Main_player(play - 1)
    if command == 'exi':
        _exit(0)


def Change_Volume(command, Volume): # Change the volume
    if command == 'vl+':
        if Volume < 250:
            return Volume + 5
        else:
            return Volume
    if command == 'vl-':
        if Volume > 0:
            return Volume - 5
        else:
            return Volume


def Size_File(play): # Get time of any file
    global Timer
    Time = File(List_of_files[play])
    Time = int(Time.info.length)  # Get the files time in secound
    Timer = int(Time) # Send it for timer function
    Minute = str(Time // 60)  # get minute
    Second = str(Time % 60)  # get second
    if len(Second) == 1:  # Change XX:X to XX:0X
        Second = '0' + Second
    return ("⌛ " + Minute + ":" + Second + " ⌛")


def File_Timer(): # When music over go to next
    global command, Timer
    while True: # Timer of file
        sleep(1)
        Timer -= 1
        if Timer == 0:
            command = 'nex'
            Change_Info()


def Change_Info(): # When use goto or music end change the informations
    sleep(0.3)
    Indicator_Button.invoke()


def Change_Directory(): # Change Direcotry and get new files
    global List_of_files
    Destroy = True # Destroyed first Gui page 1 time
    sleep(0.5)
    welcome_win = Tk() # First Gui window
    welcome_win.geometry('424x81+600+0')
    massage = Label(welcome_win, text = "<<  welcome  >>\n    Please select ur directory    ")
    massage.config(font = ("Times",25,'bold') ,fg = '#000066', bg='#ffb6ff')
    massage.grid(row = 0,column = 0)
    while True:
        List_of_files = glob(Select_Dirctory()) # Get the Directore mp3 files
        if Destroy == True: 
            welcome_win.destroy()
            Destroy = False
        if len(List_of_files) != 0: # Directory is NOT empty
            break


def Starter(): # Start the program
    global List_of_files
    List_of_files = Get_Files()
    Main_player(0)


def Search(file):
    def accept(event): # Go to file
        def Selection(play):
            file.stop()
            Search_win.destroy()
            Thread(target=Change_Info).start()
            Main_player(play)
        Name = Enter.get()
        Search_list = []
        for i in List_of_files: # Find files and put in list to make menue
            if Name.lower() in i.lower(): # Compare them with out upper and lower case
                Search_list.append(i)
        if len(Search_list) == 0:
            showerror("error",'Ca')
            Cancel()
        else:
            Search_menu = Menu(Search_win,tearoff=0)
            for Name in Search_list: # This Name is new variable and dont need the first one anymore
                Show_name = Name.split('\\')
                Show_name = str(List_of_files.index(Name) + 1) + ' : ' + Show_name[-1]
                Search_menu.add_command(label=Show_name,command=lambda Name = Name :Selection(List_of_files.index(Name)))
            Search_menu.tk_popup(event.x_root,event.y_root)
    def Cancel(): # continue playing files
        global command
        command = 'None'
        Search_win.destroy() # Close window
    Search_win = Tk()
    Search_win.resizable(False,False)
    Search_win.title('Search_File')
    Search_win['background'] = 'pink'
    Label(Search_win,text='Enter Name : ',font=("Times",15,'bold'),bg='pink').grid(row = 0,column=0)
    Label(Search_win,bg='pink',text='-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-',font=("Times",7,'bold')).grid(row = 1,column=0,columnspan=3)
    Label(Search_win,text='🎼',font=("Times",30,'bold'),bg='pink').grid(row = 2,column=0)
    Enter = Entry(Search_win,font=("Times",15,'bold'))
    Enter.grid(row = 0,column=1,columnspan=2)
    Button(Search_win,bd=6,text='Search',command = accept,font=("Times",13,'bold')).grid(row = 2,column=1)
    Button(Search_win,bd=6,text = 'cancel',command=Cancel,font=("Times",13,'bold')).grid(row = 2,column=2) # Cancel
    Search_win.bind('<Return>', accept) # Accept buy pressing Enter
    Search_win.mainloop()


Starter()