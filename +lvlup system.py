#DMGsimulator Idle Game by Leszek Michalak

player_name = input("please enter hero name and press enter key")
while True:
  if len(player_name)<3:
    print("Better try longer name")
    import time
    time.sleep(3)
    player_name = input("please enter hero name and press enter key (use 3-20 letter long name)")
  if len(player_name)>20:
    print("Better try shorter name")
    import time
    time.sleep(3)
    player_name = input("please enter hero name and press enter key (use 3-20 letter long name)")
  if len(player_name)>3 and len(player_name)<20:
    print("\nHero name: "+player_name)
    import time
    time.sleep(1)
    break

hero_class = input("\nPlease choose hero's class:\n1. knight (type 1) \n2. cleric (type 2)\n\n")

while True:
  if hero_class==str(1):
    print(str(player_name)+ " is a knight")
    import time
    time.sleep(3)
    break
  if hero_class==str(2):
    print(str(player_name)+ " is a cleric")
    import time
    time.sleep(3)
    break
  else:
    print("Please type hero's class correctly")
    import time
    time.sleep(3)
    hero_class = input("\nPlease choose hero's class:\n1. knight (type 1) \n2. cleric (type 2)\n\n")

#player stats

player_lvl=1
Cash_player=0
Exp_player_total=0
player_stamina = 15
player_strenght = 10
player_armor = 2
player_dexterity = 10
player_hp = player_stamina * 10
player_max_hp = player_stamina * 10
player_dmg = range(player_strenght, player_strenght * 3, 1)
prev_player_hp = player_hp
player_purse = 0

#variable monster stats

monster_lvl=1
monster_hp = 100*monster_lvl
monster_max_hp = 100*monster_lvl
monster_dmg = range(1, 40)
monster_armor = 1
monster_dexterity = 10
prev_monster_hp = monster_hp

print("\n" + str(player_name) + " hp: " + str(player_hp))
print("Damage: " + str(min(player_dmg)) + " to " + str(max(player_dmg)))
print("Armor: " + str(player_armor) + "\n")

import time
time.sleep(2)

print("Monster hp: " + str(monster_hp))
print("Monster's damage: " + str(min(monster_dmg)) + " to " +str(max(monster_dmg)))
print("Monster armor: " + str(monster_armor))

start=input("\ntype anykey to start a fight")

import time
time.sleep(1)
fight=1
round=1
print("\nstart!\n")



