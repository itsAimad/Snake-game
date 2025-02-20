import tkinter
from tkinter import *
from tkinter import colorchooser,ttk
from PIL import Image, ImageTk
from PIL.ImageOps import expand
from Snake import main
from MongoDatabase import mongo_connection



class Welcome_snake(Tk):

    def __init__(self):
        super().__init__()
        self.title("Snake Game By Aimad 😊")
        self.width = 800
        self.height = 600
        self.resizable(False,False)
        self.center_screen()
        self.bind("<c>",self.check_background)
        self.config(bg="#6fdf62")

        # icon for the window
        self.icon = PhotoImage(file="Images/img.png")
        self.iconphoto(True,self.icon)

        # Label for Title
        self.text = Label(self,text="Welcome to Snake Game !",font=("Impact", 26),bg="#6fdf62")
        self.text.place(x=210,y=70)

        #image of snake in label
        self.image = Image.open("Images/img.png")
        self.image = self.image.resize((180,180))
        self.image_ = ImageTk.PhotoImage(self.image)
        self.img_label = Label(self,image=self.image_,bg="#6fdf62")
        self.img_label.place(x=300,y=140)

        # button of play
        self.play = Button(self,text="Play",font=("Impact",16),command=self.play,bg="#505770",width=7,height=1)
        self.play.place(x=270,y=373)

        # button of view old score
        self.view = Button(self,text="View Scores", font=("Impact",16),command=self.view_scores,bg="#505770",width=11,height=1)
        self.view.place(x=430,y=373)



    def play(self):
        self.destroy()
        main.Snake().mainloop()


    def view_scores(self):

        # new window for scores
        table = Toplevel(self)
        table.title("Scores 💯")

        # Create a treeview widget
        tree = ttk.Treeview(table,columns=("Date","Score"),show="headings")
        tree.heading("Date",text="Date")
        tree.heading("Score",text="Score")

        # Retreive data
        scores = self.retreive_scores()

        for score in scores:
            tree.insert("",END,values=(score["Date"],score["Score"]))


        tree.pack(fill=BOTH,expand=True)
    def retreive_scores(self):
        scores_collection = mongo_connection()
        scores = scores_collection.find({},{"_id":0,"Date":1,"Score":1})

        return list(scores)






    def center_screen(self):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Get X and Y value
        x = (screen_width // 2) - (self.width //2)
        y = (screen_height // 2) - (self.height //2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

        return  screen_width,screen_height

    def check_background(self,event):

        if (event.keysym):
            color = colorchooser.askcolor()
            self.config(bg=color[1])
            self.img_label.config(bg=color[1])
            print(color[1])




if __name__ == "__main__":

    welcome = Welcome_snake()
    welcome.mainloop()
