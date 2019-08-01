import pygame
pygame.init()
import random
import time

#setting the display_width and display_height 
# also setting car height and width
display_width = 600
display_height = 600
car_width = 20
car_height = 22

#setting rgb values
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
blue  = (0,0,255)

#initialising score
score = 0

#setting game display container
gameDisplay = pygame.display.set_mode((display_width, display_height))

#setting the caption
pygame.display.set_caption('Dodge the block')

#setting the clock to handle fps in future
clock = pygame.time.Clock()

#loading car file
carImg = pygame.image.load('C:/Users/Akash/Desktop/racecar3.png')

#setting car pos values
x =  (display_width * 0.45)
y =  (display_height * 0.80)

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#creating random values
object_width = 30
object_height = 30
object_startx = random.randrange(0, display_width)   
object_starty = random.randrange(0, display_height)


fruit_startx = random.randrange(0, display_width)
fruit_starty = random.randrange(0, display_height)
fruit_width = 35
fruit_height = 35


#defining objects
def object(object_startx, object_starty, object_width, object_height, color):
	pygame.draw.rect(gameDisplay, color, [object_startx, object_starty, object_width, object_height])

def fruit(fruit_startx, fruit_starty, fruit_width, fruit_height, color):
	pygame.draw.rect(gameDisplay, color, [fruit_startx, fruit_starty, fruit_width, fruit_height])

#creating two lists for blocks to be drawn
box_coords = []

while len(box_coords)!=15:
	object_startx = random.randrange(0, display_width)
	object_starty = random.randrange(0, display_height)
	if not (x < (object_startx + object_width) and x+car_width > object_startx and y+car_height > object_starty and y < (object_starty+object_height)):
		box_coords.append((object_startx,object_starty))	

#logic
gameover = False
x_change =0
y_change =0

while not gameover:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = True

		if x  > display_width-car_width:
			gameover = True

		if x < 0:
			gameover = True

		if y < 0:
			gameover = True

		if y > display_height-car_height:
			gameover = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -2

			if event.key == pygame.K_RIGHT:
				x_change = 2

			if event.key == pygame.K_UP:
				y_change = -2

			elif event.key == pygame.K_DOWN:
				y_change = 2

		elif event.type == pygame.KEYUP:
			x_change=0
			y_change=0

	x= x+x_change
	y= y+y_change

	gameDisplay.fill(green)
	car(x,y)

#calling fruit for first time	
	fruit(fruit_startx, fruit_starty, fruit_width, fruit_height, blue)

#drawing fruit every next when user hits one
	if x < (fruit_startx + fruit_width) and x + car_width > fruit_startx and y+car_height > fruit_starty and y < (fruit_starty+fruit_height):
		fruit_startx = random.randrange(0, display_width)
		fruit_starty = random.randrange(0, display_height)
		score = score+1
	
		# print('fruit start x value is  {}, fruit start y value is {}'.format(fruit_startx, fruit_starty))

#checking collision
	for box in box_coords:
		object_startx,object_starty = box
		object(object_startx, object_starty, object_width, object_height, black)
		if x < (object_startx + object_width) and x+car_width > object_startx and y+car_height > object_starty and y < (object_starty+object_height):
			gameover = True

#updating
	pygame.display.update()
	clock.tick(100)
print("your score is {}".format(score))
pygame.quit()
quit()