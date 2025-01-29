# 🐍 Snake Game

## 🌟 Description
Dive into the classic Snake game experience, enhanced with Python's Tkinter library for a dynamic GUI and Pygame library for soothing background music. Challenge yourself as the game speed intensifies with your increasing score!

## 🚀 Features
- **Classic Snake Gameplay**: Navigate the snake using the arrow keys and gobble up food to grow longer.
- **Increasing Speed**: Watch as the snake's speed ramps up based on your score.
- **Background Music**: Enjoy a calm and serene soundtrack while you play.

## 🎮 How to Play
- Run the `snake_game.py` file to start the game.
- Use the arrow keys to steer the snake.
- Collect food to rack up points and grow your snake.
- Avoid crashing into walls or the snake's own body.

## 🧩 Code Highlights
The game speed accelerates as you score more points:
```python
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

self.after(delay, self.update_snake)
```
## 🙏 Acknowledgements
+ #### Pygame
+ #### Tkinter