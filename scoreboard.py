from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		file = open("Highest_score.txt","r")
		self.high_score = int(file.read())
		self.color("white")
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.update_scoreboard()
		file.close()


	def update_scoreboard(self):
		self.clear()
		self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=FONT)

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()


	# def Game_Over(self):
	# 	self.goto(0,0)
	# 	self.write("GAME OVER", align= ALIGNMENT, font= FONT)

	def reset(self):
		if self.score > int(self.high_score):
			self.high_score = self.score
			with open("Highest_score.txt", "w") as file:
				file.write(f"{self.high_score}")
		self.score = 0
		self.update_scoreboard()

