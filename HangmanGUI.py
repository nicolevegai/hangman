from tkinter import *


class HangmanGUI:
    def __init__(self, window):
        self.window = window
        bgrcolor = "#20207f"
        title = "THE HANGMAN"
        window.title("Hangman")
        window.geometry("1300x750")
        window.resizable(0, 0)

        self.frame = Frame(master=window, bg=bgrcolor)
        self.frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  # Expand the frame to fill the root window

        # Create a canvas to display the cards on
        self.image_frame = Frame(master=self.frame)
        self.canvas = []
        for i in range(5):
            # set the background to green to simulate a table and set the border thickness to 0
            self.canvas.append(Canvas(master=self.image_frame, width=250, height=500, bg="green", highlightthickness=0))
            self.canvas[i].grid(row=0, column=i)

        self.image_frame.grid(row=1, padx=20)

        self.label = Label(self.frame, text="", bg=bgrcolor, fg="white")
        self.label.grid(row=5)
        self.label.config(font=("Courier", 44))
        self.label2 = Label(self.frame, text=title, bg=bgrcolor, fg="White")
        self.label2.grid(row=0, columnspan=2)
        self.label2.config(font=("Courier", 20))

        self.bt1 = Button(self.frame, text="Hit me!")
        self.bt1.config(font=("Courier", 15))
        self.bt1.grid(row=1, column=1, columnspan=2)
        self.bt2 = Button(self.frame, text="Exit Game", bg="black", fg="yellow")
        self.bt2.grid(row=2, column=2)

