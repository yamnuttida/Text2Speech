from tkinter import *
from PIL import ImageTk, Image
from os import path
from playsound import playsound
from tkinter import filedialog 
import time
from mutagen.mp3 import MP3
from pygame import mixer
from tkinter import messagebox
import main as m ##import function from main.py
import playgif as pg ##import function from playgif.py(loading)

root = Tk()
root.title("Story")
root.iconbitmap("fairytale.ico")
root['background']='#b8f6fd'

##--------------------background---------------------------##
canv = Canvas(root, width=1190, height=720, bg='#b8f6fd')
canv.grid(row=0, column=3)

img = ImageTk.PhotoImage(Image.open("bs3.png"))  # PIL solution
canv.create_image(40, 40, anchor=NW, image=img)


#------------------------------page show story--------------------------#
def OpenFile():
    global folder
    global run
    name = filedialog.askopenfilenames(initialdir="",
                           filetypes =(("pdf files","*.pdf"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print(name)
    if name == '':
        clear_frame()
        display(folder)
        button_upload = Button ( root, text='Upload',image= my_img3 ,bg='#b8f6fd', fg='White', command=lambda: [stop_autoplay(),loading_img(),OpenFile(),runingg(),complete(),display(folder)]).grid(row=1, column=3)
        run = False

    else:
        fol_name = name[0].split('/')[-1].rsplit('.')[0]
        story_name = name[0].split('/')[-1]
        folder_name = m.pdf_to_image(name[0], fol_name)
        text = m.get_text_from_im(folder_name)
        folder = folder_name
        print(folder)
    return folder

#----------------------------------page book rec--------------------------------#
def OpenFile2():
    global folder
    global run
    name = filedialog.askopenfilenames(initialdir="",
                           filetypes =(("pdf files","*.pdf"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print(name)
    if name == '':
        # clear_frame()
        root.destroy()
        import gui

    else:
        fol_name = name[0].split('/')[-1].rsplit('.')[0]
        story_name = name[0].split('/')[-1]
        folder_name = m.pdf_to_image(name[0], fol_name)
        text = m.get_text_from_im(folder_name)
        folder = folder_name
        print(folder)
    return folder


#----------------------get image--------------------------------##

def open_image(folder):
    imger_list = []
    condition = True
    var = {}
    var2 = {}
    i = 0
    while condition:
        if path.exists(f"{folder}//image{i}.png"):
            image_path = f"{folder}//image{i}.png"
            var["my_img{0}".format(i)] = Image.open(image_path)
            imger_list.append(resize_image(var["my_img{0}".format(i)], i ,var2))
        else:
            condition = False
        i+=1
    return imger_list
#--------------------------get sound------------------------------#
def open_sound(folder):
    sound_list = []
    condition = True
    i = 0
    while condition:
        if path.exists(f"{folder}//sound//sound{i}.mp3"):
            image_path = f"{folder}//sound//sound{i}.mp3"
            sound_list.append(image_path)
        else:
            condition = False
        i+=1
    return sound_list

def resize_image(image, i, var2 ):
    var2["new_pic{0}".format(i)] = ImageTk.PhotoImage(image.resize((650, 650), Image.ANTIALIAS))
    return var2["new_pic{0}".format(i)]

#----------------------------function play sound-------------------------------#
 
def playfirst(sound_list):
    mixer.init()
    mixer.music.load(sound_list[0])
    mixer.music.play()

def play_forward(image_number,sound_list):
    mixer.init()
    mixer.music.load(sound_list[image_number-1])
    mixer.music.play()

#-----------------------function forward button----------------------------#
def forward(image_number,imger_list):
    global my_lable
    global button_forward
    global button_back

    # my_lable.grid_forget()
    my_lable = Label(image= imger_list[image_number-1])

    button_forward = Button(root, text = ">>",image= my_img2 ,bg='#b8f6fd',command = lambda: [forward(image_number+1,imger_list),play_forward(image_number+1,sound_list)])
    button_back = Button(root, text = "<<",image= my_img1 ,bg='#b8f6fd',command = lambda: [forward(image_number-1,imger_list),play_forward(image_number-1,sound_list)])
    
    if image_number == len(imger_list):
        button_forward = Button(root, text=">>",image= my_img2 ,bg='#b8f6fd',state = DISABLED)


    my_lable.grid(row = 0, column = 3)
    button_back.grid(row=0, column=1)
    button_forward.grid(row=0, column=4)

#-----------------------function back button----------------------------#
def back(image_number):
    global my_lable
    global button_forward
    global button_back
    # my_lable.grid_forget()
    my_lable = Label(image= imger_list[image_number-1])
    button_forward = Button(root, text = ">>",image= my_img2 ,bg='#b8f6fd',command = lambda: [forward(image_number+1,imger_list),play_forward(image_number+1,sound_list)])
    button_back = Button(root, text = "<<",image= my_img1 ,bg='#b8f6fd',command = lambda: [forward(image_number-1,imger_list),play_forward(image_number-1,sound_list)])

    if image_number == 0:
        button_back = Button(root, text=">>",image= my_img1 ,bg='#b8f6fd',state = DISABLED)

    my_lable.grid(row = 0, column = 3)
    button_back.grid(row=0, column=1)
    button_forward.grid(row=0, column=4)

#------------------------pop up loading--------------------------#

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

def loading_img():
    clear_frame()
    lbl = pg.ImageLabel(root)
    lbl.grid(row = 0, column=3)
    lbl.load('loading3.gif')
    lbl.place_forget()
    return 

##-----------------------------process upload file button----------------------------------##
def complete():
    global run
    if run:
        messagebox.showinfo('Info', 'Process completed!')
    return 

def runingg():
    global run
    if run:
        time.sleep(1)
    return

def show():
    global run
    if run:
        myLabel = Label(root, text=clicked.get()).place(x=250, y=30)


def display(folder):
    global imger_list
    global sound_list
    global run

    if run:
        clear_frame()
        print(folder)

        imger_list = open_image(folder)

        lbl = pg.ImageLabel(root)
        lbl.grid(row = 0, column=3)
        lbl.load('bk4.jpg')

        my_lable = Label(image =imger_list[0])
        my_lable.grid(row = 0, column = 3)
        sound_list = open_sound(folder)
        my_lable.bind("<Button-1>", playfirst(sound_list))
        button_back = Button(root, text = "<<" ,image= my_img1 ,bg='#b8f6fd', command= lambda:[back(1),play_forward(1,sound_list)]).grid(row=0, column=1)
        button_upload = Button ( root, text='Upload',image= my_img3 ,bg='#b8f6fd', fg='White', command=lambda: [stop_autoplay(),loading_img(),OpenFile(),runingg(),complete(),display(folder)]).grid(row=1, column=3)
        button_forward = Button(root, text=">>", image= my_img2 ,bg='#b8f6fd',command=lambda: [forward(2,imger_list),play_forward(2,sound_list)]).grid(row=0, column=4)
        button_autoplay = Button(root, text= 'autoplay',image= my_img4 , bg='#e5885d',relief="groove", command = lambda: [start_autoplay(),root.after(0, autoplay)]).place(x=100,y=650)
        button_stopplay = Button(root, text= 'stop play',bg='#e5885d', image= my_img5 ,command = lambda: stop_autoplay()).place(x=220,y=650)
        exit_button = Button(root, text="Exit", bg = '#f06524',fg='White',relief="groove",  command= lambda: [stop_autoplay(),root.destroy()]).place(x =1280, y=10)
        button_backward = Button(root, width=20, text='<<back', bg='#98603b',relief="groove",fg='White', command=lambda : [stop_autoplay(),prevPage()]).place(x=10,y=10) 
    return 

##-----------------------------------auto play--------------------------------##

def play_auto(s):
    mixer.init()
    mixer.music.load(s)
    mixer.music.play()

def stop_sound():
    mixer.music.stop()


i = 0
def autoplay():
    global i
    if running:
        try:
            my_lable = Label(root, image=imger_list[i])
            my_lable.grid(row = 0, column = 3)
            my_lable.bind("<Button-1>", play_auto(sound_list[i]))
            audio = MP3(f"{folder}//sound//sound{i}.mp3")
            time = (round(audio.info.length)*1000)+2000
            root.after(time, autoplay)
        except:
            root.after(5000, autoplay)
        i+=1


def start_autoplay():
    global running
    running = True

def stop_autoplay():
    global running
    running = False
    stop_sound()


#------------------------- button style----------------------------#
b = Image.open('back.png')
b = b.resize((50, 50), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(b)

fw = Image.open('forward.png')
fw = fw.resize((50, 50), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(fw)

ul = Image.open('upload.png')
ul = ul.resize((85, 40), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(ul)

atp = Image.open('autoplay1.png')
atp = atp.resize((100, 50), Image.ANTIALIAS)
my_img4 = ImageTk.PhotoImage(atp)

st = Image.open('stop.png')
st = st.resize((45, 45), Image.ANTIALIAS)
my_img5 = ImageTk.PhotoImage(st)


#---------------------------image show book shell------------------------------#

ph1 = Image.open('011.jpg')
ph1 = ph1.resize((150,200),Image.ANTIALIAS)
my_ph1 = ImageTk.PhotoImage(ph1)

my_ph11 = Label(root,borderwidth=6, relief="groove",image = my_ph1)
my_ph11.place(x=160,y=130)

ph2 = Image.open('002.jpg')
ph2 = ph2.resize((150,200),Image.ANTIALIAS)
my_ph2 = ImageTk.PhotoImage(ph2)

my_ph22 = Label(root,borderwidth=6, relief="groove",image = my_ph2)
my_ph22.place(x=390,y=130)

ph3 = Image.open('019.jpg')
ph3 = ph3.resize((150,200),Image.ANTIALIAS)
my_ph3 = ImageTk.PhotoImage(ph3)

my_ph33 = Label(root,borderwidth=6, relief="groove",image = my_ph3)
my_ph33.place(x=620,y=130)

ph4 = Image.open('21.jpg')
ph4 = ph4.resize((150,200),Image.ANTIALIAS)
my_ph4 = ImageTk.PhotoImage(ph4)

my_ph44 = Label(root,borderwidth=6, relief="groove",image = my_ph4)
my_ph44.place(x=850,y=130)

ph5 = Image.open('22.jpg')
ph5 = ph5.resize((150,200),Image.ANTIALIAS)
my_ph5 = ImageTk.PhotoImage(ph5)

my_ph55 = Label(root,borderwidth=6, relief="groove",image = my_ph5)
my_ph55.place(x=160,y=440)

ph6 = Image.open('23.jpg')
ph6 = ph6.resize((150,200),Image.ANTIALIAS)
my_ph6 = ImageTk.PhotoImage(ph6)

my_ph66 = Label(root,borderwidth=6, relief="groove",image = my_ph6)
my_ph66.place(x=390,y=440)

ph7 = Image.open('25.jpg')
ph7 = ph7.resize((150,200),Image.ANTIALIAS)
my_ph7 = ImageTk.PhotoImage(ph7)

my_ph77 = Label(root,borderwidth=6, relief="groove",image = my_ph7)
my_ph77.place(x=620,y=440)

ph8 = Image.open('16.jpg')
ph8 = ph8.resize((150,200),Image.ANTIALIAS)
my_ph8 = ImageTk.PhotoImage(ph8)

my_ph88 = Label(root,borderwidth=6, relief="groove",image = my_ph8)
my_ph88.place(x=850,y=440)

## image BOOK rec ##
ph0 = Image.open('book.jpg')
ph0 = ph0.resize((100,50),Image.ANTIALIAS)
my_ph0 = ImageTk.PhotoImage(ph0)

my_ph00 = Label(root,borderwidth=6, relief="groove",image = my_ph0)
my_ph00.place(x=530,y=25)

#--------------------------------------------function---------------------------------------#
list_folder = ['011-DYLAN-THE-DRAGON-Free-Childrens-Book-By-Monkey-Pen','002-GINGER-THE-GIRAFFE-Free-Childrens-Book-By-Monkey-Pen',
'019-BUBBLE-FUN-Free-Childrens-Book-By-Monkey-Pen','021','022','023','025','016']
folder = ''

#--------------------------------back to book shell button function---------------------------#
def prevPage():
    root.destroy()
    import gui

#--------------------------------get folder function------------------------------# 
def cilck1(k):
    global folder
    folder = list_folder[k]
    return folder

#-------------------------------------------------RUN--------------------------------------------------#
#----------------------button Run-------------------------#
run = True
button_upload = Button ( root, text='Upload',image= my_img3 ,bg='#b8f6fd', fg='White', command=lambda: [loading_img(),OpenFile2(),runingg(),complete(),display(folder)]).grid(row=1, column=3)
button1 = Button(root, width=20, text='001',relief="groove",bg='White', command= lambda :[display(cilck1(0))]).place(x=165,y=350)

button2 = Button(root, width=20, text='002',relief="groove",bg='White', command=lambda : [display(cilck1(1))]).place(x=395,y=350)

button3 = Button(root, width=20, text='003',relief="groove",bg='White', command=lambda : [display(cilck1(2))]).place(x=625,y=350)

button4 = Button(root, width=20, text='004',relief="groove",bg='White', command=lambda : [display(cilck1(3))]).place(x=855,y=350)

button5 = Button(root, width=20, text='005',relief="groove",bg='White', command=lambda : [display(cilck1(4))]).place(x=165,y=660)

button6 = Button(root, width=20, text='006',relief="groove",bg='White', command=lambda : [display(cilck1(5))]).place(x=395,y=660)

button7 = Button(root, width=20, text='007',relief="groove",bg='White', command=lambda : [display(cilck1(6))]).place(x=625,y=660)

button8 = Button(root, width=20, text='008',relief="groove",bg='White', command=lambda : [display(cilck1(7))]).place(x=855,y=660)

exit_button = Button(root, text="Exit", bg = '#f06524',fg='White',relief="groove",  command= lambda: [root.destroy()]).place(x =1160, y=10)

x = True

def update_x():
    global x
    x = False

while x == True:
    try:
        root.update_idletasks()
        root.update()
        time.sleep(0.01)
    except:
        pass

root.mainloop()
