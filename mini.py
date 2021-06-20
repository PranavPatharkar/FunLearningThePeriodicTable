# Title: Fun learning the periodic table

from tkinter import *
import tkinter
import random
import webbrowser
from pygame import *
from pygame import mixer

play =0
song =0
def bgmusic():
    mixer.init()
    global song
    song = random.randint(0, 5)
    if song == 0:
        mixer.music.load("assets/mp3s/music0.mp3")
    if song == 1:
        mixer.music.load("assets/mp3s/music1.mp3")
    if song == 2:
        mixer.music.load("assets/mp3s/music2.mp3")
    if song == 3:
        mixer.music.load("assets/mp3s/music3.mp3")
    if song == 4:
        mixer.music.load("assets/mp3s/music4.mp3")
    if song == 5:
        mixer.music.load("assets/mp3s/music5.mp3")
    mixer.music.play(-1)

questions_list = [
    "How many protons does Hydrogen have ?",
    "What is the atomic mass number of Helium ?",
    "Which among these is a group 18 element ?",
    "Which of the following is a noble element ?",
    "Which of the following elements belong to atomic number 10 ?",
    "Which of the following elements doesn’t belong to S block ?",
    "Which element has an electronic configuration 1s2 2s1 ?",
    "How many isotopes does Hydrogen have ?",
    "Which of the following describes Oxygen ?",
    "Which group does Neon belong ?",
    ' How many isotopes does Carbon have?',
    ' What is the atomic symbol of Helium?',
    ' Which of the following elements have atomic number 6?',
    ' Which is the atomic symbol of Berrylium?',
    ' What is the Atomic number of Fluorine?',
    ' What is the atomic symbol of Neon?',
    ' Select the electronic configuration of Nitrogen.',
    ' Which of the following describes Lithium?',
    ' What is the atomic mass number of Helium?',
    ' Which of the following is an S block element?'
]

four_options = [
    ["3", "1", "2", "0", ],
    ["3", "1", "2", "4", ],
    ["Neon", "Fluorine", "Berrelium", "Lithium", ],
    ["H", "Ne", "C", "O", ],
    ["F", "Na", "Ne", "O", ],
    ["Li", "He", "Be", "N", ],
    ["Oxygen", "Lithium", "carbon", "Nitrogen", ],
    ["1", "2", "3", "0", ],
    ["Non metal", "Alkali metal", "Alkaline earth metal", "Halogen", ],
    ["1", "17", "2", "18", ],
    ["5", "2", "3", "1"],
    ["He", "Ha", "H", "Hel"],
    ["Nitrogen", "Carbon", "Oxygen", "Fluorine"],
    ["Be", "B", "Ber", "Br"],
    ["10", "9", "8", "7"],
    ["Ne", "N", "No", "Na"],
    ["1s2 2s2 2p1", "1s2 2s1", "1s2 2s2 2p3", "1s2 2s2 2p6"],
    ["Alkali Metal", "Noble Element", "Metal", "Alkaline Earth Metal"],
    ["1", "3", "5", "4"],
    ["Carbon", "Berrylium", "Nitrogen", "Neon"]

]

correct_answers = [1, 3, 0, 1, 2, 3, 1, 2, 0, 3, 2, 0, 1, 0, 1, 0, 2, 0, 3, 1]
user_choice = []
indices = []

def callback(url):
    webbrowser.open_new_tab(url)

def generate():
    global indices
    while(len(indices) < 10):
        x = random.randint(0, 19)
        if x in indices:
            continue
        else:
            indices.append(x)

