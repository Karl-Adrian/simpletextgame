answer = input("would you like to play? (yes/no) ")
yes
if answer.lower().strip() == "yes":

    answer = input("You reach at a junction, you going (left or right)").lower().strip()
    if answer == "left":
        answer = input("You meet a monster, he's running towards you, you run or attack?")

        if answer == "attack":
            print("you really thought that was a great idea? anyways, you died!")
        else:
            print("Good choice you made it to safety")
            answer = input("You see a plane in an open field, seems like it's in good condition, do you fly it or run?")

            if answer == "fly":
                print("Bruh, you don't know how to fly a plane, you dead lol")
            else:
                print("As you continue running you see a group of people sitting by a campfire,")
                answer = input("you run toward them panting like crazy"
                                " you tell them about the monster that's following you, they laugh and say they can"
                                " defeat the monster, wyd? stay or run?")
                if answer == "stay":
                    print("They provide you with a handgun for self-defense, you hear the monster's roar as it"
                          "closes in on you, you shiver in fear but your new friends seem confident, they really"
                          "want to take this beast down, having second thoughts? Well it's already too late to change"
                          " your mind as the monster appears and spots you, you manage to get in a few shots but this "
                          "monster is just too powerful, it rips apart your friends like paper then charges towards you"
                          "You start regretting on why you decided to stay, before you could even scream, your head is"
                          " way off your body...dead")
                else:
                    print("You reject their offer and run, leaving them for dead, sad")
                    answer = input("You spot a warehouse and run to hide in it, you hear the screams of the group you "
                                   "left behind, you hide behind some equipment, the monster bashes in, it nears your "
                                   "position wyd? stay quiet or distract it?")

                    if answer == "stay quiet":
                        print("you hold your breath as you keep as quiet as possible, the monster passes your position "
                              "You sigh in relief, but you sighed too goddamn loud, the monster turns and grabs you "
                              "by the neck, you dead")
                    else:
                        print("You see a metal rod lying beside you and you throw it as far as possible, the monster"
                              " runs towards the noise, you take that chance to escape but you trip and fall, too bad"
                              " that fall made alot of noise, your body is ripped in half before you even try to "
                              "scream")

elif answer == "right":
            answer = input("Today just isn't your day, is it? you just encountered a bear and it's hungry for your"
                           " blood, wyd, stay and try to fight or run like the sorry coward you are?")
            if answer == "fight":
                print("you muster the strength to fight, you see a nearby steak and you charge at the bear filled with"
                      " rage, you stab it in the eye and it howls in pain, it drops, slowly dying, you cheer as you"
                      " run, trying to find your way back home")
            else:
                print("you run as fast as possible, you see a cottage, you go hide in it. The house looks good, but"
                      " something's just not right, you hear the bear's heavy breathing outside looking for you, "
                      "you step on a crack on the floor, the bear looks towards you through a window, the bear bashes"
                      " the door and lunges towards you.")
                answer = input("you picking up the gun or you flee?")
                if answer == "gun":
                    print("you reach for the gun but the bear grabs a hold of your foot and drags you, you try to reach "
                       "once more but the bear's strength is too much. The bear grabs your neck and rips your head off."
                       " R.I.P")
                else:
                    print("Just before you leave through the back door, you get stopped by a floating, glowing figure. "
                          "you cannot identify what it is. I grabs your hand and flies you away from danger, after you "
                          "reach to safety, the glowing diminishes and you're able to see that it's a female, she has "
                          "wings and pointed ears, she explains that she's a Pixie called Chi, she explains that she "
                          "can save you from everything by taking you to a world where everything is perfect free from "
                          "harm")
                    answer = input("You see this offer as too good to be true, she offers her hand do you take the hand? "
                                   "or run away")
                    if answer == "run away":
                        print("You scream as loud as you can and run away for your life, the pixie giggles and snaps "
                              "her fingers, then out of nowhere the bear emerges again and runs toward you so fast and "
                              "rams you to the ground, breaking all your bones. You lay there paralysed, watching as "
                              "the  bear devours you piece by piece, you regret not taking the pixie's hand, you fade "
                              "off......Goodbye")
                    else:
                        print("She takes your hand and whisks you away with such a high speed you go unconscious, you "
                              "wake up in a world that you would only see in a dream. The air was fresh, sun shining "
                              "the sweet smell of apple pie, and the happiness of the people there. You finally found "
                              "peace.")

print("Game over!")