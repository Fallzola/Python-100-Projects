import sys

print("""                  ,;;;:.
                          ;;''''`:
                          ;(  O O|              ,;;,
                           |   _\|              \  |
                            \__-/              ,' /
                            |   |             /  /
                      _,--''`---'''-------.,-'  /
                    ,'  /          `.     |  _,'
                  ,'    |====== WM =|     |-'
                 \      ,======|  |=|''---'
                / `.  ,' \      \/ /
              ,'. ,'`'   | --._    |
            ,'  ,'       |         |
        __,' _,'         \    -._  |
       `- ,-'            |---------)
      ';;'               ;:::::::::|
                        ;:::::::::::\
                       /::::::;:::::|
                      /_:::::/\:::::_\
                      / `-:_/  \,-' |
                     /    /     \   |
                     |   |      | _,)
                     \_,-\      |   |
                      \   |     |   |
                       |__|      \,-|
                       /##|      |  |
                      \##/       |  |
                     ,-'''-.     |,-|
                    // \_/ \\    `.##\
                    |\_/ \_/|      `--`
           jrei     \/ \_/ \/
                     `-...-'
                     """)

print("Welcome to the Soccer Final! Make the right decisions and win the world cup!")
decision1 = input("You receive the ball in the middle of the camp, you can either\n[1]Pass the ball quickly\nor\n[2]Try to carry the ball yourself\n:")
if decision1 == "1":
    print("You make a quick pass, but because your ally is so far, the enemy team intercepts the ball and make a goal, you lost 🐦")
    sys.exit()
elif decision1 == "2":
    print("You decide to carry the ball, and after a few meters, a defender tries to steal it from you, what do you do?")
    decision1 = input("[1]Pass the ball\n[2]Try to dribble him\n:")
    if decision1 == "1":
        print("You pass the ball and now your teammate is in a 1v1 with the goalie, where should he shoot?")
        decision1 = input("[1]Powershot on the left\n[2]Panenka the goal keeper\n:")
        if decision1 == "1":
            print("He powershots but the keeper catches it early, and now he misses the goal, you lost 🐦")
            sys.exit()
        elif decision1 == "2":
            print("The keeper expected a powershot and the panenka worked! He made the goal and you won! 🔥")
        else:
            print(f"There is no such decision as {decision1}")
    elif decision1 == "2":
        print("After trying to dribble him, you lost the ball and after quick passes from the enemy team, they made a goal, you lost 🐦")
        sys.exit()
else:
    print("There is no such decision as {decision1}")