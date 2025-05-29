print()
print("----------------------------------------------------------------")
print()
print("You stand in front of your first dungeon, you notice it is small."); print();print(f"But don't underestimate it, the dungeon just might give you some trouble...");print();print(f"You enter the first floor of the dungeon.")
l = "left"
r = "right"
decision_1 = input("Do you turn LEFT or RIGHT? ")
if decision_1 == l or "left":
    print()
    print(f'You turn left and find yourself standing before an old man in ragged clothes. He says to you "Please great knight, spare me a piece of bread and drink for my troubles".');print();print(f"What do you do?")
    
    h = "help him"
    i = "ignore him and continue"
    decision_2 = input("Do you HELP HIM or IGNORE HIM AND CONTINUE? ")
    print()
    if decision_2 == "help" or "h":
        print(f"As you lean down to assist the beggar, he suddenly changes form to a mimic and attacks you.")
        a = "fight back"
        b = "run away"
        decision_3 = input("Do you FIGHT BACK or RUN AWAY? ")
        print()
        if decision_3 == a or "fight back":
            print(f"wow... You would hit an old man?")
        else:
            print(f"what a wimp.")
    else:
        print(f"You walk past the beggar and think nothing of him..."); print();print("...but then you feel the urge to look back. Looking back behind you, you see that the old man has suddenly disappeared.");print();print(f"You feel someone breathing on your neck");print(f"What do you do? ")
        
        r = "run away"
        t = "turn around"
        decision_3 = input("Do you RUN AWAY or TURN AROUND? ")
        print()
        if decision_3 == r or "run away":
            print(f"You run towards the exit without looking back and make it to the entrance.")
        else:
            print(f"Before you get the chance to see what peers over you, your legs fall to the floor and you find yourself unable to move.")
else:
    print()
    print(f"You hit a wall...");print(f"Dummy...");print();print(f"You now turn around and continue down the hall heading left like you should have in the first place.")
    print()
    print(f'After walking down the long hall, you find yourself standing before an old man in ragged clothes. He says to you "Please great knight, spare me a piece of bread and drink for my troubles".');print();print(f"What do you do?")
    
    h = "help"
    i = "ignore and continue"
    decision_2 = input("Do you HELP HIM or IGNORE HIM AND CONTINUE? ")
    print()
    if decision_2 == h or "help him":
        print(f"As you lean down to assist the beggar, he suddenly changes form to a mimic and attacks you.")
        
        f = "fight him"
        r = "run away"
        decision_3 = input("Do you FIGHT HIM or RUN AWAY? ")
        print()
        if decision_3 == f or "fight him":
            print("*WAM*...*BAM*...*THANK YOU MAM*...");print(f"You defeat the mimic.");print(f"+12 gold");print(f"+6 exp")
    else:
        print(f"You walk past the beggar and think nothing of him..."); print();print("...but then you feel the urge to look back. Looking back behind you, you see that the old man has suddenly disappeared.");print();print(f"You feel someone breathing on your neck")
        
        r = "run away"
        t = "turn around"
        p = "pray"
        decision_3 = input("Do you RUN AWAY, TURN AROUND or PRAY? ")
        print()
        if decision_3 == r or "run away":
            print(f"You run towards the exit without looking back and make it to the entrance.")
        if decision_3 == p or "pray":
            print(f"You kneel down to pray to your God before the end comes for you. Before you finish your sentence, the mimic swallows you up whole and you become food for the dungeon")
        else:
            print(f"Before you get the chance to see what peers over you, your legs fall to the floor and you find yourself unable to move.")
    
print();print()
print(f"The end")