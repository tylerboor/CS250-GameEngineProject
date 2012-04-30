############################################################
# Author:				Tyler Boraski
# Date:				3/28
# Class:				CS 250 - Software Engineering
# Assignment:		Project
# Description:		This file runs the game's graphical engine.
############################################################

# ----- Import the self.pygame library and initialize it -----
import pygame
pygame.init()

# ----- Other libraries we wrote
import player
#import weapons
#import spells

# ----- Import other libraries -----
import time

# ----- Global variables -----
# Color variables
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
sand = (255, 230, 160)

class engine:
    def __init__(self):
        # Initialize the game engine
        self.pygame = pygame

        # Set the screen size, and open a window with a title
        size = [800,600]
        self.screen = self.pygame.display.set_mode(size)
        self.pygame.display.set_caption("CS250 Project - Tyler Boraski & Ryan Osbaldeston")

        # Initialize object that sets the screen's frame rate
        self.clock = self.pygame.time.Clock()
        # Setting the frame rate
        self.clock.tick(25)

        # This is a list of 'sprites.' Each enemy in the program is
        # added to this list.
        # The list is managed by a class called 'RenderPlain.'
        self.enemy_list = self.pygame.sprite.RenderPlain()

        # This is a list of every sprite.
        # All entities.
        self.all_sprites_list = self.pygame.sprite.RenderPlain()
    
    def environment(self):
        # Allow buttons to be held down
        self.pygame.key.set_repeat(1, 25)
        
        # Initialize test enemy
        enemyImage = "images/player-DOWN.png"
        self.enemy = player.Player("Wytch", enemyImage, 30, 30)
        self.all_sprites_list.add(self.enemy)   # Add the enemy to the list of objects
        self.enemy_list.add(self.enemy)         # Add the enemy to the list of enemies
        self.enemy.rect.x = 200
        self.enemy.rect.y = 200
        enemyDirection = "UP"
        speedCounter = 0
        
        while True:            
            # Draw background
            self.screen.fill(white)
            self.pygame.draw.rect(self.screen,black,[5,5,790,590],0)

            # Draw initial testing environment
            self.pygame.draw.rect(self.screen,sand,[20,20,760,560],0)
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,black)
            self.screen.blit(mousePos, [10,10])
            
            if enemyDirection == "UP" and speedCounter % 15 == 0:
                if self.enemy.rect.y > 100:
                    self.enemy.rect.y = self.enemy.rect.y - 1
                else:
                    enemyDirection = "DOWN"
            elif enemyDirection == "DOWN" and speedCounter % 15 == 0:
                if self.enemy.rect.y < 500:
                    self.enemy.rect.y = self.enemy.rect.y + 1
                else:
                    enemyDirection = "UP"
            speedCounter += 1
            
            if speedCounter > 15:
                speedCounter = 0
            
            # Listen for keyboard events				
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN:
                    # Movement keys
                    if event.key == self.pygame.K_UP and self.player.rect.y > 20:
                        self.player.rect.y = self.player.rect.y - 5
                    if event.key == self.pygame.K_DOWN and self.player.rect.y < 540:
                        self.player.rect.y = self.player.rect.y + 5
                    if event.key == self.pygame.K_LEFT and self.player.rect.x > 20:
                        self.player.rect.x = self.player.rect.x - 5
                    if event.key == self.pygame.K_RIGHT and self.player.rect.x < 755:
                        self.player.rect.x = self.player.rect.x + 5
                        
                    # Action keys
                    if event.key == self.pygame.K_SPACE:
                        # actionHandler needs to be implemented
                        continue
                        
                    # Inveory key 
                    if event.key == self.pygame.K_i:
                        # inventoryHandler needs to be implemented which includes spells as well
                        continue
                        
                    # Escape key back to the main menu
                    if event.key == self.pygame.K_ESCAPE:
                        self.mainMenu()
                elif event.type == self.pygame.KEYUP:
                    continue
            # Draw character				
            self.all_sprites_list.draw(self.screen)

            # Update the screen with what we've drawn.
            self.pygame.display.flip()
            self.pygame.event.pump()            

    def classSelection(self):
        while True:            
            # Draw background
            self.screen.fill(blue)
            self.pygame.draw.rect(self.screen,black,[100,100,600,400],2)
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,black)
            self.screen.blit(mousePos, [10,10]) 
            
            titleFont = self.pygame.font.Font(None, 60)
            titleFont.set_underline(True)
            title = titleFont.render("Class Selection",True,black)
            self.screen.blit(title, [240,130])
            
            # instructions for choosing a class
            instructFont = self.pygame.font.Font(None, 20)
            instructions = instructFont.render("Arrow keys to choose, enter to select",True,black)
            self.screen.blit(instructions, [280,480])
            
            # Draw options
            optionFont = self.pygame.font.Font(None, 40)
            optionText = optionFont.render("Wanderer",True,black)
            self.screen.blit(optionText, [330,300])
            
            # Listen for keyboard events
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_RETURN:
                        # Initialize the player entity
                        playerImage = "images/player-DOWN.png"
                        self.player = player.Player("Wanderer", playerImage, 30, 30)
                        self.all_sprites_list.add(self.player) # Add the player to the list of objects
                        self.player.rect.x = 385
                        self.player.rect.y = 285
                        self.environment()
                        
            # Update the screen with what we've drawn.
            self.pygame.display.flip()
            self.pygame.event.pump()
        
    def mainInstructionMenu(self):
        while True:            
            # Draw background
            self.screen.fill(blue)
            self.pygame.draw.rect(self.screen,black,[100,100,600,400],2)
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,black)
            self.screen.blit(mousePos, [10,10]) 
            
            # Draw text
            instructFont = self.pygame.font.Font(None, 60)
            instructFont.set_underline(True)
            instructTitle = instructFont.render("Instructions",True,black)
            self.screen.blit(instructTitle, [270,130])
            bodyFont = self.pygame.font.Font(None, 20)
            body = bodyFont.render("Insert all instructions here",True,black)
            self.screen.blit(body, [120,200])				
            
            # Listen for keyboard events
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_RETURN or event.key == self.pygame.K_ESCAPE or event.key == self.pygame.K_BACKSPACE:
                        self.mainMenu()
                        
            # Update the screen with what we've drawn.
            self.pygame.display.flip()
            self.pygame.event.pump()
        
    def mainMenu(self):
        # Disable key repeat
        self.pygame.key.set_repeat()
        
        # Setup option variables to handle selecting options on main menu
        optionNum = 1
        
        # Initialize coordinate variables for the shield
        shieldX = 290
        shieldY = 190
        
        while True:
            # Draw background
            self.screen.fill(blue)
            self.pygame.draw.rect(self.screen,black,[100,100,600,400],2)
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,black)
            self.screen.blit(mousePos, [10,10]) 
            
            # Draw background
            titleFont = self.pygame.font.Font(None, 60)
            titleFont.set_underline(True)
            title = titleFont.render("Tyler and Ryan's Game",True,black)
            self.screen.blit(title, [160,130])
            optionFont = self.pygame.font.Font(None, 40)
            option1text = optionFont.render("New Game",True,black)
            option2text = optionFont.render("Instructions",True,black)
            option3text = optionFont.render("Exit",True,black)
            self.screen.blit(option1text, [380,220])
            self.screen.blit(option2text, [380,300])
            self.screen.blit(option3text, [380,380])
        
            # Draw shield
            shield = self.pygame.image.load("images/Shield.png")
            shieldPos = [shieldX, shieldY]
            self.screen.blit(shield, shieldPos)
            
            # Listen for keyboard events
            for event in self.pygame.event.get():
                # Moving the shield icon with UP and DOWN arrow keys
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_UP and shieldY > 190:
                        shieldY = shieldY - 80
                        optionNum = optionNum - 1
                    if event.key == self.pygame.K_DOWN and shieldY < 350:
                        shieldY = shieldY + 80
                        optionNum = optionNum + 1
                    # Pressing ENTER to select and option
                    if event.key == self.pygame.K_RETURN:
                        if optionNum == 1:
                            self.classSelection()
                        elif optionNum == 2:
                            self.mainInstructionMenu()
                        elif optionNum == 3:
                            self.pygame.quit()
                            exit()
                            
            # Update the screen with what we've drawn.
            self.pygame.display.flip()
            self.pygame.event.pump()
        
if __name__ == "__main__":
    E = engine()
    E.mainMenu()