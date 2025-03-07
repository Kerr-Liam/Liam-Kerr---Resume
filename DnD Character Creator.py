import random
import time
def character_maker():
    # simple introduction to the program
    print('========Welcome to the D&D character sheet maker========')
    print('')

    # Any Presets
    stats = ['Str', 'Dex', 'Con', 'Wis', 'Int', 'Cha']
    stat_roll = []
    stat_count = 0
    ac = 0
    # blank lists for later use
    language = []
    equipment = []
    feats = []
    weapons = []
    weapon_info = []
    weapons_options = []
    spells = []

    # Assign value to each stat roll
    def stat_value(roll):
        if roll == 4 or roll == 5:
            stats[stat_count] = '-3'
        elif roll == 6 or roll== 7:
            stats[stat_count] = '-2'
        elif roll == 8 or roll == 9:
            stats[stat_count] = '-1'
        elif roll == 10 or roll == 11:
            stats[stat_count] = '+0'
        elif roll == 12 or roll == 13:
            stats[stat_count] = '+1'
        elif roll == 14 or roll == 15:
            stats[stat_count] = '+2'
        elif roll == 16 or roll == 17:
            stats[stat_count] = '+3'
        elif roll == 18 or roll == 19:
            stats[stat_count] = '+4'
        elif roll == 20:
            stats[stat_count] = '+5'
        else:
            print("uh oh spaghettio")
        return stats[stat_count]

    # Roll a random number for each stat
    for i in stats:
        roll = random.randint(4,20)
        rolls = stat_value(roll)
        stat_roll.append(roll)
        stat_count = stat_count + 1



    # functions for class choices
    def fighter():
        hit_dice = '1d10'
        hp = 20 + int(stats[2])
        des = print('You are now choosing your weapons and equipment, write a or b for your choice')
        equip_1 = input('Would you like (a) Chain mail armor or (b) leather armor and a long bow? ').lower()
        while equip_1 not in equip_options:
            print('Sorry that is not an option (enter a or b)')
            equip_1 = input('Would you like (a) Chain mail armor or (b) leather armor and a long bow? ').lower()
        if equip_1 == 'a':
            print('You chose Chain mail armor')
            ac = 16
        else:
            print('You chose Leather armor and a Long bow')
            ac = 11 + int(stats[1])
            weapons.append(f'Long bow(150/600)  /  {stats[1]}  /  1d8 piercing')
            weapons_options.append('long bow')
            weapon_info.append('20x Arrows')
        equip_2 = input('Would you like (a) A shortsword and shield or (b) A warhammer and a morning star? ')
        while equip_2 not in equip_options:
            print('Sorry that is not an option (enter a or b)')
            equip_2 = input('Would you like (a) A shortsword and shield or (b) A warhammer and a morning star? ')
        if equip_2 == 'a':
            print('You chose a Shortsword and a Shield')
            ac = ac + 2
            weapons.append(f'Shortsword  /  {stats[0]}  / 1d6 piercing')
            weapons_options.append('shortsword')
        else:
            print('You chose a Warhammer and a Morning Star')
            weapons.append(f'Warhammer  /  {stats[0]}  / 1d8 bludgeoning')
            weapons_options.append('warhammer')
            weapons.append(f'Morning Star  /  {stats[0]}  / 1d8 piercing')
            weapons_options.append('morning star')
        p = print('You are now choosing your backpack, type the name of the pack you would like')
        backpack = input("Would you like a Dungeoneer pack or an Explorer pack? ").lower()
        while backpack not in pack_options:
            print('Sorry that is not an option (try checking your spelling)')
            backpack = input("Would you like a Dungeoneer pack or an Explorer's pack? ").lower()
        return hit_dice,hp,ac,backpack,equip_1,equip_2
    def ranger():
        hit_dice = '1d10'
        hp = 20 + int(stats[2])
        des = print('You are now choosing your weapons and equipment, write a or b for your choice')
        equip_1 = input('Would you like (a) Scale mail or (b) Leather armor? ').lower()
        while equip_1 not in equip_options:
            print('Sorry that is not an option (enter a or b)')
            equip_1 = input('Would you like (a) Scale mail or (b) Leather armor? ').lower()
        if equip_1 == 'a':
            print('You chose Scale mail')
            if int(stats[1]) <= 2:
                ac = 14 + int(stats[1])
            else:
                ac = 16
        else:
            print('You chose Leather armor')
            ac = 11 + int(stats[1])
        equip_2 = input('Would you like (a) a Shortsword or (b) a Handaxe? ')
        while equip_2 not in equip_options:
            print('Sorry that is not an option (enter a or b)')
            equip_2 = input('Would you like (a) a Shortsword or (b) a Handaxe? ')
        if equip_2 == 'a':
            print('You chose a Shortsword')
            weapons.append(f'Shortsword  /  {stats[0]}  / 1d6 piercing')
            weapons_options.append('shortsword')
        else:
            print('You chose a Handaxe')
            weapons.append(f'Handaxe(20/60)  /  {stats[0]}  / 1d6 slashing')
            weapon_info.append('Handaxe')
            weapons_options.append('handaxe')
        p = print('You are now choosing your backpack, type the name of the pack you would like')
        backpack = input("Would you like a Dungeoneer pack or an Explorer pack? ").lower()
        while backpack not in pack_options:
            print('Sorry that is not an option (try checking your spelling)')
            backpack = input("Would you like a Dungeoneer pack or an Explorer's pack? ").lower()
        weapons.append(f'Long bow(150/600)  /  {stats[1]}  / 1d8 piercing')
        weapons_options.append('long bow')
        weapon_info.append('20x Arrows')
        return hit_dice,hp,ac,backpack,equip_1,equip_2
    def rogue():
        hit_dice = '1d8'
        hp = 18 + int(stats[2])
        des = print('You are now choosing your weapons and equipment, write a or b for your choice')
        equip_1 = input('Would you like (a) A rapier or (b) A shortsword? ').lower()
        while equip_1 not in equip_options:
            print('Sorry that is not an option (enter a or b)')
            equip_1 = input('Would you like (a) A rapier or (b) A shortsword? ').lower()
        if equip_1 == 'a':
            print('You chose a Rapier')
            weapons.append(f'Rapier  /  {stats[0]}  / 1d8 piercing')
            weapons_options.append('rapier')
        else:
            print('You chose a Shortsword')
            weapons.append(f'Shortsword  /  {stats[0]}  / 1d6 piercing')
            weapons_options.append('shortsword')
        equip_2 = input('Would you like (a) Shortbow or (b) A Shortsword? ').lower()
        while equip_1 not in equip_options:
            print('Sorry that is not an option (enter a or b)')
            equip_2 = input('Would you like (a) Shortbow or (b) A Shortsword? ').lower()
        if equip_2 == 'a':
            print('You chose a Shortbow')
            weapons.append(f'Shortbow  /  {stats[1]}  / 1d6 piercing')
            weapons_options.append('shortbow')
            weapon_info.append('20x Arrows')
        else:
            print('You chose a Shortsword')
            weapons.append(f'Shortsword  /  {stats[0]}  / 1d6 piercing')
            weapons_options.append('shortsword')
        print('You are now choosing your backpack, type the name of the pack you would like')
        backpack = input("Would you like a Dungeoneer pack, an Explorer pack or a Burglar pack? ").lower()
        while backpack not in pack_options:
            print('Sorry that is not an option (try checking your spelling)')
            backpack = input("Would you like a Dungeoneer pack, an Explorer pack or a Burglar pack? ").lower()
        ac = 11 + int(stats[1])
        weapons.append(f'Dagger  /  {stats[0]}  / 1d4 piercing')
        weapon_info.append('Dagger')
        weapons_options.append('dagger')
        equipment.append("  - Thieves' Tools")
        return hit_dice,hp,ac,backpack,equip_1,equip_2
    def wizard():
        hit_dice = '1d6'
        hp = 16 + int(stats[2])
        des = print('You are now choosing your weapons and equipment, write a or b for your choice')
        equip_1 = input('Would you like (a) A quarterstaff or (b) A dagger? ').lower()
        while equip_1 not in equip_options:
            print('Sorry that is not an option (try checking your spelling)')
            equip_1 = input('Would you like (a) A quarterstaff or (b) A dagger? ').lower()
        if equip_1 == 'a':
            print('You chose a Quaterstaff')
            weapons.append(f'Quaterstaff  /  {stats[0]}  / 1d6 blugdeoning')
            weapons_options.append('quarterstaff')
        else:
            print('You chose a Dagger')
            weapons.append(f'Dagger  /  {stats[0]}  / 1d4 piercing')
            weapons_options.append('dagger')
        print('You are now choosing your backpack, type the name of the pack you would like')
        backpack = input("Would you like an Explorer pack or a Scholar pack? ").lower()
        while backpack not in pack_options:
            print('Sorry that is not an option (enter a or b)')
            backpack = input("Would you like an Explorer pack or a Scholar pack? ").lower()
        ac = 10 + int(stats[1])
        equipment.append("  - Spellbook")
        equipment.append("  - Arcane focus")
        spell ="Burning Hands / 50/50 chance to do 2d8 or 1d6 fire damage", "Magic Missile / 1d10 force damage",  "Ray of frost / 1d8 cold damage."
        for i in spell:
            spells.append(i)
        return hit_dice,hp,ac,backpack,equip_1,spell


    # only two options for equipment choices, to be used to make loop
    equip_options = ['a', 'b']
    # option list for the backpack choices later in program
    pack_options = ['dungeoneer', 'explorer', 'burglar', 'scholar','dungeoneer pack', 'explorer pack', 'burglar pack', 'scholar pack']
    # List of items in the backpack choices for the equipment
    dungeoneer_pack = ['  - Crowbar', '  - Hammer', '  - 10x Pitons', '  - 10x Torches', '  - Tinderbox', '  - 10x Rations', '  - Waterskin', '  - 50ft Rope']
    explorer_pack = ['  - Bedroll', '  - Mess kit', '  - Tinderbox', '  - 10x Torches', '  - 10x Rations', '  - Waterskin', '  - 50ft Rope']
    burglar_pack = ['  - 1000x Ball bearings', '  - 10ft String', '  - Bell', '  - 5x Candles', '  - Crowbar', '  - Hammer', '  - 10x Pitons', '  - Hooded lantern', '  - 2x Flasks of oil', '  - 5x Rations', '  - Tinderbox', '  - Waterskin', '  - 50ft Rope']
    scholar_pack = ['  - Book of lore', '  - Bottle of ink', '  - Ink pen', '  - 10x Parchment sheets', '  - Small bag of sand', '  - Small knife']
    # Choice of their characters name
    first_name = input('Please choose a first name: ')
    last_name = input('Please choose a last name: ')
    name = f'{first_name[0].upper()}{first_name[1:].lower()} {last_name[0].upper()}{last_name[1:].lower()}'
    # Calculate passive wisdom(perception)
    passive = int(stats[0]) + 10
    # proficiency bonus is alwasy +2 because they are level 1
    profbns = 2
    # Calculating the spell save DC and attack modifier
    dc = 8 + profbns + int(stats[4])
    spell_mod = profbns + int(stats[4])
    # Choice of race
    race = input("Would you like to be a Dwarf, Elf, Human, or Tiefling? ").lower()
    race_options = ['dwarf','elf','human','tiefling']
    while race not in race_options:
        print('Sorry that is not an option (try checking your spelling)')
        race = input("Would you like to be a Dwarf, Elf, Human, or Tiefling? ").lower()
    # limit their options for class (assists with the while loop)
    clas_options = ['fighter','ranger','rogue','wizard']
    # They chose to be a dwarf and now have to choose their class
    # Returning race choice and continuing to class choice
    print(f"You are a(n) {race}")
    clas = input("Would you like to be a Fighter, Ranger, Rogue, or Wizard? ").lower()
    while clas not in clas_options:
        print('Sorry that is not a option (try checking your spelling)')
        clas = input("Would you like to be a Fighter, Ranger, Rogue, or Wizard? ").lower()
    if clas == 'fighter':
        output = fighter()
    elif clas == 'ranger':
        output = ranger()
    elif clas == 'rogue':
        output = rogue()
    elif clas == 'wizard':
        output = wizard()

    # Adds the users choice of backpack's items to the equipment list to later be printed
    backpack = output[3]
    if 'dungeoneer' in backpack:
        for i in dungeoneer_pack:
            equipment.append(i)
    elif 'explorer' in backpack:
        for i in explorer_pack:
            equipment.append(i)
    elif 'burglar' in backpack:
        for i in burglar_pack:
            equipment.append(i)
    elif 'scholar' in backpack:
        for i in scholar_pack:
            equipment.append(i)
    # return what backpack they chose
    print(f'You chose the {backpack} backpack')

    # Printing option
    return_info = input("Would you like to see your character sheet before proceeding to the game?(yes/no) ").lower()
    if return_info == 'yes':
        # informing them of timer and pausing for 5 seconds
        print('Please wait while we create your character...')
        time.sleep(3)
           
        # Character Sheet Begining
        print('')
        print('')
        print("========Your Character Sheet========")
        time.sleep(1)
        print('')
        # printing out the characters name using {name} which is the first and last name already entererd combined with capitals
        print(f"Name: {name}")
        time.sleep(0.5)
        # printing out the characters class with a capital first letter
        print(f'Class: {clas[0].upper()}{clas[1:].lower()}')
        time.sleep(0.5)
        # printing out the characters race with a capital first letter
        print(f'Race: {race[0].upper()}{race[1:].lower()}')
        time.sleep(0.5)
        # Hit Points (HP)
        print(f'Hit Points: {output[1]}')
        time.sleep(0.5)
        # Armour Class (AC)
        print(f'Armor Class: {output[2]}')
        time.sleep(0.5)
        # Initiative
        print(f'Initiative: {stats[1]}')
        time.sleep(0.5)
        # Hit Dice
        print(f'Hit Dice: {output[0]}')
        time.sleep(0.5)
        # Proficiency Bonus
        print(f'Proficiency Bonus: +{profbns}')
        time.sleep(0.5)
        # Passive Perception
        print(f'Passive Wisdom(perception): {passive}')
        time.sleep(0.5)
        print('') 
        # Main stats
        print('----Ability Scores----')
        time.sleep(1)
        print(f"Strength: {stat_roll[0]}")
        print(f"Modifier: {stats[0]}")
        time.sleep(0.5)
        print("")
        print(f"Dexterity: {stat_roll[1]}")
        print(f"Modifier: {stats[1]}")
        time.sleep(0.5)
        print("")
        print(f"Constitution: {stat_roll[2]}")
        print(f"Modifier: {stats[2]}")
        time.sleep(0.5)
        print("")
        print(f"Intelligence: {stat_roll[4]}")
        print(f"Modifier: {stats[4]}")
        time.sleep(0.5)
        print("")
        print(f"Wisdom: {stat_roll[3]}")
        print(f"Modifier: {stats[3]}")
        print("")
        print(f"Charisma: {stat_roll[5]}")
        print(f"Modifier: {stats[5]}")
        time.sleep(0.5)
        print("")

        # Saving Throws
        print("----Saving Throws----")
        time.sleep(1)
        print(f'Strength = {stats[0]}')
        time.sleep(0.5)
        print(f'Dexterity = {stats[1]}')
        time.sleep(0.5)
        print(f'Constitution = {stats[2]}')
        time.sleep(0.5)
        print(f'Intelligence = {stats[4]}')
        time.sleep(0.5)
        print(f'Wisdom = {stats[3]}')
        time.sleep(0.5)
        print(f'Charisma = {stats[5]}')
        time.sleep(0.5)
        print('')
        # printing out the characters skills using the modifiers from before
        print("----Skills----")
        time.sleep(1)
        print(f'Acrobatics: {stats[1]}')
        time.sleep(0.5)
        print(f'Animal Handling: {stats[3]}')
        time.sleep(0.5)
        print(f'Arcana: {stats[4]}')
        time.sleep(0.5)
        print(f'Athletics: {stats[0]}')
        time.sleep(0.5)
        print(f'Deception: {stats[5]}')
        time.sleep(0.5)
        print(f'History: {stats[4]}')
        time.sleep(0.5)
        print(f'Insight: {stats[3]}')
        time.sleep(0.5)
        print(f'Intimidation: {stats[5]}')
        time.sleep(0.5)
        print(f'Investigation: {stats[4]}')
        time.sleep(0.5)
        print(f'Medicine: {stats[3]}')
        time.sleep(0.5)
        print(f'Nature: {stats[4]}')
        time.sleep(0.5)
        print(f'Perception: {stats[3]}')
        time.sleep(0.5)
        print(f'Performance: {stats[5]}')
        time.sleep(0.5)
        print(f'Persuasion: {stats[5]}')
        time.sleep(0.5)
        print(f'Religion: {stats[4]}')
        time.sleep(0.5)
        print(f'Sleight Of Hand: {stats[1]}')
        time.sleep(0.5)
        print(f'Stealth: {stats[1]}')
        time.sleep(0.5)
        print(f'Survival: {stats[3]}')
        time.sleep(0.5)
        print('')
        # Attacks & Spellcasting
        print("----Attacks & Spellcasting----")
        time.sleep(1)
        print('   Weapon Name   / Atk Bonus /   Damage and Type')
        time.sleep(0.5)
        for i in weapons:
            print(f"   - {i}")
            time.sleep(0.5)
        print('')
        print('Extra info: ')
        for i in weapon_info:
            print(f"  - {i}")
            time.sleep(0.5)
        print('')
        # only printing the spells if the user chooses to be a wizard or elf or tiefling
        if clas == 'wizard':
            print("----Spells----")
            time.sleep(1)
            print(f"Spell Save DC: {dc}")
            time.sleep(0.5)
            print(f"Spell Attack Modifier: +{spell_mod}")
            time.sleep(0.5)
            print("    Spell Name / Casting Time / Range / Components / Duration / Description")
            time.sleep(0.5)
            print('')
            print(f"Spells: ")
            for i in spells:
                print(f"   - {i}")
                time.sleep(0.5)
            print('')
        # Equipment
        print("----Equipment----")
        print('Backpack: ')
        for i in equipment:
            print(i)
            time.sleep(0.5)
        print('')
        print('')
        print('Scroll up for your character info')
    time.sleep(1)
    campaign_start = input('Would you like to start the campaign? (yes/no) ').lower()
    while campaign_start != 'yes':
        campaign_start = input('Type (yes) when you would like to start. ').lower()
    print('')
    print('')
    campaign(stats, name, output, weapons_options, spells, clas)

