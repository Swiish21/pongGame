import tkinter as tk
import random

class PongGame:
    def __init__(self, master):
        # Initialize the game window
        self.master = master
        self.master.title("Pong Game")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="black")
        self.canvas.pack()
        
        # Create paddles and ball
        self.pad1 = self.canvas.create_rectangle(20, 150, 40, 250, fill="white")
        self.pad2 = self.canvas.create_rectangle(560, 150, 580, 250, fill="white")
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        
        # Ball speed
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        
        # Scores
        self.score1 = 0
        self.score2 = 0
        self.score_display = self.canvas.create_text(300, 20, text="0 : 0", fill="white", font=("Arial", 24))
        
        # Key bindings for paddle movement
        self.master.bind("<KeyPress-Up>", self.move_pad2_up)
        self.master.bind("<KeyPress-Down>", self.move_pad2_down)
        self.master.bind("<KeyPress-w>", self.move_pad1_up)
        self.master.bind("<KeyPress-s>", self.move_pad1_down)
        
        # Start the game loop
        self.game_loop()

    def move_pad1_up(self, event):
        # Move left paddle up
        if self.canvas.coords(self.pad1)[1] > 0:
            self.canvas.move(self.pad1, 0, -20)

    def move_pad1_down(self, event):
        # Move left paddle down
        if self.canvas.coords(self.pad1)[3] < 400:
            self.canvas.move(self.pad1, 0, 20)

    def move_pad2_up(self, event):
        # Move right paddle up
        if self.canvas.coords(self.pad2)[1] > 0:
            self.canvas.move(self.pad2, 0, -20)

    def move_pad2_down(self, event):
        # Move right paddle down
        if self.canvas.coords(self.pad2)[3] < 400:
            self.canvas.move(self.pad2, 0, 20)

    def game_loop(self):
        # Move the ball
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        ball_pos = self.canvas.coords(self.ball)
        
        # Ball hits top or bottom wall
        if ball_pos[1] <= 0 or ball_pos[3] >= 400:
            self.ball_speed_y *= -1
        
        # Ball is out of bounds
        if ball_pos[0] <= 0:
            self.score2 += 1
            self.update_score()
            self.restart_game()
        elif ball_pos[2] >= 600:
            self.score1 += 1
            self.update_score()
            self.restart_game()
        
        # Ball hits paddle
        if self.check_collision(self.pad1) or self.check_collision(self.pad2):
            self.ball_speed_x *= -1
        
        # Continue the game loop
        self.master.after(20, self.game_loop)

    def check_collision(self, pad):
        # Check if the ball collides with a paddle
        ball_pos = self.canvas.coords(self.ball)
        pad_pos = self.canvas.coords(pad)
        if (ball_pos[0] <= pad_pos[2] and ball_pos[2] >= pad_pos[0] and
            ball_pos[1] <= pad_pos[3] and ball_pos[3] >= pad_pos[1]):
            return True
        return False

    def restart_game(self):
        # Restart the game by resetting the ball position and speed
        self.canvas.coords(self.ball, 290, 190, 310, 210)
        self.ball_speed_x = random.choice([-5, 5])
        self.ball_speed_y = random.choice([-5, 5])

    def update_score(self):
        # Update the score display
        self.canvas.itemconfig(self.score_display, text=f"{self.score1} : {self.score2}")

def main():
    # Create the main window and start the game
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()