while True:
  print("\nround:" + str(round))
  
  import random
  hit_p_c=random.choice(range(0,player_dexterity, 1))
  hit_m_c=random.choice(range(0,monster_dexterity, 1))
  if hit_p_c>hit_m_c*2:
    print("Monster misses!")
    hit_m=0
    player_hp = player_hp - hit_m + player_armor
  else:
    hit_m = random.choice(list(monster_dmg))
  if hit_m_c>hit_p_c*2:
    print("Hero misses!")
    hit_p=0
  else:
    hit_p=random.choice(list(player_dmg))

  player_hp=player_hp-hit_m+player_armor
  monster_hp=monster_hp-hit_p+monster_armor

  print(str(player_name) + str(" does ") + str(hit_p) + str(" damage with his hit"))
  print(str("Monster does ") + str(hit_m) + str(" damage with its hit\n"))
  print(str(player_name) + "'s hp: " + str(player_hp) + " (damage received:" + str(hit_m) + ", absorbed by armor:" + str(player_armor) + ")")
  print("monster's hp: " + str(monster_hp) + " (damage received:" + str(hit_p) + ", absorbed by armor:" + str(monster_armor) + ")" + "\n")

  import time
  time.sleep(0.8)
  round+=1

  if monster_hp<0:
    print("Hero delivers final blow (" +str(prev_player_hp-player_hp) + " damage)")  
    print("Victory!")    
    Exp_gain=monster_lvl*6
    Cash_gain=monster_lvl*3
    print("Experience points gained: " + str(Exp_gain) +  " ("+ str(Exp_player_total) + " points so far)")
    print("Gold coins found: " + str(Cash_gain) + " (" + str(player_purse) + " gold coins so far in purse)") 
    while Exp_player_total>=player_lvl*20:
      player_lvl+=1
      print("Level up! Please choose which attribute you want to level up: dexterity, strenght or stamina)")
      lvl_up_attribute=input("please type in the name of an attribute:")
      if lvl_up_attribute!=str("dexterity") or str("strenght") or str("stamina"):
        input("Please type once again:")
      if lvl_up_attribute==str("dexterity"):
        player_dexterity+=2
        print("Atribute '" + str(lvl_up_attribute) + "' has increased by 2 points, to a total of " + str(player_dexterity) + "points")
        break
      if lvl_up_attribute==str("strenght"):
        player_strenght+=2
        print("Atribute '" + str(lvl_up_attribute) + "' has increased by 2 points, to a total of " + str(player_strenght) + "points")
        break
      if lvl_up_attribute==str("stamina"):
        player_stamina+=2
        print("Atribute '" + str(lvl_up_attribute) + "' has increased by 2 points, to a total of " + str(player_stamina) + "points")
        break
        continue



    end_match_option=input("do you want to continue? yes/no/nIf you want to see your character's stats please type in 'stats' or 'match' for fight stats")
    if end_match_option==str("no"):
      break
    if end_match_option==str("yes"):
      player_hp=player_max_hp
      monster_hp=monster_max_hp
      player_purse = player_purse + Cash_gain
      Exp_player_total = Exp_player_total + Exp_gain
      round=1
      fight+=1
      continue
    if end_match_option==str("stats"):
      print("Player lvl: " + str(player_lvl))
      print("strenght: " + str(player_strenght))
      print("dexterity: " + str(player_dexterity))
      print("stamina: " + str(player_stamina))
      print("armor: " + str(player_armor))
      print("player max hp:" + str(player_max_hp))
      print("Damage: " + str(min(player_dmg)) + " to " + str(max(player_dmg)))
      input("please type any key for continue:")
      player_hp=player_max_hp
      monster_hp=monster_max_hp
      player_purse = player_purse + Cash_gain
      Exp_player_total = Exp_player_total + Exp_gain
      fight+=1
      round=1
      continue
    if end_match_option==str("match"):
      print("Match no.: " + str(fight))
      print("Number of rounds: " + str(round))
      print(str(player_name) + "'s hp left: " + str(player_hp))
      input("please type any key for continue:")
      player_hp=player_max_hp
      monster_hp=monster_max_hp
      player_purse = player_purse + Cash_gain
      Exp_player_total = Exp_player_total + Exp_gain
      fight+=1
      round=1
      continue     
  elif player_hp<1:
    print("Monster delivers final blow")
    print("Hero collapses")
    end_match_option=input("do you want to continue? yes/no/nIf you want to see your character's stats please type in 'stats' or 'match' for fight stats")
    if end_match_option==str("no"):
      break
    if end_match_option==str("yes"):
      player_hp=player_max_hp
      monster_hp=monster_max_hp
      fight+=1
      round=1
      continue
    if end_match_option==str("stats"):
      print("Player lvl: " + str(player_lvl))
      print("strenght: " + str(player_strenght))
      print("dexterity: " + str(player_dexterity))
      print("stamina: " + str(player_stamina))
      print("armor: " + str(player_armor))
      print("player max hp:" + str(player_max_hp))
      print("Damage: " + str(min(player_dmg)) + " to " + str(max(player_dmg)))
      input("please type any key for continue:")
      player_hp=player_max_hp
      monster_hp=monster_max_hp
      player_purse = player_purse + Cash_gain
      Exp_player_total = Exp_player_total + Exp_gain
      fight+=1
      round=1
      continue
    if end_match_option==str("match"):
      print("Match no.: " + str(fight))
      print("Number of rounds: " + str(round))
      print(str(player_name) + "'s hp left: " + str(player_hp))
      input("please type any key for continue:")
      player_hp=player_max_hp
      monster_hp=monster_max_hp
      player_purse = player_purse + Cash_gain
      Exp_player_total = Exp_player_total + Exp_gain
      fight+=1
      round=1
      continue