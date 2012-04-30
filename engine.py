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
import weapons
import spells
import attack

# ----- Import other libraries -----
import time

# ----- Global variables -----
# Color variables
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
sand = (255, 230, 160)

# Image variables
mainMenuImg = pygame.image.load("images/MainMenu.jpg").convert()
instructMenuImg = pygame.image.load("images/InstructionMenu.jpg").convert()
classSelectImg = pygame.image.load("images/ClassSelection.jpg").convert()
healthImg = pygame.image.load("images/small-check.png").convert()
healthImg.set_colorkey((255,255,255))
keyImg = pygame.image.load("images/key.png").convert()
keyImg.set_colorkey((255,255,255))
chestImg = pygame.image.load("images/chest.png").convert()
chestImg.set_colorkey((255,255,255))


class Item(pygame.sprite.Sprite):
    def __init__ (self, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if type == "health":
            self.image = healthImg
        if type == "chest":
            self.image = chestImg
        if type == "key":
            self.image = keyImg
        self.rect = self.image.get_rect()

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
        
        # Sprite list for items
        self.item_sprite_list = self.pygame.sprite.RenderPlain()
        
    def gameOver(self):
        while True:
            titleFont = self.pygame.font.Font(None, 80)
            gameOver = titleFont.render("Game Over",True,red)
            self.screen.blit(gameOver, [240,200])
            
            # Draw character				
            self.all_sprites_list.draw(self.screen)
            
            # Listen for keyboard events
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_RETURN or event.key == self.pygame.K_ESCAPE or event.key == self.pygame.K_BACKSPACE:
                        self.mainMenu()

            # Update the screen with what we've drawn.
            self.pygame.display.flip()
            self.pygame.event.pump()     
        
    def handleAttack(self, attacker, target, attack):
        targetHealth = self.computeDamageTaken(attacker, target, attack) # Get damage return for skill/power leveling (to be added)
        if targetHealth < 1:
            #attacker.points = attacker.points + self.player.addXP(target.level)
            # points can be used for leveling up
            target.remove(self.all_sprites_list)
            if target.type == "Wanderer":
                self.gameOver()
            if target.type == "Wytch":
                target.remove(self.enemy_list)

	
    def computeDamageTaken(self, attacker, target, attack):
        defending = False
        if attack.Type == "Active Spell":
            damage = attacker.player.getBasePowerDamage()*attack.modVal - target.player.getBaseDefenseVsMagic()
        elif attack.Type != "Passive Spell":
            if attack.modStat == "dex":
                if defending:
                    damage = attacker.player.getBaseDexSkillDamage()*attack.modVal - target.player.getBaseDefenseVsPhysical()*target.player.shield.modVal
                    # Modify Shield level here (to be added)
                else:
                    damage = attacker.player.getBaseDexSkillDamage()*attack.modVal - target.player.getBaseDefenseVsPhysical()
            else:
                if defending:
                    damage = attacker.player.getBaseStrSkillDamage()*attack.modVal - target.player.getBaseDefenseVsPhysical()*target.player.shield.modVal
                    # Modify Shield level here (to be added)
                else:
                    damage = attacker.player.getBaseStrSkillDamage()*attack.modVal - target.player.getBaseDefenseVsPhysical()
        if damage < 1:
            damage = 1
        if target.player.HP - damage < 1:
            target.player.HP = 0
        else:
            target.player.HP = target.player.HP - damage
        return target.player.HP
    
    def environment(self):
        # Allow buttons to be held down
        self.pygame.key.set_repeat(1, 25)
        
        # Initialize test enemies
        enemy1Image = "images/player-DOWN.png"
        enemy2Image = "images/player-LEFT.png"
        self.enemy1 = player.Player("Wytch", enemy1Image, 30, 30)
        self.enemy2 = player.Player("Wytch", enemy2Image, 30, 30)
        self.all_sprites_list.add(self.enemy1)   # Add the enemy to the list of objects
        self.all_sprites_list.add(self.enemy2)
        self.enemy_list.add(self.enemy1)         # Add the enemy to the list of enemies
        self.enemy_list.add(self.enemy2)
        self.enemy1.rect.x = 200
        self.enemy1.rect.y = 200
        self.enemy2.rect.x = 600
        self.enemy2.rect.y = 500
        enemy1Direction = "UP"
        enemy2Direction = "LEFT"
        speedCounter = 0
        
        # Initial test items
        self.health = Item("health")
        self.item_sprite_list.add(self.health)
        self.health.rect.x = 600
        self.health.rect.y = 200
        self.health2 = Item("health")
        self.item_sprite_list.add(self.health2)
        self.health2.rect.x = 500
        self.health2.rect.y = 100
        self.health3 = Item("health")
        self.item_sprite_list.add(self.health3)
        self.health3.rect.x = 600
        self.health3.rect.y = 100
        self.chest = Item("chest")
        self.item_sprite_list.add(self.chest)
        self.chest.rect.x = 300
        self.chest.rect.y = 400
        self.key = Item("key")
        self.key.rect.x = 340
        self.key.rect.y = 400
        
        while True:            
            # Draw background
            self.screen.fill(white)
            self.pygame.draw.rect(self.screen,black,[5,5,790,590],0)

            # Draw initial testing environment
            self.pygame.draw.rect(self.screen,sand,[20,20,760,560],0)
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,white)
            self.screen.blit(mousePos, [10,10])
            
            # Draw health stats
            entityFont = self.pygame.font.Font(None, 20)
            playerHealth = ("Health: " + str(self.player.player.HP))
            playerHealthText = entityFont.render(playerHealth,True,black)
            self.screen.blit(playerHealthText, [50,50])
            enemy1Health = ("Enemy 1 Health: " + str(self.enemy1.player.HP))
            enemy1HealthText = entityFont.render(enemy1Health,True,black)
            self.screen.blit(enemy1HealthText, [50,550])
            enemy2Health = ("Enemy 2 Health: " + str(self.enemy2.player.HP))
            enemy2HealthText = entityFont.render(enemy2Health,True,black)
            self.screen.blit(enemy2HealthText, [50,560])
            
            # Enemy 1 animation
            if enemy1Direction == "UP" and speedCounter % 15 == 0:
                if self.enemy1.rect.y > 100:
                    self.enemy1.update("UP", 1)
                else:
                    enemy1Direction = "DOWN"
            elif enemy1Direction == "DOWN" and speedCounter % 15 == 0:
                if self.enemy1.rect.y < 500:
                    self.enemy1.update("DOWN", 1)
                else:
                    enemy1Direction = "UP"
            # Enemy 2 animation
            if enemy2Direction == "LEFT" and speedCounter % 15 == 0:
                if self.enemy2.rect.x > 100:
                    self.enemy2.update("LEFT", 1)
                else:
                    enemy2Direction = "RIGHT"
            elif enemy2Direction == "RIGHT" and speedCounter % 15 == 0:
                if self.enemy2.rect.x < 550:
                    self.enemy2.update("RIGHT", 1)
                else:
                    enemy2Direction = "LEFT"
            speedCounter += 1
            if speedCounter > 15:
                speedCounter = 0
            
            # Listen for keyboard events				
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN:
                    # Movement keys
                    if event.key == self.pygame.K_UP and self.player.rect.y > 20:
                        self.player.update("UP", 5)
                    if event.key == self.pygame.K_DOWN and self.player.rect.y < 540:
                        self.player.update("DOWN", 5)
                    if event.key == self.pygame.K_LEFT and self.player.rect.x > 20:
                        self.player.update("LEFT", 5)
                    if event.key == self.pygame.K_RIGHT and self.player.rect.x < 755:
                        self.player.update("RIGHT", 5)
                        
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
                    
            # Check for collisions
            enemyCollision = pygame.sprite.spritecollide(self.player, self.enemy_list, False) 
            if len(enemyCollision) > 0:
                for sprite in enemyCollision:
                    self.handleAttack(sprite, self.player, sprite.weapons.weapons[5])
                    self.handleAttack(self.player, sprite, self.player.weapons.weapons[5])
            itemCollision = pygame.sprite.spritecollide(self.player, self.item_sprite_list, False)
            if len(itemCollision) > 0:
                for item in itemCollision:
                    if item.type == "health":
                        self.player.player.addHP(80)
                        item.remove(self.item_sprite_list)
                    if item.type == "chest":
                        for event in self.pygame.event.get():
                            if event.key == self.pygame.K_SPACE:
                                self.item_sprite_list.add(self.key)
                    if item.type == "key":
                        item.remove(self.item_sprite_list)
            
            # Draw items
            self.item_sprite_list.draw(self.screen)
            
            # Draw character				
            self.all_sprites_list.draw(self.screen)

            # Update the screen with what we've drawn.
            self.pygame.display.flip()
            self.pygame.event.pump()            

    def classSelection(self):
        while True:            
            # Draw background
            self.screen.blit(classSelectImg, [0,0]) 
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,white)
            self.screen.blit(mousePos, [10,10]) 
            
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
            self.screen.blit(instructMenuImg, [0,0]) 
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,white)
            self.screen.blit(mousePos, [10,10]) 
            
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
        shieldX = 280
        shieldY = 250
        
        # Reset entities if there are any
        for entity in self.all_sprites_list:
            self.all_sprites_list.remove(entity)
        for entity in self.enemy_list:
            self.enemy_list.remove(entity)
        
        while True:
            # Draw background
            self.screen.blit(mainMenuImg, [0,0]) 
            
            # Mouse position for debugging
            mouseCoordinates = self.pygame.mouse.get_pos()
            mouseFont = self.pygame.font.Font(None, 14)
            mousePos = mouseFont.render(("MOUSE_POS = (%d,%d)" % mouseCoordinates),True,white)
            self.screen.blit(mousePos, [10,10]) 
            
            # Draw shield
            shield = self.pygame.image.load("images/Shield.png")
            shieldPos = [shieldX, shieldY]
            self.screen.blit(shield, shieldPos)
            
            # Listen for keyboard events
            for event in self.pygame.event.get():
                # Moving the shield icon with UP and DOWN arrow keys
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_UP and shieldY > 190:
                        shieldY = shieldY - 70
                        optionNum = optionNum - 1
                    if event.key == self.pygame.K_DOWN and shieldY < 350:
                        shieldY = shieldY + 70
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