from tkinter import *
from tkinter import colorchooser

from Snake.main import Snake


class Welcome_snake(Tk):

    def __init__(self):
        super().__init__()
        self.title("Snake Game By Aimad 😊")
        self.width = 800
        self.height = 600
        self.resizable(False,False)
        self.center_screen()
        self.bind("<c>",self.check_background)

        #image of snake in label
        self.label = Label(self,text="Hello",font=("arial",30))
        self.label.place(x=self.width//2,y=self.height//2)

        # button
        self.play = Button(self,text="Play",font=("Arial",15),command=self.play)
        self.play.place(x=125,y=123)



    def play(self):
        self.destroy()
        from Snake import main
        run_game = Snake()
        run_game.mainloop()

    def center_screen(self):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Get X and Y value
        x = (screen_width // 2) - (self.width //2)
        y = (screen_height // 2) - (self.height //2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def check_background(self,event):

        if (event.keysym):
            color = colorchooser.askcolor()
            self.config(bg=color[1])
            self.label.config(bg=color[1])




if __name__ == "__main__":

    welcome = Welcome_snake()
    welcome.mainloop()
