import pgzrun
from random  import randint

WIDTH = 600
HEIGHT = 500

SCORE = 0
gameover = False

bee = Actor("bee")
bee.pos = 100, 100
#C:/Users/valim/Downloads/JetLearn/Python Game Developer

flower = Actor("flower")
flower.pos = 200, 200

def draw():
    screen.blit("background", (0, 0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score:" + str(SCORE), color = "black", topleft = (10, 10))

    if gameover:
        screen.fill("pink")
        screen.draw.text("Times up! Your final score is: "+ str(SCORE), 
                         midtop = (WIDTH/2, 10), fontsize = 40, color = "red")
        
def place_flower():
    flower.x = randint(70, (WIDTH-70))
    flower.y = randint(70, (HEIGHT-70))

def time_up():
    global gameover
    gameover = True

def update():
    global SCORE
    
    if keyboard.left:
        bee.x = bee.x-2
    
    if keyboard.right:
        bee.x = bee.x+2

    if keyboard.up:
        bee.y = bee.y-2

    if keyboard.down:
        bee.y = bee.y+2

    flower_collected = bee.colliderect(flower)

    if flower_collected:
        SCORE = SCORE+10
        place_flower()

clock.schedule(time_up, 60.0)

pgzrun.go()