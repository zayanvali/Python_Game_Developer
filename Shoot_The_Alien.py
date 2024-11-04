from random import randint
import pgzrun

TITLE = "Shoot the Alien"
WIDTH = 500
HEIGHT = 500
alien = Actor("alien")
message = ""

def draw():
    screen.clear()
    screen.fill(color = (0, 0, 255))

    alien.draw()
    screen.draw.text(message, center = (400, 10), fontsize = 30)

def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "GOOD SHOT!"
        place_alien()

    else:
        message = "YOU MISSED!"
        place_alien()

pgzrun.go()