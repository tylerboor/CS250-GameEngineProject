# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rosbaldeston"
__date__ ="$Jan 9, 2012 10:40:21 AM$"

class Skills:
    def __init__(self):
        None
        
    def activated(self):
        active = list()
        for item in self.archerySkills:
            if item[3] != 0:
                active.append(item)
        for item in self.oneHandedSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.shieldSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.staffSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.twoHandedSkills:
            if item[3] != 0:
                active.append(item)
        for item in self.unarmedSkills:
            if item[3] != 0:
                active.append(item)
        return active

    # Start Archery Block
    # Archery Weapon Types and Stat Modifiers:
    #   Short Bow:
    #   Long Bow:
    #   Composite Bow:
    #   Compound Bow:
    #   Crossbow:
    def initializeArchery(self, withLevel, withSkills):
        None

    def getArcherySkillLevel(self):
        None

    def getArcheryActivated(self):
        None

    def getArcheryAvailable(self):
        None

    def getArcheryUnavailable(self):
        None

    def activateArcherySkill(self, skill):
        None
	
    def setArcherySkillLevel(self, lv):
            self.archeryLV = lv

    def setArcheryLevelingRateModifier(self, mod):
            self.archeryMod = mod
    # End Archery Block

    # Stary One-Handed Block
    # One-Handed Weapon Types and Stat Modifiers:
    #   Dagger:
    #   Sai:
    #   Sword:
    #   Battle Axe:
    #   Mace:
    def initializeOneHanded(self, withLevel, withSkills):
        None

    def getOneHandedSkillLevel(self):
        None

    def getOneHandedActivated(self):
        None

    def getOneHandedAvailable(self):
        None

    def getOneHandedUnavailable(self):
        None

    def activateOneHandedSkill(self, skill):
        None
	
    def setOneHandedSkillLevel(self, lv):
            self.oneHandedLV = lv

    def setOneHandedLevelingRateModifier(self, mod):
            self.oneHandedMod = mod
    # End One-Handed Block

    # Start Shield Block
    # Shield Types and Stat Modifiers:
    #   Buckler:
    #   Kite:
    #   Heater:
    #   Parma:
    #   Scutum:
    def initializeShield(self, withLevel, withSkills):
        None

    def getShieldSkillLevel(self):
        None

    def getShieldActivated(self):
        None

    def getShieldAvailable(self):
        None

    def getShieldUnavailable(self):
        None

    def activateShieldSkill(self, skill):
        None
	
    def setShieldSkillLevel(self, lv):
            self.shieldLV = lv

    def setShieldLevelingRateModifier(self, mod):
            self.shieldMod = mod
    # End Shield Block

    # Start Staff Block
    # Staff Weapon Types and Stat Modifiers:
    #   Bo:
    #   Spear:
    #   Halberd:
    #   Glaives:
    #   Bardiche:
    def initializeStaff(self, withLevel, withSkills):
        None
    
    def getStaffSkillLevel(self):
        None
    
    def getStaffActivated(self):
        None
        
    def getStaffAvailable(self):
        None
    
    def getStaffUnavailable(self):
        None
        
    def activateStaffSkill(self, skill):
        None
	
    def setStaffSkillLevel(self, lv):
            self.staffLV = lv

    def setStaffLevelingRateModifier(self, mod):
            self.staffMod = mod
    # End Staff Block

    # Start Two-Handed Block
    # Two-Handed Weapon Types and Stat Modifiers:
    #   Club:
    #   Greatsword:
    #   War Axe:
    #   War Hammar:
    #   
    def initializeTwoHanded(self, withLevel, withSkills):
        None
    
    def getTwoHandedSkillLevel(self):
        None
    
    def getTwoHandedActivated(self):
        None
        
    def getTwoHandedAvailable(self):
        None
    
    def getTwoHandedUnavailable(self):
        None
        
    def activateTwoHandedSkill(self, skill):
        None
	
    def setTwoHandedSkillLevel(self, lv):
            self.twoHandedLV = lv

    def setTwoHandedLevelingRateModifier(self, mod):
            self.twoHandedMod = mod
    # End Two-Handed Block
    
    # Start Unarmed Block
    def initializeUnarmed(self, withLevel, withSkills):
        None
    
    def getUnarmedSkillLevel(self):
        None
    
    def getUnarmedActivated(self):
        None
        
    def getUnarmedAvailable(self):
        None
    
    def getUnarmedUnavailable(self):
        None
        
    def activateUnarmedSkill(self, skill):
        None
	
    def setUnarmedSkillLevel(self, lv):
            self.unarmedLV = lv

    def setUnarmedLevelingRateModifier(self, mod):
            self.unarmedMod = mod
    # End Unarmed Block
