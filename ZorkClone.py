position = [1, 1]
monsters = [1, 1, 1, 1]
items = []
chests = [1,1,1,1,1]
GameOver = 1
print ("Welcome to the game you are standing on the first floor of a house." + 
  '\n' + "In order to win you must kill all the monsters before you die" + 
  '\n' + "Controls: right, left, up, down, grab, fight, help" +
  '\n' + "There is a door to the right")
while GameOver == 1:
  move = input(str("Where would you like to move?"))
  if move == 'God':
    position = [3, 1]
    monsters = [0, 0, 0, 1]
    items = ['sword', 'stones']
  elif move == 'help':
    print("HELP:" + '\n' + "Controls: right, left, up, down, grab, fight, help")
  elif move == 'left':
    if position == [1, 5] or position == [2, 4] or position == [2, 5]:
      print("You can't go left")
    else:
      position[1] -= 1
  elif move == 'right':
    if position == [1, 4] or position == [2, 3] or position == [2, 4]:
      print("You can't go right")
    else:
      position[1] += 1
  elif move == 'up':
    if position == [1, 1] or position == [1, 3] or position == [1, 4] or position == [2, 2] or position == [2, 1]:
      print("You can't go up")
    else:
      position[0] += 1
  elif move == 'down':
    if position == [2, 1] or position == [2, 3] or position == [2, 4] or position == [3, 2]:
      print("You can't go down")
    else: 
      position[0] -= 1
  if position[1] <= 0:
    position[1] += 1
    print("You can't go left")
  elif position[1] >= 6:
    position[1] -= 1
    print("You can't go right")
  elif position[0] >= 4:
    position[0] -= 1
    print("You can't go up")
  elif position[0] <= 0:
    position[0] += 1
    print("You can't go down")
  if position[0] == 1:
    if position[1] == 1:
      print("There is a door to the right")
    elif position[1] == 2:
      print("There is a door to the right and left, and a staircase going up")
    elif position[1] == 3:
      print("There is a door to the right and left")
    elif position[1] == 4:
      if len(items) < 3 and chests[0] == 1:
        if move == 'grab':
          items.append('sword')
          chests[0] = 0
          print(items, '\n', "There is a door to the left")
        else:
          print("You found a sword")
      else:
        print("There is a door to the left")
    elif position[1] == 5:
      if len(items) < 3 and chests[4] == 1:
        if move == 'grab':
          items.append('stones')
          chests[4] = 0
          print(items, '\n', "There is a staircase going up")
        else:
          print("You found a stone")
      else:
        print("There is a staircase going up")
  elif position[0] == 2:
    if position[1] == 1:
      if len(items) < 3 and chests[3] == 1:
        if move == 'grab':
          items.append('sword')
          chests[3] = 0
          print(items, '\n', "There is a door to the right")
        else:
          print("You found a sword")
      else:
        print("There is a door to the right")
    elif position[1] == 2:
      if monsters[0] == 1:
        print("You found a monster")
        move = input(str("Where would you like to move?"))
        if 'sword' in items and move == 'fight':
              print("You killed the monster")
              items.remove('sword')
              monsters[0] = 0
        elif move == 'down':
          position[0] = 1
          print("There is a door to the right and left and a staircase going up")
        elif move != 'down':
          print("You didn't kill the monster! You are dead")
          GameOver = 0
      else:
        print("There is a door to the right and left and a staircase going down")
    elif position[1] == 3:
      print("There is a door to the left and a staircase going up")
    elif position[1] == 4:
      if monsters[1] == 1:
        print("You found a monster")
        move = input(str("Where would you like to move?"))
        if 'sword' in items and move == 'fight':
              print("You killed the monster")
              items.remove('sword')
              monsters[1] = 0
        elif move == 'up':
          position[0] = 1
          print("There is a door to the right and left and a staircase going down")
        elif move != 'up':
          print("You didn't kill the monster! You are dead")
          GameOver = 0
      else:
        print("There is a staircase going up")
    elif position[1] == 5:
      if len(items) < 3 and chests[1] == 1:
        if move == 'grab':
          items.append('sword')
          chests[1] = 0
          print(items, '\n', "There is a staircase going up and down")
        else:
          print("You found a sword")
      else:
        print("There is a staircase going up and down")
  elif position[0] == 3:
    if position[1] == 1:
       if monsters[3] == 1:
        print("You found the boss monster")
        move = input(str("Where would you like to move?"))
        if 'sword' in items and 'stones' in items and move == 'fight':
          print("You have found the prize")
          move = input(str("Where would you like to move?"))
          if move == 'grab':
            print("You have won the game")
          else:
            print("You forgot to pick up the prize! You are dead")
          GameOver = 0
        elif move == 'right':
          position[1] = 2
          print("There is a door to the right and left")
        elif move != 'right':
          print("You didn't kill the monster! You are dead")
          GameOver = 0
    elif position[1] == 2:
      if len(items) < 3 and chests[2] == 1:
        if move == 'grab':
          items.append('sword')
          chests[2] = 0
          print(items, '\n', "There is a door to the right and left")
        else:
          print("You found a sword")
      else:
        print("There is a door to the right and left")
    elif position[1] == 3:
      print("There is a door to the right and left and a staircase going down")
    elif position[1] == 4:
      print("There is a door to the right and left and a staircase going down")
    elif position[1] == 5:
      if monsters[2] == 1:
        print("You found a monster")
        move = input(str("Where would you like to move?"))
        if 'sword' in items and move == 'fight':
              print("You killed the monster")
              items.remove('sword')
              monsters[2] = 0
        elif move == 'left':
          position[1] = 4
          print("There is a door to the right and left and a staircase going down")
        elif move != 'left':
          print("You didn't kill the monster! You are dead")
          GameOver = 0
      else:
        print("There is a door to the left and a staircase going down") 