from tkinter import *
import random
from tkinter import colorchooser,messagebox



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

        # Initialize game
        self.snake = [(40,40),(30,40), (20,40)]
        self.food = self.create_food()
        self.direction = "Right"
        self.segment_width = 14
        self.segment_height = 14
        self.bind("<KeyPress>",self.change_direction)
        self.update_snake()


    def center_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate X and Y
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height //2) - (self.height //2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def background(self, event):
        if event.keysym:
            color = colorchooser.askcolor()
            self.canvas.config(bg=color[1])
            print("You choosed :",color[1])

    def create_food(self):
        x = random.randint(0,(self.width // 12) -1)* 10
        y = random.randint(0, (self.height //12) -1)*10
        self.canvas.create_oval(x,y,x+10,y+10,fill="red",outline="red",tags="food")

        return (x,y)

    def change_direction(self,event):
        if event.keysym in ["Up","Down","Left","Right"]:
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
            self.food = self.create_food()

        else:
            self.snake.pop()

        self.canvas.delete("snake")

        # Customizing the snake: Different colors for head and body and adding eyes
        for index, (x, y) in enumerate(self.snake):
            if index == 0:
                color = "blue"  # Head color
                self.canvas.create_rectangle(x, y, x + 14, y + 17, fill=color, tag="snake")
                # Adding eyes to the head
                self.canvas.create_oval(x + 4, y + 2, x + 6, y + 6, fill="white", tag="snake")
                self.canvas.create_oval(x + 8, y + 2, x + 10, y + 6, fill="white", tag="snake")
            else:
                color = "green"  # Body color
                self.canvas.create_rectangle(x, y, x + 12, y + 17, fill=color, tag="snake")


        if self.check_collision():
            self.game_over()
        else:
            self.after(100,self.update_snake)

    def check_collision(self):
        head_x,head_y = self.snake[0]

        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            return True
        if len(self.snake) != len(set(self.snake)):
            return  True
        return  False

    def game_over(self):
        messagebox.showinfo(title="Game Over",message="You lost\nYour Score is : ")
if __name__ == "__main__":
    snake_game = Snake()
    snake_game.mainloop()