from tkinter import *
import random
from tkinter import colorchooser,messagebox
import pygame
from Snake import welcome_snake
from MongoDatabase import mongo_connection
from datetime import datetime

class Snake(Tk):

    
    def __init__(self):
        super().__init__()
        self.title("Snake Game")
        self.width  = 800
        self.height = 600
        self.resizable(False,False)
        self.center_screen()
        self.bind("<c>", self.background)
        self.canvas = Canvas(self,width=self.width,height=self.height,bg="#fff")
        self.canvas.pack()

        # Border of the game
        self.canvas.create_rectangle(14,14,self.width -10,self.height -10,outline="#000",width=8)

        # label for the score of the player
        self.CURRENT = 0
        self.score = Label(self,text=f"Your Score : {self.CURRENT}",font=("Impact",18),bg="#fff",justify="center")
        self.score.place(x=340,y=20)


        # icon for the game
        self.icon = PhotoImage(file="Images/img.png")
        self.iconphoto(True,self.icon)

        # Initialize pygame mixer
        pygame.mixer.init()
        # Load Songs
        self.background_music = pygame.mixer.Sound("Songs/time to call.mp3")
        # self.eat_song = pygame.mixer.Sound("")

        # Play background song
        pygame.mixer.Sound.play(self.background_music,loops=-1)

        # Initialize game
        self.snake = [(40,60),(30,40), (20,40)]
        self.food = self.create_food()
        self.direction = "Right"
        self.bind("<KeyPress>",self.change_direction)
        self.update_snake()
        self.CURRENT = 0

    def center_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate X and Y
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height //2) - (self.height //2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}") # to center the window

    def background(self, event):
        if event.keysym:
            color = colorchooser.askcolor()
            self.canvas.config(bg=color[1])
            self.score.config(bg=color[1])
            print("You choosed :",color[1])

    def create_food(self):
        color = random.choice(["red","blue","green","orange","purple","gray","black"])
        x = random.randint(10,(self.width // 10  ) - 9)* 10
        y = random.randint(10,(self.height // 10 ) - 9)* 10
        self.canvas.create_oval(x,y,x+10,y+10,fill=color,outline=color,tags="food")

        return (x,y)

    def change_direction(self,event):
        opposite_directions  = {
            "Up" : "Down",
            "Down" : "Up",
            "Left" : "Right",
            "Right" : "Left"
        }
        if event.keysym in ["Up","Down","Left","Right"]:
            # check if the new direction isn't the oposite of the old direction
            if event.keysym != opposite_directions.get(self.direction):
                self.direction = event.keysym


    def update_snake(self):
        head_x,head_y = self.snake[0]

        if self.direction == "Up":
            head_y -=10
        elif self.direction == "Down":
            head_y +=10
        elif self.direction == "Left":
            head_x -=10
        elif self.direction == "Right":
            head_x +=10

        self.snake.insert(0,(head_x,head_y))

        if (head_x,head_y) == self.food:
            self.canvas.delete("food")
            self.random_score = [10,20,30,15,12,23,24]
            self.CURRENT += random.choice(self.random_score)
            self.score.config(text=f"Your Score : {self.CURRENT}")
            self.food = self.create_food()

        else:
            self.snake.pop()

        self.canvas.delete("snake")

        # Customizing the snake: Different colors for head and body and adding eyes
        for index, (x, y) in enumerate(self.snake):
            if index == 0:
                # Draw the head with gradient and details
                color = "#1E90FF"  # Blue for the head
                self.canvas.create_oval(x, y, x + 20, y + 20, fill=color, outline="#00008B", width=2,tag="snake")  # Head (same size as body)

                # Draw eyes (smaller and better positioned)
                eye_size = 6  # Size of the eyes
                self.canvas.create_oval(x + 5, y + 5, x + 5 + eye_size, y + 5 + eye_size,fill="white", outline="black", width=1, tag="snake")  # Left eye
                self.canvas.create_oval(x + 11, y + 5, x + 11 + eye_size, y + 5 + eye_size,fill="white", outline="black", width=1, tag="snake")  # Right eye

                # Draw pupils (smaller and centered in the eyes)
                pupil_size = 2  # Size of the pupils
                self.canvas.create_oval(x + 6, y + 6, x + 6 + pupil_size, y + 6 + pupil_size,fill="black", tag="snake")  # Left pupil
                self.canvas.create_oval(x + 12, y + 6, x + 12 + pupil_size, y + 6 + pupil_size,fill="black", tag="snake")  # Right pupil

                # Draw tongue (smaller and better positioned)
                self.canvas.create_line(x + 10, y + 18, x + 10, y + 22,fill="red", width=2, tag="snake")  # Tongue

            else:
                # Draw the body with gradient and scales
                color = "#32CD32"  # Green for the body
                self.canvas.create_oval(x, y, x + 20, y + 20, fill=color, outline="#228B22", width=2,tag="snake")  # Body

                # Draw scales (optional)
                self.canvas.create_arc(x + 5, y + 5, x + 15, y + 15,start=0, extent=180, fill="#228B22", outline="#228B22", tag="snake")  # Scales


        if self.check_collision():
            pygame.mixer.Sound.stop(self.background_music)
            self.game_over()
        else:
                if self.CURRENT < 500:
                    delay = 90
                elif self.CURRENT < 1000:
                    delay = 80
                elif self.CURRENT < 1500:
                    delay = 60
                elif self.CURRENT < 2000:
                    delay = 40
                elif self.CURRENT < 2500:
                    delay = 30
                elif self.CURRENT < 3000:
                    delay = 20
                else:
                    delay = 10

                self.after(delay,self.update_snake)

    def check_collision(self):
        head_x,head_y = self.snake[0]

        if head_x < 24 or head_x >= self.width - 31 or head_y < 29 or head_y >= self.height - 30:
            return True

        if (head_x,head_y) in self.snake[1:]:
            return True
        if len(self.snake) != len(set(self.snake)):
            return  True
        return  False

    def game_over(self):
        messagebox.showinfo(title="Game Over",message=f"You lost\nYour Score is : {self.CURRENT}")
        play_again = messagebox.askyesno(title="Play Again",message="Do you want to play Again ?")



        if play_again:
            self.restart_game()
            # insert the score to document in mongoDB
            mongo_collection = mongo_connection()

            query = mongo_collection.insert_one(
                {"Date": datetime.now().strftime("%m-%d-%y %H:%M:%S"), "Score": self.CURRENT})

            if (query):
                print("New Score just added go check it !")
            else:
                print("Not Yet")

        else:
            # insert the new score to mongoDB
            mongo_collection = mongo_connection()
            query = mongo_collection.insert_one(
                {"Date": datetime.now().strftime("%m-%d-%y %H:%M:%S"), "Score": self.CURRENT}
            )

            if (query):
                print("New Score just added go check it !")
            else:
                print("Not Yet")
            self.destroy()
            pygame.mixer.Sound.stop(self.background_music)
            welcome_snake.Welcome_snake().mainloop() # go to the welcome page







    def restart_game(self):
        self.CURRENT = 0
        self.score.config(text=f"Your Score : {self.CURRENT}")
        pygame.mixer.Sound.play(self.background_music)
        self.canvas.delete("snake")
        self.canvas.delete("food")
        self.food = self.create_food()
        self.snake = [(40, 40), (30, 40), (20, 40)]
        self.direction = "Right"
        self.update_snake()


if __name__ == "__main__":
    Snake().mainloop()
