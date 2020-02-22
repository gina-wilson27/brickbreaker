# Pragnya Pandrate (pp8sdv) and Gina Wilson (vw8fn)
# enemies, collectibles, health bar, and different levels

# Main objective: The objective of our game is to model the Brickbreaker game. This game involves starting with bricks
# and a paddle that a ball bounces off of. The paddle moves based on user input and the ball bounces of the paddle when
# they collide.
# When the ball hits the brick the brick disappears.
# If the ball hits an enemy, a life is lost
# There are gold coins that the user can collect that will give a higher score.
# The aim of the game is to make all the bricks disappear. If the ball misses the paddle, then you lose one life.
# You are given three lives until the game ends.

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

game_on = False

# Create a start screen
camera.draw('Students: Pragnya Pandrate (pp8sdv) and Gina Wilson (vw8fn)', 20, 'white', 400, 50)
camera.draw('Instructions: The objective of the game is to get rid of all the bricks.', 20, "white", 400, 250)
camera.draw('Move the paddle at the bottom of the screen from left to right using the arrow keys in order to bounce the'
            , 20, "white", 400, 300)
camera.draw('ball off of the paddle. When the ball hits the brick it will disappear. Hitting a coin will give you more '
            'points .', 20, "white", 400, 350)
camera.draw('If the ball misses the paddle you lose one life. Hitting a white enemy will subtract a single life.',
            20, 'white', 400, 400)
camera.draw('Levels progress as the bricks disappear. At each level, a new enemy will spawn. Touching a green enemy'
            'will end the game',
            20, 'white', 400, 450)
camera.draw('If you lose all three lives, the game is over.', 20, 'white', 400, 500)

# Create a character called paddle.
paddle = gamebox.from_color(400, 500, "red", 50, 10)

# There is a character called ball that bounces off of the paddle.
ball = gamebox.from_color(400, 490, "blue", 10, 10)

# Initial ball velocity


ball.yspeed += 2
ball.xspeed += 2


# Create walls
right_wall = gamebox.from_color(775, 300, "red", 50, 600)
left_wall = gamebox.from_color(25, 300, "red", 50, 600)
top_wall = gamebox.from_color(400, 25, "red", 800, 50)

# Create global brick counter
number_of_bricks = 15

# Create characters that are bricks of the same size.
bricks = [
    gamebox.from_color(250, 100, "red", 70, 10),
    gamebox.from_color(325, 100, "red", 70, 10),
    gamebox.from_color(400, 100, "red", 70, 10),
    gamebox.from_color(475, 100, "red", 70, 10),
    gamebox.from_color(550, 100, "red", 70, 10),
    gamebox.from_color(250, 120, "red", 70, 10),
    gamebox.from_color(325, 120, "red", 70, 10),
    gamebox.from_color(400, 120, "red", 70, 10),
    gamebox.from_color(475, 120, "red", 70, 10),
    gamebox.from_color(550, 120, "red", 70, 10),
    gamebox.from_color(250, 140, "red", 70, 10),
    gamebox.from_color(325, 140, "red", 70, 10),
    gamebox.from_color(400, 140, "red", 70, 10),
    gamebox.from_color(475, 140, "red", 70, 10),
    gamebox.from_color(550, 140, "red", 70, 10),
]

# health bar
healthbar = gamebox.from_color(400, 75, "green", 100, 10)

# Creating Enemies

enemy1 = gamebox.from_color(150, 175, "white", 20, 20)
enemy2 = gamebox.from_color(650, 350, "white", 20, 20)
enemy3 = gamebox.from_color(200, 350, "green", 20, 20)
enemy4 = gamebox.from_color(600, 350, "green", 20, 20)

enemy1.xspeed += 2

enemy2.xspeed += 2

enemy3.yspeed += 2

enemy4.yspeed += 2


# Creating Collectables

depth1 = random.randint(160, 400)
depth2 = random.randint(160, 400)
depth3 = random.randint(160, 400)
depth4 = random.randint(160, 400)

collectables = [
    gamebox.from_color(150, depth1, "yellow", 10, 10),
    gamebox.from_color(400, depth2, "yellow", 10, 10),
    gamebox.from_color(450, depth3, "yellow", 10, 10),
    gamebox.from_color(600, depth4, "yellow", 10, 10),
]

# Create a global live counter
lives = 3
number_of_touches = 0
level = 1
score = 0