def campaign(stats, name, output, weapons_options, spells, clas):
    # Start of campaign
    existing_encounters = []
    monsters = []

    if clas == 'wizard':
        weapons_options.append('burning hands')
        weapons_options.append('ray of frost')
        weapons_options.append('magic missile')
            ###
            ###
            ###
    # Class for encounters (combat)
    class encounter():
        #assigning values
        def __init__(self, name, hp, dmg, Str, ac, t):
            self.name = name
            self.hp = hp
            self.new_hp = hp
            self.str = int(Str)
            self.ac = ac
            self.type = t
            self.dmg = dmg
        def end():
            print('Thank you for Playing')
            exit()
        def restart(self):
            monsters.clear()
            restart_options = ['New Game', 'Re-try Campaign', 'End Game']
            restart_numbers = ['1', '2', '3']
            print('YOU HAVE DIED')
            print('Would you like to:')
            option = 1
            for i in restart_options:
                print(f"   {option}. {i}")
                option = option + 1
            restart = input('Enter the number of your choice: ')
            if restart not in restart_numbers:
                print("Sorry that's not an option. Make sure you enter the number of your choice")
                print('Would you like to:')
                option = 1
                for i in restart_options:
                    print(f"   {option}. {i}")
                    option = option + 1
                restart = input('Enter the number of your choice: ').lower()
            elif restart == '1':
                character_maker()
            elif restart == '2':
                campaign()
            elif restart == '3':
                end()
            else:
                print('Woops...')
        def alive(self, n, length):
            if self.hp <= 0 and self.type != 'player':
                monsters.remove(n)
            elif self.hp <= 0 and self.type == 'player':
                self.restart()
            elif self.hp > 0 and self.type != 'player':
                self.player_attack()
            elif length == 1 and self.type == 'player':
                monsters.clear()
                if player.hp < player.new_hp:
                    player.hp = player.new_hp
                    print(f'After hard fought combat you take a rest and restore your hit points back to {player.hp}')
                time.sleep(1)
                print('')
            elif self.type == 'player' and length != 1:
                self.damage(monsters[0].dmg)
            else:
                print('Something went wrong')
        def player_attack(self):
            chance = random.randint(1,2)
            print('')
            print('Which of the following weapons would you like to use?')
            print('====Weapons====')
            for i in weapons_options:
                print(f'   - {i}')
            weapon_used = input("Your choice: ").lower()
            while weapon_used not in weapons_options:
                print("Sorry that's not an option (check your spelling)")
                weapon_used = input("Your choice: ").lower()
            if weapon_used == 'long bow':
                dmg = random.randint(1,8)
                self.damage(dmg)
            elif weapon_used == 'shortsword':
                dmg = random.randint(1,6)
                self.damage(dmg)
            elif weapon_used == 'warhammer':
                dmg = random.randint(1,8)
                self.damage(dmg)
            elif weapon_used == 'morning star':
                dmg = random.randint(1,8)
                self.damage(dmg)
            elif weapon_used == 'light crossbow':
                dmg = random.randint(1,8)
                self.damage(dmg)
            elif weapon_used == 'handaxe':
                dmg = random.randint(1,6)
                self.damage(dmg)
            elif weapon_used == 'rapier':
                dmg = random.randint(1,8)
                self.damage(dmg)
            elif weapon_used == 'dagger':
                dmg = random.randint(1,4)
                self.damage(dmg)
            elif weapon_used == 'quarterstaff':
                dmg = random.randint(1,6)
                self.damage(dmg)
            elif weapon_used == 'short bow':
                dmg = random.randint(1,6)
                self.damage(dmg)
            elif weapon_used == 'burning hands':
                if chance == 1:
                    dmg = random.randint(1,8) + random.randint(1,8)
                else:
                    dmg = random.randint(1,6)
                self.damage(dmg)
            elif weapon_used == 'magic missile':
                dmg = random.randint(1,4)
                self.damage(dmg)
            elif weapon_used == 'ray of frost':
                dmg = random.randint(1,4)
                self.damage(dmg)
        #Damage / Combat function
        def damage(self, dmg):
            dead = 1
            print('')
            print(f'{self.name} is attacked')
            roll = self.str + random.randint(1,20) + 2
            print('Attack Roll...')
            time.sleep(2)
            print(f"Attack Roll = {roll}")            
            if roll >= self.ac:
                print('The Atttack Hits')
                print('Rolling damage...')
                time.sleep(2)
                hp = self.hp - dmg
                self.hp = hp
                print(f'{self.name} takes {dmg} damage. They have {hp} hp left.')
                if self.hp <= 0:
                    print(f"{self.name} has DIED")
                return hp
            else:
                time.sleep(2)
                print('**Miss**')
            print('')

    
    # Player stats       
    player = encounter(name, output[1], -3, stats[0], output[2], 'player')
    # Monster Stats
    goblin_1 = encounter('goblin_1', 7, random.randint(1,6), -1, 15, 'monster')
    goblin_2 = encounter('goblin_1', 7, random.randint(1,6), -1, 15, 'monster')
    Animated_Armour_1 = encounter('Animated_Armour_1', 33, random.randint(1,6), 2, 18, 'monster')
    Animated_Armour_2 = encounter('Animated_Armour_2', 33, random.randint(1,6), 2, 18, 'monster')
    Owlbear = encounter('Owlbear',40, random.randint(1,10), 5, 13, 'monster')
    Giant_Spider_1 = encounter('Giant_Spider_1', 11, random.randint(1,6), 1, 13, 'monster')
    Giant_Spider_2 = encounter('Giant_Spider_2', 11, random.randint(1,6), 1, 13, 'monster')
    Woodelf_1 = encounter('Woodelf_1', 16, random.randint(1,8), 0, 13, 'monster')
    Woodelf_2 = encounter('Woodelf_2', 11, random.randint(1,8), 1, 12, 'monster')
    Woodelf_3 = encounter('Woodelf_3', 11, random.randint(1,8), 1, 12, 'monster')
    Bullywug = encounter('Bullywug', 11, random.randint(1,4), 0, 12, 'monster')
    Bandit_1 = encounter('Bandit_1', 11, random.randint(1,4), 0, 12, 'monster')
    Bandit_2 = encounter('Bandit_2', 11, random.randint(1,4), 0, 12, 'monster')
    Bandit_3 = encounter('Bandit_3', 11, random.randint(1,4), 0, 12, 'monster')
    Bandit_4 = encounter('Bandit_4', 11, random.randint(1,4), 0, 12, 'monster')
    Bandit_5 = encounter('Bandit_5', 11, random.randint(1,4), 0, 12, 'monster')
    Bandit_6 = encounter('Bandit_6', 11, random.randint(1,4), 0, 12, 'monster')
    Worg = encounter('Worg', 18, random.randint(1,6) + random.randint(1,6), 3, 13, 'monster')

    #Campaign introduction
    print('Our adventure begins in the mighty town of Mara.')
    print('')
    time.sleep(1)
    print('Here you are heading to a caravan master who has placed posters all over the town asking for an escort to the city of Grayhaven and offering a reward of 25 gold pieces')
    print('for doing so. The poster also says that the journey will last about 20 days, food and bedding included, and this is a strictly one-person job.')
    print('')
    time.sleep(5)
    print('As you are alone and have no place to be you figure a ride from Mara to Grayhaven where you’re getting paid and there’s free food and bedding is perfect.')
    print('')
    time.sleep(5)
    print('Eventually you locate the posters owner, seeing he is an old dwarf with a long grey beard. He introduces himself as Dugal Stonepick, he warns you that there have been')
    print('caravans that have been going missing on that trail over the past few months and if you choose to embark on this journey you should do so with extreme caution.')
    print('')
    time.sleep(5)
    print('Ignorant of his warnings you accept the task.')
    print('')
    time.sleep(1)
    print('Dugal Stonepick informs you that you will be escorting one caravan containing provisions that absolutely must make it to the city of Grayhaven at all costs')
    print('because his business over there quickly running out of supplies and in urgent need of a restock.')
    print('')
    time.sleep(5)
    print('Saying your farewells, you begin your journey to Grayhaven…')
    print('')
    print('')
    print('')
    
    # Determining and running the random encounters
    for i in range(20):
        encounter = random.randint(1,20)
        if encounter >= 16:
            encounter_type = random.randint(1,8)
            while encounter_type in existing_encounters:
                encounter_type = random.randint(1,8)
            existing_encounters.append(encounter_type)
            if encounter_type == 1:
                monster_encounter = "Glimmerberry Bush"
                print('Along the road you notice a path inbetween the trees')
                time.sleep(2)
                print('Upon further inspecting the path, you notice it leads to a small opening that surrounds what appears to be a Glimmerberry bush')
                time.sleep(4)
                print('The berries from this bush can be used to create a variety of potions (including health potions) and can be sold for a high price')
                time.sleep(4)
                print('You can:')
                encounter_choices = ['ignore the bush', 'pick the berries']
                for i in encounter_choices:
                    print(f'   - {i}')
                choice = input('What would you like to do? ').lower()
                while choice not in encounter_choices:
                    print("Sorry that's not an option (check your spelling)")
                    choice = input('What would you like to do? ').lower()
                if choice == 'ignore the bush':
                    print('You decide the bush seems too good to be true and ignore it')
                elif choice == 'Pick the berries':
                    print('You walk up to the bush and once you get close enough realise the bush is a fake')
                    time.sleep(3)
                    print('Out from the trees jump two Goblins')
                    monsters.append(goblin_1)
                    monsters.append(goblin_2)
                    monsters.append(player)
                    while player in monsters:
                        for i in monsters:
                            i.alive(i, len(monsters))
                print('You head back to the caravan and continue on your journey...')
                print('')
                print('')
                time.sleep(2)
                
            elif encounter_type == 2:
                monster_encounter = "Lost Knights"
                print('The caravan is forced to come to a halt as a dozen heavily armoured knights march down the road, blocking the way forward.')
                time.sleep(4)
                print('When the knights get closer you notice that these are not men in armour but spirits')
                time.sleep(4)
                print('The knights demand that you move aside so they can continue to their home city of Kalimir')
                time.sleep(4)
                print('You can:')
                encounter_choices = ['ask them to move', 'attack']
                for i in encounter_choices:
                    print(f'   - {i}')
                choice = input('What would you like to do? ').lower()
                while choice not in encounter_choices:
                    print("Sorry that's not an option (check your spelling)")
                    choice = input('What would you like to do? ').lower()
                if choice == 'ask them to move':
                    print('Rolling persuasion...')
                    time.sleep(2)
                    choice_roll = stats[5] + random.randint(1,20)
                    if choice_roll >= 10:
                        print('You successfully persuade the knights to move')
                        time.sleep(2)
                        print('They apologise for any inconvinience and step to the side of the road, allowing you to continue on your journey...')
                        time.sleep(5)
                    else:
                        print("The knights no longer see you as friendly and send their two strongest fighters forward")
                        time.sleep(2)
                        print("The knights say if you can beat their men they shall allow you to pass")
                        time.sleep(2)
                        monsters.append(Animated_Armour_1)
                        monsters.append(Animated_Armour_2)
                        monsters.append(player)
                        while player in monsters:
                            for i in monsters:
                                i.alive(i, len(monsters))
                        print('After striking down the second fighter the other knights vanish allowing you to continue on your journey...')
                elif choice == 'Attack':
                    print('You jump off the caravan with you weapon drawn')
                    time.sleep(2)
                    print("The knights notice you're no longer friendly and send their two strongest fighters forward")
                    time.sleep(2)
                    print("The knights say if you can beat their men they shall allow you to pass")
                    time.sleep(2)
                    monsters.append(Animated_Armour_1)
                    monsters.append(Animated_Armour_2)
                    monsters.append(player)
                    while player in monsters:
                        for i in monsters:
                            i.alive(i, len(monsters))
                    print('After striking down the second fighter the other knights vanish allowing you to continue on your journey...')
                print('')
                print('')
                time.sleep(2)
                
            elif encounter_type == 3:
                monster_encounter = "Slumbering Owlbear"
                print('As the caravan passes past a pile of leaves on the side of the road, an Owlbear awakens from beneath.')
                time.sleep(4)
                print('Although Owlbears are normally terrirorial and will attack on site, this one seems dazed, only having just awoken.')
                time.sleep(5)
                print('You can: ')
                encounter_choices = ['run', 'attack']
                for i in encounter_choices:
                    print(f'   - {i}')
                choice = input('What would you like to do? ').lower()
                while choice not in encounter_choices:
                    print("Sorry that's not an option (check your spelling)")
                    choice = input('What would you like to do? ').lower()
                if choice == 'run':
                    choice_roll = stats[1] + random.randint(1,20)
                    if choice_roll >= 15:
                        print('You successfully escape the Owlbear before it attacks you or the caravan')
                    else:
                        print('You rush to get the caravan to move and cause the Owlbear to snap back to reality')
                        time.sleep(4)
                        print('The Owlbear attacks you')
                        time.sleep(3)
                        monsters.append(Owlbear)
                        monsters.append(player)
                        while player in monsters:
                            for i in monsters:
                                i.alive(i, len(monsters))
                        print('You defeat the Owlbear allowing you to continue on your journey...')
                elif choice == 'attack':
                    print('You draw your weapon and charge at the Owlbear')
                    time.sleep(4)
                    monsters.append(Owlbear)
                    monsters.append(player)
                    while player in monsters:
                        for i in monsters:
                            i.alive(i, len(monsters))
                    print('You defeat the Owlbear allowing you to continue on your journey...')
                print('')
                print('')
                time.sleep(2)
                
            elif encounter_type == 4:
                monster_encounter = "Trapdoor Spiders"
                print('In the centre of the road lies a 10-foot-deep hole covered in webs, causing the caravan to come to a stop')
                time.sleep(4)
                print('Upon investigating the hole two giant spiders crawl out and attack you')
                monsters.append(Giant_Spider_1)
                monsters.append(Giant_Spider_2)
                monsters.append(player)
                while player in monsters:
                    for i in monsters:
                        i.alive(i, len(monsters))
                print('You head back to the caravan and continue on your journey...')
                print('')
                print('')
                time.sleep(2)
            elif encounter_type == 5:
                monster_encounter = "Unforgiving Elves"
                print('A group of three forest elves jump out o the woods and begin hailing the caravan with arrows')
                time.sleep(4)
                print('You jump behind the caravan for cover')
                time.sleep(3)
                print('You can:')
                encounter_choices = ['run', 'attack']
                for i in encounter_choices:
                    print(f'   - {i}')
                choice = input('What would you like to do? ').lower()
                while choice not in encounter_choices:
                    print("Sorry that's not an option (check your spelling)")
                    choice = input('What would you like to do? ').lower()
                    if choice == 'run':
                        choice_roll = stats[1] + random.randint(1,20)
                        if choice_roll >= 15:
                            print('You successfully escape the Elves before they do any permanent damage to you or the caravan')
                        else:
                            print('You try to quickly get the caravan moving but get caught in combat')
                            time.sleep(4)
                            monsters.append(Scout)
                            monsters.append(Tribal_warrior_1)
                            monsters.append(Tribal_warrior_2)
                            monsters.append(player)
                            while player in monsters:
                                for i in monsters:
                                    i.alive(i, len(monsters))
                            print('You defeat the Elves allowing you to continue on your journey...')
                    elif choice == 'attack':
                        print('You stand up and try to fight the elves off')
                        time.sleep(3)
                        monsters.append(Scout)
                        monsters.append(Tribal_warrior_1)
                        monsters.append(Tribal_warrior_2)
                        monsters.append(player)
                        while player in monsters:
                            for i in monsters:
                                i.alive(i, len(monsters))
                        print('You defeat the Elves allowing you to continue on your journey...')
                    print('')
                    print('')
                    time.sleep(2)
            elif encounter_type == 6:
                monster_encounter = "Wagon Mishap"
                print('In the centre of the road up ahead is what appears to be an abandoned wagon, forcing you to stop the caravan.')
                time.sleep(4)
                print('You approach the wagon cautiously. As you get closer you hear strange croaking sound.')
                time.sleep(4)
                print('Once at the front of the wagon, you slowly lift a cloth covering the entrance')
                time.sleep(4)
                print('As you do so a Bullywug (small frog creature) jumps out and begins to attack you.')
                time.sleep(4)
                monsters.append(Bullywug)
                monsters.append(player)
                while player in monsters:
                    for i in monsters:
                        i.alive(i, len(monsters))
                print('You head back to the caravan and continue on your journey...')
                print('')
                print('')
                time.sleep(2)
            elif encounter_type == 7:
                monster_encounter = "Waylaid by Brigands"
                print('A group of bandits are blocking the road ahead')
                time.sleep(3)
                print('They demand that in order for you to continue, you must surrender all the provisions in the caravan')
                time.sleep(4)
                print('You can:')
                encounter_choices = ['surrender', 'attack']
                for i in encounter_choices:
                    print(f'   - {i}')
                choice = input('What would you like to do? ').lower()
                while choice not in encounter_choices:
                    print("Sorry that's not an option (check your spelling)")
                    choice = input('What would you like to do? ').lower()
                if choice == 'surrender':
                    print('You have surrendered the only thing you were meant to protect')
                    time.sleep(4)
                    print('You arrive to the city empty handed. After recieving no payment or praise you make your way into the city to continue your life...')
                    print('')
                    time.sleep(5)
                    encounter.end()
                elif choice == 'attack':
                    print('Rolling Intimidation...')
                    time.sleep()
                    choice_roll = stats[5] + random.randint(1,20)
                    if choice_roll >= 15:
                        print('You raise from your seat, slowly drawing your weapon')
                        time.sleep(3)
                        print('The bandits look at you in fear')
                        time.sleep(3)
                        print('Before you can even make a move they all scatter, running into the surrounding forest.')
                    else:
                        print('You give the bandits a slight smirk as you jump down from your seat and draw your weapon')
                        time.sleep(4)
                        print('The bandits all draw their daggers and attack you')
                        monsters.append(Bandit_1)
                        monsters.append(Bandit_2)
                        monsters.append(Bandit_3)
                        monsters.append(Bandit_4)
                        monsters.append(Bandit_5)
                        monsters.append(Bandit_6)
                        monsters.append(player)
                        while player in monsters:
                            for i in monsters:
                                i.alive(i, len(monsters))
                        print('You collect yourself and continue on your journey...')
                print('')
                print('')
                time.sleep(2)
            elif encounter_type == 8:
                monster_encounter = "Worg!"
                print('From the undergrowth pounces a worg that appears very skinny and desperate')
                time.sleep(3)
                print('The worg pauses for a second, makes eye contact then attacks you')
                time.sleep(3)           
                monsters.append(Worg)
                monsters.append(player)
                while player in monsters:
                    for i in monsters:
                        i.alive(i, len(monsters))
            
    # Campaign Ending
    print('On the 20th morning you awaken for the final time.')
    print('')
    time.sleep(1)
    print('Eagerly you pack up your camp and set off on the final stretch to the city of Grayhaven.')
    print('')
    time.sleep(4)
    print('After only a couple hours of much deserved peaceful riding you can see these mighty walls slowly rising in the distance.')
    print('As you get closer and closer the walls continue to grow, seemingly touching the clouds.')
    print('')
    time.sleep(6)
    print('Eventually you get close enough to the city that you can hear the sound of all the people of this massive city booming from over the walls.')
    print('')
    time.sleep(5)
    print('You cross a bridge approaching a large gate.')
    print('')
    time.sleep(4)
    print('Once at the gates you are met with a familiar face…')
    print('')
    time.sleep(5)
    print('Dugal stonepick or atleast a man who looks like Dugal. ')
    print('')
    time.sleep(5)
    print('This man walks up to you and introduces himself as Thovir stonepick, brother of Dugal stonepick.')
    print('')
    time.sleep(5)
    print('Thovir thanks you for escorting the caravan and gratefully hands you the 25 gold pieces promised')
    print('')
    time.sleep(5)
    print('You grab your belongings and make your way past the gates, into the city...')
    time.sleep(4)
    end()
    
character_maker()