def display_result(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelresultimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelresultimage.pack(pady=(50, 30))
    labelresulttext= Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()

    if score >= 8:
        if mixer.music.get_busy() == True:
            mixer.music.stop()
            mixer.music.load("assets/mp3s/excellent.mp3")
            mixer.music.play()
        img = PhotoImage(file="assets/pngs/Exc.png")
        labelresultimage.configure(image=img)
        labelresultimage.image = img
        labelresulttext.configure(
            text=f"You Are Excellent !! Your score is:{score}/10",background = "#7493ff")

    elif (score >= 5 and score < 8):
        if mixer.music.get_busy() == True:
            mixer.music.stop()
            mixer.music.load("assets/mp3s/goodjob.mp3")
            mixer.music.play()
        img = PhotoImage(file="assets/pngs/good.png")
        labelresultimage.configure(image=img)
        labelresultimage.image = img
        labelresulttext.configure(
            text=f"You Can Be Better !! Your score is:{score}/10", background = "#c091ff")

    else:
        if mixer.music.get_busy() == True:
            mixer.music.stop()
            mixer.music.load("assets/mp3s/workhard.mp3")
            mixer.music.play()
        img = PhotoImage(file="assets/pngs/workk.png")
        labelresultimage.configure(image=img)
        labelresultimage.image = img
        labelresulttext.configure(
            text=f"You Should Work Hard !! Your score is:{score}/10", background = "#c091ff")
    btnquit.pack(pady = 15)

def calculate_score():
    global indices, user_choice, correct_answers
    x = 0
    score = 0
    for i in indices:
        if user_choice[x] == correct_answers[i]:
            score = score + 1
        x += 1
    #print(score)
    display_result(score)

ques = 1

def selected():
    global radiovar, user_choice
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_choice.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text=questions_list[indices[ques]])
        r1['text'] = four_options[indices[ques]][0]
        r2['text'] = four_options[indices[ques]][1]
        r3['text'] = four_options[indices[ques]][2]
        r4['text'] = four_options[indices[ques]][3]
        ques += 1
    else:
        calculate_score()


def start_quiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions_list[indices[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#3f95ff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=four_options[indices[0]][0],
        font=("Times", 14),
        value=0,
        variable=radiovar,
        command=selected,
        background="#4295ff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=four_options[indices[0]][1],
        font=("Times", 14),
        value=1,
        variable=radiovar,

        command=selected,
        background="#6094ff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=four_options[indices[0]][2],
        font=("Times", 14),
        value=2,
        variable=radiovar,
        command=selected,
        background="#7394ff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=four_options[indices[0]][3],
        font=("Times", 14),
        value=3,
        variable=radiovar,
        command=selected,
        background="#8e92ff",
    )
    r4.pack(pady=5)

def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    lblLink.destroy()
    link.destroy()
    generate()
    start_quiz()

root = tkinter.Tk()
root.title("Fun Learning The Periodic Table!")
root.geometry("700x800")
bg = PhotoImage(file = "assets/pngs/bg4.png")
label1 = Label( root, image = bg)
label1.place(x = 0 , y = 0)
bgmusic()
# root.resizable(0,0)

def exit():
    root.quit()
btnquit = Button(
    root,
    text="QUIT",
    font=("Comic sans MS", 13, "bold"),
    relief=FLAT,
    border=0,
    background="#4e94ff",
    width = 15,
    command=exit,
)

btnmute = Button(
    root,
    text="Music Off",
    font=("Comic sans MS", 10, "bold"),
    relief=FLAT,
    border=0,
    background="#4e94ff",
    width = 10,
    command=pause,
)
btnmute.pack(padx = 5,pady = 5,side=BOTTOM, anchor=SE)

btnunpause = Button(
    root,
    text="Music On",
    font=("Comic sans MS", 10, "bold"),
    relief=FLAT,
    border=0,
    background="#4e94ff",
    width = 10,
    command=unpause,
)
btnunpause.pack(padx = 5, side=BOTTOM, anchor=SE)

img1 = PhotoImage(file="assets/pngs/Ptable.png")

labelimage = Label(
    root,
    image=img1,
    #background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="Fun Learning The Periodic Table!",
    font=("Comic sans MS", 24, "bold"),
    background="#4e94ff",
)
labeltext.pack(pady=(0, 100))

img2 = PhotoImage(file="assets/pngs/start3.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Read The Rules.\nClick Start Once You Are ready.",
    background="purple",  #b892ff
    foreground = "white",
    font=("Comic sans MS", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 100))

lblLink = Label(
    root,
    text="You can have look at contents of periodic table here:\n",
    width=100,
    font=("Times", 14),
    foreground="#000000",
    background="pink",
)
lblLink.pack(pady=(10, 20))

link = Label(root, text="Go to database: click here", font=(
    'Comic sans MS', 12), width=100, fg="blue", bg="yellow", cursor="hand2")
link.pack(pady=(0, 20))
link.bind("<Button-1>",
          lambda e: callback("https://en.wikipedia.org/wiki/List_of_chemical_elements"))
lblRules = Label(
    root,
    text="This quiz contains Multiple choice questions.\nOnce you select an option that will be a final choice,\nhence think before you select!!",
    width=100,
    font=("Times", 14),
    foreground="#000000",
    background="#00FFFF",
)
lblRules.pack()

root.mainloop()
#End of the source code