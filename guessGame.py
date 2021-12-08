import random 
try :
    while True :
        number = float(random.randint(0,100))    
        print("..........GUESS GAME..........\n")
        print("to PLAY enter \"Y\" or \"Q\" for QUIT ")
        inp = input(">>> ").lower() 
        i = 0
    
        if inp ==  "y" :
            print("INTRO : you have to guess a number between 0 and 100 ")
            while True :
                guessed_number = float(input("GUESS NUMBER : "))
                if guessed_number == number :
                    print("what a nice guess ....\n you WON thhis game")
                    print("what a nice guess ....\n you WON thhis game")
                    print("what a nice guess ....\n you WON thhis game")
                    print("..congrats..\n")
                    print("*       *      * ")
                    print("  *     *     *  ")
                    print("    *   *   *    ")
                    print("      * * *      ")
                    print("* * * * * * * * *")
                    print("      * * *      ")
                    print("    *   *   *    ")
                    print("  *     *     *  ")
                    print("*       *      * \n")
                    i += 1
                    print(f"you completed this game in {i} steps !\n")
                    break
                elif guessed_number > number :
                    print("too high..")
                    i += 1
                elif guessed_number < number :
                    print("too low..")
                    i += 1
        if inp == "q" :
            print("thanks for playing...\n")
            break
        else :
            print("please enter VALID INPUT \n")
except : 
    print("you did something wrong , please try again")
