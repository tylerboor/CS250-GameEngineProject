############################################################
# Author:		Tyler Boraski
# Date:			3/28
# Class:		CS 250 - Software Engineering
# Assignment:	Project
# Description	This file runs the game's graphical engine.
############################################################

# ----- Import the pygame library -----
import pygame

# ----- Import other libraries -----
import time

# ----- Global variables -----
# Color variables
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
sand = (255, 230, 160)


class Player(pygame.sprite.Sprite):
	# Initialize the player sprite
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(black)
		self.rect = self.image.get_rect()

class engine:
	def main():
		# Initialize the game engine
		pygame.init()

		# Set the screen size, and open a window with a title
		size = [800,600]
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("CS250 Project - Tyler Boraski & Ryan Osbaldeston")
		
		# Allow buttons to be held down
		pygame.key.set_repeat(1, 50)
		
		# Loop until the user clicks the close button
		done = False
		
		# Initialize object that sets the screen's frame rate
		clock = pygame.time.Clock()
		
		# Initialize coordinate variables for the shield
		shieldX = 290
		shieldY = 190
		
		# Initialize game state
		# 0 = The game is at the main menu
		# 1 = The game is being played
		gameState = 0
		
		# Setup option variables to handle selecting options on main menu
		optionNum = 1
		
		# Instruction page variable
		instructPage = False
		
		# Image variables
		shield = pygame.image.load("images/Shield.png")
		
		# Initialize the player entity
		player = Player(black, 30, 30)
		player.rect.x = 385
		player.rect.y = 285
		
		# This is a list of 'sprites.' Each entity in the program is
		# added to this list.
		# The list is managed by a class called 'RenderPlain.'
		enemy_list = pygame.sprite.RenderPlain()
		
		# This is a list of every sprite.
		# All entities.
		all_sprites_list = pygame.sprite.RenderPlain()
		
		# Add the player to the list of objects
		all_sprites_list.add(player)
		
		
		
		# ----- Main Program Loop -----
		while done == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
			
			# Setting the frame rate
			clock.tick(60)
			
			# Draw the position of the mouse for debugging and such
			mouseCoordinates = pygame.mouse.get_pos()
			mouseFont = pygame.font.Font(None, 14)
			mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,black)
			
			# Handle the game states
			if gameState == 0:
			
				# ----- Menu -----
				
				# Draw background
				screen.fill(blue)
				pygame.draw.rect(screen,black,[100,100,600,400],2)
				
				# Mouse position for debugging
				mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,black)
				screen.blit(mousePos, [10,10]) 
				
				# Main menu
				if instructPage == False:
					# Draw background
					titleFont = pygame.font.Font(None, 60)
					titleFont.set_underline(True)
					title = titleFont.render("Tyler and Ryan's Game",True,black)
					screen.blit(title, [160,130])
					optionFont = pygame.font.Font(None, 40)
					option1text = optionFont.render("New Game",True,black)
					option2text = optionFont.render("Instructions",True,black)
					option3text = optionFont.render("Exit",True,black)
					screen.blit(option1text, [380,220])
					screen.blit(option2text, [380,300])
					screen.blit(option3text, [380,380])
				
					# Draw shield				
					shieldPos = [shieldX, shieldY]
					screen.blit(shield, shieldPos)
					
					# Listen for keyboard events
					for event in pygame.event.get():
						# Moving the shield icon with UP and DOWN arrow keys
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_UP and shieldY > 190:
								shieldY = shieldY - 80
								optionNum = optionNum - 1
							if event.key == pygame.K_DOWN and shieldY < 350:
								shieldY = shieldY + 80
								optionNum = optionNum + 1
							# Pressing ENTER to select and option
							if event.key == pygame.K_RETURN:
								if optionNum == 1:
									gameState = 1
								elif optionNum == 2:
									instructPage = True
								elif optionNum == 3:
									pygame.quit()
									exit()
				# Instruction screen
				else:
					# Draw background
					instructFont = pygame.font.Font(None, 60)
					instructFont.set_underline(True)
					instructTitle = instructFont.render("Instructions",True,black)
					screen.blit(instructTitle, [270,130])
					bodyFont = pygame.font.Font(None, 20)
					body = bodyFont.render("Insert all instructions here",True,black)
					screen.blit(body, [120,200])				
					
					# Listen for keyboard events
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
								instructPage = False
					
			elif gameState == 1:
			
				# ----- Game Environment -----
				
				# Draw background
				screen.fill(white)
				pygame.draw.rect(screen,black,[5,5,790,590],0)
				
				# Mouse position for debugging
				mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,white)
				screen.blit(mousePos, [10,10])
				
				# Draw initial testing environment
				pygame.draw.rect(screen,sand,[20,20,760,560],0)
				
				# Listen for keyboard events				
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						# Movement keys
						if event.key == pygame.K_UP and player.rect.y > 0 and player.rect.y < 570:
							player.rect.y = player.rect.y - 5
						if event.key == pygame.K_DOWN and player.rect.y > 0 and player.rect.y < 570:
							player.rect.y = player.rect.y + 5
						if event.key == pygame.K_LEFT and player.rect.x > 0 and player.rect.x < 770:
							player.rect.x = player.rect.x - 5
						if event.key == pygame.K_RIGHT and player.rect.x > 0 and player.rect.x < 770:
							player.rect.x = player.rect.x + 5
							
						# Action keys
						if event.key == pygame.K_SPACE:
							# actionHandler needs to be implemented
							
						# Inveory key 
						if event.key == pygame.K_i:
							# inventoryHandler needs to be implemented which includes spells as well
							
						# Escape key back to the main menu
						if event.key == pygame.K_ESCAPE:
							gameState = 0
					elif event.type == pygame.KEYUP:
						continue
				# Draw character				
				all_sprites_list.draw(screen)
			
			# Update the screen with what we've drawn.
			pygame.display.flip()
			pygame.event.pump()			
			
		# Exit the game
		print "Got HEREERERE"
		pygame.quit()

	if __name__ == "__main__":
		main()
		
class Player(pygame.sprite.Sprite):
	# Initialize the player sprite
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(black)
		self.rect = self.image.get_rect()