from tkinter import *
from datetime import date
import pygame
from pygame.locals import *
from pygame import mixer


from PIL import ImageTk, Image  # PIL -> Pillow
from tkinter import messagebox


root = Tk()
root.title("Library")
root.minsize(width=1000, height=800)
root.geometry("1800x1180")
same = True
n = 2.2


# Adding a background image
background_image = Image.open("Checkers_image.JPG")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize(
    (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(1100, 530, image=img)
Canvas1.config(bg="black", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="red", bd=5)
headingFrame1.place(relx=0.20, rely=0.05, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="CHECKERS",
                     bg='black', fg='red', font=('Courier', 80))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


def game():

   # root.quit()
    import GUI


def rules():

    root = Tk()
    root.title("RULES")
    root.minsize(width=400, height=400)
    root.geometry("1800x1180")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#25b89a")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="black", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.10)

    headingLabel = Label(headingFrame1, text="RULES",
                         bg='cyan', fg='black', font=('Courier', 17))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='grey')
    labelFrame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)
    y = 0.35

    Label(labelFrame, text="Taking a Turn", bg='grey', fg='white',
          font=('Courier', 25, 'bold')).place(relx=0.35, rely=0.05)
    Label(labelFrame, text="Typically the darker color pieces moves first.Each player takes their turn by moving a piece.Pieces are always moved diagonally ",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.02, rely=0.15)
    Label(labelFrame, text="and can be moved in the following ways: ",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.02, rely=0.20)
    Label(labelFrame, text="Diagonally in the forward direction (towards the opponent) to the next dark square. ",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.25)
    Label(labelFrame, text="If there is one of the opponent's pieces next to a piece and an empty space on the other side, you jump your opponent",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.30)
    Label(labelFrame, text="and remove their piece. You can do multiple jumps if they are lined up in the forward direction",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.35)
    Label(labelFrame, text="KING PIECES", bg='grey', fg='white',
          font=('Courier', 25, 'bold')).place(relx=0.35, rely=0.43)
    Label(labelFrame, text="The last row is called the king row. If you get a piece across the board to the opponent's king row, that piece becomes a king",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.50)
    Label(labelFrame, text="Another piece is placed onto that piece so it is now two pieces high. King pieces can move in both directions, forward and backward",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.55)
    Label(labelFrame, text="Once a piece is kinged, the player must wait until the next turn to jump out of the king row",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.60)
    Label(labelFrame, text="WINNING THE GAME", bg='grey', fg='white',
          font=('Courier', 25, 'bold')).place(relx=0.35, rely=0.65)
    Label(labelFrame, text="You win the game when the opponent has no more pieces or can't move (even if he/she still has pieces)",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.75)
    Label(labelFrame, text="If neither player can move then it is a draw or a tie.",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.80)

    quitBtn = Button(root, text="Quit", bg='#FF5733', fg='black',
                     font=('Courier', 30, 'bold'), command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def about():

    root = Tk()
    root.title("ABOUT")
    root.minsize(width=400, height=400)
    root.geometry("1800x1180")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#25b89a")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="black", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.10)

    headingLabel = Label(headingFrame1, text="RULES",
                         bg='cyan', fg='black', font=('Courier', 17))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='grey')
    labelFrame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)
    y = 0.35

    Label(labelFrame, text="HOW TO USE THE APP", bg='grey', fg='white',
          font=('Courier', 25, 'bold')).place(relx=0.35, rely=0.05)
    Label(labelFrame, text=" TO CHECK THE RULES CLICK ON RULES BUTTON ",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.02, rely=0.15)
    Label(labelFrame, text="After you know the rules click on the play game option ",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.02, rely=0.20)
    Label(labelFrame, text="In the game section click on settings and add your names",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.25)
    Label(labelFrame, text="After that click on play option to start playing",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.30)
    Label(labelFrame, text="PLAY as per the rules for additional help a help box will show messages to help you",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.35)

    Label(labelFrame, text="After you play the game you can check your high scores",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.50)
    Label(labelFrame, text="After you have finished playing then you can click on exit button to exit game",
          bg='grey', fg='white', font=('Courier', 13)).place(relx=0.04, rely=0.55)

    quitBtn = Button(root, text="Quit", bg='#FF5733', fg='black',
                     font=('Courier', 30, 'bold'), command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


# adding buttons


btn1 = Button(root, text="Play Game", bg='black', fg='white', font=(
    'Courier', 60), command=lambda: [root.destroy(), game()])
btn1.place(relx=0.35, rely=0.39, relwidth=0.35, relheight=0.1)

btn2 = Button(root, text="RULES", bg='black', fg='white',
              font=('Courier', 60), command=rules)
btn2.place(relx=0.35, rely=0.59, relwidth=0.35, relheight=0.1)

btn3 = Button(root, text="ABOUT", bg='black', fg='white',
              font=('Courier', 60), command=about)
btn3.place(relx=0.35, rely=0.79, relwidth=0.35, relheight=0.1)

root.mainloop()
