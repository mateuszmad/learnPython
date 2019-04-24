c = 3
map = [["0" for x in range(c)] for y in range(c)]


def map_printing(board):
    print("MAP:")
    for row in board:
        print(" ".join(row))


class Character(object):
    def __init__(self, name, hp, ap, luck, alive):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.luck = luck
        self.alive = alive


def statistic_print(fighter):
    print(fighter.name)
    print("HP =", fighter.hp)
    print("AP =", fighter.ap)


def map_exploring():
    while True:
        map_printing(map)
        x = int(input("You are in x position, to with place you wanna go? 1/2/3 >>"))
        if x == 1:
            print("You are in treasury. To open the box you have to solve the riddle.")
            riddle()
        elif x == 2:
            print("You are in cave. In the dark you see goblin.")
            fight(player, goblin)
        elif x == 3:
            print("You see a door. You need key.")

            if "key" in player_items:
                print("I opened the door. Leave the dungeon. END OF GAME")
                break
            else:
                print("You don't have a key.")

        else:
            print("You have to choose between 1, 2 or 3.")


def riddle():
    print("To open the box, you have to solve the riddle:")
    while True:
        answer = int(input("what is the solution to the equation: 2*2+2"))
        if answer == 6:
            print("Answer is correct. You open the box and found a sword! (+3 attack point)")
            player.ap = player.ap + 3
            break
        else:
            print("Answer is incorrect. You lost 1 health point")
            player.hp = player.hp - 1


def fight(fighter1, fighter2): #place no 2 on the map
    print("Fight begin!")
    if int(fighter1.luck) > int(fighter2.luck):
        while True:
            decision = input("You have fist move in this round. What do you want to do? Attack or Run a/r >>")
            if decision == "a":
                 fighter2.hp = int(fighter2.hp) - int(fighter1.ap)
                 print(fighter1.name, "attack and hit ", fighter2.name, "with", fighter1.ap, "attack point(s)")

                 if fighter2.hp <= 0:
                     print(fighter2.name, "is dead and you get a key")
                     player_items.append("key")
                     fighter2.alive = False
                     break

                 fighter1.hp = int(fighter1.hp) - int(fighter2.ap)
                 print(fighter2.name, "attack and hit ", fighter1.name, "with", fighter2.ap, "attack point(s)")

                 if fighter1.hp <= 0:
                     print(fighter1.name, "is dead")
                     fighter1.alive = False
                     break

                 print("Statistic after round:",)
                 statistic_print(fighter1)

            elif decision == "r":
                break
            else:
                print("You have to choose between attack and run!")
    else:
        while True:
            print(fighter2.name,"has more luck and will attack first!")
            fighter1.hp = int(fighter1.hp) - int(fighter2.ap)
            print(fighter2.name, "attack and hit ", fighter1.name, "with", fighter2.ap, "attack point(s)")

            if fighter1.hp <= 0:
                print(fighter1.name, "is dead")
                fighter1.alive = False
                break

            decision = input("It is your move. What do you want to do? Attack or Run a/r >>")

            if decision == "a":
                fighter2.hp = fighter2.hp - fighter1.ap
                print(fighter1.name, "attack and hit ", fighter2.name,"with", fighter1.ap, "attack point(s)")

                print("Statistic after round:", )
                statistic_print(fighter1)

                if fighter2.hp <= 0:
                    print(fighter2.name, "is dead and you have get a key")
                    player_items.append("key")
                    fighter1.alive = False
                    break

            elif decision == "r":
                break


goblin = Character("Goblin", 10, 3, 4, True)
player = Character("Hero", 8, 5, 5, True)
player_items = []

map[0][1] = "1"
map[1][0] = "2"
map[1][1] = "X"
map[1][2] = "3"

map_exploring()