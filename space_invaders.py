import turtle
import os
import math
import random
import subprocess

#Set up the screen

win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.bgcolor("#0F056b")
#win.bgpic("space_invaders_background.gif")

#Register the graphics for the game
#turtle.register_shape("turtle")
turtle.register_shape("images/player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
  border_pen.fd(600)
  border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score on stage
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(290,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="right", font = ("Arial", 14, "bold"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("images/player.gif")
player.speed(0)
player.penup()
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose number of enemies
number_of_enemies = 5

#Create an empty list of enemies
enemiesList = []

#Add enemies to the list
#We need to create more turtle objects

for i in range(number_of_enemies):
  #Create the enemy
  enemiesList.append(turtle.Turtle())

for enemy in enemiesList:
  enemy.color("#FFFFFF")
  randi = random.randint(1,10)
  if(randi >= 1 and randi < 8):
    enemy.shape("square")#normal block neutral
  if(randi == 8):
    enemy.shape("turtle")#decline bullet's speed
  if(randi == 9):
    enemy.shape("circle")#decline player movement speed
  if(randi == 10):
    enemy.shape("triangle")#increase enemy movement speed
  enemy.speed(0)
  enemy.penup()
  x = random.randint(-200, 200)
  y = random.randint(100, 200)
  enemy.setposition(x, y)

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30

#Define bullet state
#we have 2 states:
#ready - ready to fire bullet
#fire - bullet is firing

bulletstate = "ready"

#Move the player left and right

def move_left():
  x = player.xcor()
  x = x - playerspeed
  if x < -280:
    x = -280
  player.setx(x)

def move_right():
  x = player.xcor()
  x = x + playerspeed
  if x > 280:
    x = 280
  player.setx(x)

def fire_bullet():
  #Declare bulletstate as a global if it needs change
  global bulletstate
  if bulletstate == "ready":
    #Move the bullet to just above the player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x,y)
    bullet.showturtle()
    bulletstate = "fire"


def isCollision(t1,t2):
  distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
  if distance < 20:
    return True
  else:
    return False



#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


gameover = False

#Main game loop
while gameover == False:
  for enemy in enemiesList:
    #This is a forever loop
    #Move the enemy
    x = enemy.xcor()
    x = x + (enemyspeed * 2)
    enemy.setx(x)

    #Move enemy back and down
    if enemy.xcor() > 280:
     for enemy in enemiesList:
          enemyspeed =  enemyspeed * -1
          y = enemy.ycor()
          y = y - 40
          enemy.sety(y)
    if enemy.xcor() < -280:
     for enemy in enemiesList:
          enemyspeed =  enemyspeed * -1
          y = enemy.ycor()
          y = y - 40
          enemy.sety(y)

    if enemy.ycor() < -300:
     for enemy in enemiesList:
         gameover = True

    #Check for collision between bullet and enemy
    if isCollision(bullet, enemy):
      #Reset the bullet
      test = enemy.shape()
      if(test == "turtle"):
          print("#decline bullet's speed ")
          if(bulletspeed > 10):
              bulletspeed -= 1
      if(test == "circle"):
          print("#decline player movement speed")
          if(playerspeed > 5):
            playerspeed -= 0.1
      if(test == "triangle"):
          print("#increase enemy movement speed")
          enemyspeed += 0.1

      bullet.hideturtle()
      bulletstate = "ready"
      bullet.setposition(0, -400)
      #Reset the enemy
      x = random.randint(-200, 200)
      y = random.randint(100, 200)
      enemy.setposition(x, y)
      #Update the score
      score += 10
      scorestring = "Score: %s" %score
      score_pen.clear()
      score_pen.write(scorestring, False, align="right", font = ("Arial", 14, "bold"))

    #Check for collision between enemy and player
    if isCollision(player, enemy) :
      player.hideturtle()
      enemy.hideturtle()
      print("GAME OVER")
      gameover = True
      break

  #Move the bullet only when bulletstate is "fire"
  if bulletstate == "fire":
    y = bullet.ycor()
    y = y + bulletspeed
    bullet.sety(y)

  #Check to see if bullet has reached the top
  if bullet.ycor() > 275:
    bullet.hideturtle()
    bulletstate = "ready"

  if (gameover == True):
    gameover_pen = turtle.Turtle()
    gameover_pen.hideturtle()
    gameover_pen.goto(5, 2)
    gameover_pen.color("white")
    gameover_pen.write("GAME OVER ! \n", font=("Arial",25,"normal"), align="center")
    gameover_pen.write("Cliquez pour continuer", font=("Arial",11,"normal"), align="center")
    win.exitonclick()
    subprocess.run('python accueil.py')