def tick(keys):
    global number_of_bricks, game_on, lives, score, number_of_touches, level

    # We use user input in order to move the paddle left to right.
    if pygame.K_SPACE in keys:
        game_on = True

    if game_on is True:
        # This will cause the ball to move up
        ball.y -= ball.yspeed
        ball.x -= ball.xspeed

        # This makes the enemies start moving
        enemy1.x += enemy1.xspeed
        enemy2.x += enemy2.xspeed
        # If the right key is pressed and the ball collides with the paddle it bounces off of at 45 degrees to the left.
        if pygame.K_RIGHT in keys and paddle.touches(right_wall) is False:
            paddle.move(10, 0)

        if pygame.K_LEFT in keys and paddle.touches(left_wall) is False:
            paddle.move(-10, 0)

        # If the paddle is in the middle of the screen the ball bounces straight up.
        if paddle.x == 400 and ball.touches(paddle):
            ball.yspeed -= 0.5

        # If the ball hits the left wall as it goes up the ball should bounce 45 degrees to the right.
        if ball.touches(left_wall) and ball.yspeed < 0:
            ball.move_to_stop_overlapping(left_wall)
            ball.xspeed *= -1

        # If the ball hits the left wall as it goes up the ball should bounce 45 degrees to the right.
        if ball.touches(left_wall) and ball.yspeed > 0:
            ball.move_to_stop_overlapping(left_wall)
            ball.xspeed *= -1

        # If the ball hits the right wall as it goes up the ball should bounce 45 degrees to the left.
        if ball.touches(right_wall) and ball.yspeed < 0:
            ball.move_to_stop_overlapping(right_wall)
            ball.xspeed *= -1

        # If the ball hits the right wall as it goes up the ball should bounce 45 degrees to the left.
        if ball.touches(right_wall) and ball.yspeed > 0:
            ball.move_to_stop_overlapping(right_wall)
            ball.xspeed *= -1

        # If the ball hits the right wall as it goes down the ball should bounce 45 degrees to the left.
        if ball.touches(top_wall):
            ball.move_to_stop_overlapping(top_wall)
            ball.yspeed *= -1


        # if the ball touches the paddle, it will reverse
        if ball.touches(paddle):
            ball.move_to_stop_overlapping(paddle)
            ball.yspeed *= -1

        # if enemy1 touches a wall, it will reverse its speed in the x direction
        if enemy1.touches(right_wall):
            enemy1.move_to_stop_overlapping(right_wall)
            enemy1.speedx *= -1
        # if enemy1 touches a wall, it will reverse its speed in the x direction
        if enemy1.touches(left_wall):
            enemy1.move_to_stop_overlapping(left_wall)
            enemy1.speedx *= -1
        # if enemy2 touches a wall, it will reverse its speed in the x direction
        if enemy2.touches(right_wall):
            enemy2.move_to_stop_overlapping(right_wall)
            enemy2.speedx *= -1
        # if enemy2 touches a wall, it will reverse its speed in the x direction
        if enemy2.touches(left_wall):
            enemy2.move_to_stop_overlapping(left_wall)
            enemy2.speedx *= -1

        # if the ball touches an enemy, the player loses a life and the ball is reset
        if ball.touches(enemy1):
            ball.move_to_stop_overlapping(enemy1)
            ball.speedy *= -1
            lives -= 1

        # if the ball touches an enemy, the player loses a life and the ball is reset
        if ball.touches(enemy2):
            ball.move_to_stop_overlapping(enemy2)
            ball.speedy *= -1
            lives -= 1

        if ball.touches(enemy3):
            ball.move_to_stop_overlapping(enemy3)
            ball.speedy *= -1
            lives -= 1

        if ball.touches(enemy4):
            ball.move_to_stop_overlapping(enemy4)
            ball.speedy *= -1
            lives -= 1

        camera.clear("black")
        camera.draw(gamebox.from_text(700, 75, "Level: " + str(level), 25, "Orange", bold=False))
        camera.draw(gamebox.from_text(100, 75, "Score: " + str(score), 25, "Orange", bold=False))
        camera.draw(paddle)
        camera.draw(ball)
        camera.draw(right_wall)
        camera.draw(left_wall)
        camera.draw(top_wall)
        camera.draw(enemy1)
        camera.draw(enemy2)
        camera.draw(healthbar)

        for collectable in collectables:
            if ball.touches(collectable) == False:
                camera.draw(collectable)
            else:
                collectables.remove(collectable)
                score += 50

        for brick in bricks:
            if ball.touches(brick) is False:
                camera.draw(brick)
            else:
                score += 10
                number_of_bricks -= 1
                bricks.remove(brick)

        if number_of_bricks <= 10:
            level = 2
            camera.draw(enemy3)
            enemy3.y += enemy3.yspeed
            if enemy3.y == 150:
                enemy3.speedy *= -1
            if enemy3.y == 590:
                enemy3.speedy *= -1


        if number_of_bricks <= 5:
            level = 3
            camera.draw(enemy4)
            enemy4.y += enemy4.yspeed
            if enemy4.y == 150:
                enemy4.speedy *= -1
            if enemy4.y == 590:
                enemy4.speedy *= -1



        # If the ball does not collide with the paddle or goes off the bottom part of the screen, subtract a life.
        if ball.y >= 600:
            camera.draw(gamebox.from_text(400, 200, "You Lose!", 100, "Yellow", bold=False))
            lives = 0
            enemy1.speedx = 0
            enemy1.speedy = 0
            enemy2.speedx = 0
            enemy2.speedy = 0
            healthbar.size = [0, 10]
            paddle.size = [0, 0]

        if lives == 2:
            healthbar.size = [66, 10]

        if lives == 1:
            healthbar.size = [33, 10]

        # If there are zero lives stop the game and display game over.
        if lives == 0:
            camera.draw(gamebox.from_text(400, 200, "You Lose!", 100, "Yellow", bold=False))
            enemy1.speedx = 0
            enemy1.speedy = 0
            enemy2.speedx = 0
            enemy2.speedy = 0
            enemy3.speedx = 0
            enemy3.speedy = 0
            enemy4.speedx = 0
            enemy4.speedy = 0
            ball.speedx = 0
            ball.speedy = 0
            ball.size = [0, 0]
            healthbar.size = [0, 10]
            paddle.size = [0, 0]


        # Draw methods:
        # Draw the walls, ball, paddle, and bricks.
        # Check for win:
        # If brick counter is 0, display "you win!"
        if number_of_bricks == 0:
            camera.draw(gamebox.from_text(400, 200, "You Win!", 100, "Yellow", bold=False))
            game_on = False

    # Display screen
    camera.display()

ticks_per_second = 60

# invokes the function
gamebox.timer_loop(ticks_per_second, tick)





