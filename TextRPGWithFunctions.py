#Start menu (1 for start 2 for options etc)
#Inventory Sorting in array (Each item has different value/attributes (Common, Rare, etc))
#Enemy has health + same type of enemy has different stats/attributes
Class = ''
chose = False

def pickClass(chose):
  while chose == False:
    classInt = int(input('Do you want to start as a berserk, mage, rogue, or archer\nClick 1 for berserk, 2 for mage, 3 for rogue or 4 for archer'))
    if classInt == 1: 
      Class = 'b' 
      chose = True
    elif classInt == 2: 
      Class = 'm'
      chose = True
    elif classInt == 3: 
      Class = 'r'
      chose = True
    elif classInt == 4: 
      Class = 'a'
    else: print("That option is not allowed")

    