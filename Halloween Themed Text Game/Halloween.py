while True:
    answer = input('Would you like to play this haloween themed game? (yes/no)? ').lower().strip()
    if answer == 'yes':
        print('''Congrat's you have choosen to pay this adventure game, Warning play at your own risk''')
        answer = input('''It's Halloween night, you and your frinds, bill and joe have choosen an outfit your turn. (bee/grim reaper/ghost) ''').lower().strip()
        if answer == 'bee':
            input('You have choosen to be a bee, you and your friend continue to plan thier halloween. bill says lets go the the rich houses. joe says lets go early and hit all the houses. who do you pick? (bill/joe) ').lower().strip()
        elif answer == 'grim reaper':
            answer = input('You have choosen to be a grim reaper, you and your friend continue to plan thier halloween. bill says lets go the the rich houses. joe says lets go early and hit all the houses. who do you pick? (bill/joe) ').lower().strip()
            if answer == 'joe':
                print('bill will remebmer this. you decide to go to all the houses early')
                answer = input('you and your friends choose to perseve thier energy for the afternoon. 2 hours pass. you both decide to go the all the houses in the nieborhood. on the way you encouter and old lady who tells you to be wary. What do you do? (ignore/accept) ').lower().strip()
                if answer == 'accept':
                    print('Good job for heading the warning, but no halloween for you.')
            elif answer == 'ignore':
                print('You have choosen to ignore the warnings. on the way to the first house you get diarrhea, and go back home.')
            elif answer == 'bill':
                print('joe will remebmer this. you decide to go to all the rich houses')
                answer = input('you and your friends choose to perseve thier energy for the afternoon. 2 hours pass. you both decide to go the richest house in the nieborhood. on the way you encouter and old lady who tells you to be wary. What do you do? (ignore/accept) ').lower().strip()
                if answer == 'accept':
                    print('You decide to turn back and try again next halloween. R.I.P.')
                elif answer == 'ignore':
                        answer = input('You continue to walk down the path. when you see the simpsons house A.K.A. the rich house. They are giving out entire full sized candy boxes. no wonder all the cady stores were sold out. you come to approch Mr. simpson at the door. What do you do? (run/ask/trick) ').lower().strip()
                        if answer == 'run':
                            print('You ran away from the best house in the world why???')
                        elif answer == 'ask':
                            answer = input('You ask Mr. simpson for candy but he says you need to complete his maze in order to get a box. as you and your friend continue down the road. You have 3 options (left/straight/right) ').lower().strip()
                            if answer == 'left':
                                        print('You Have Choosen Left, Try Again Next Time.')
                            elif answer == 'right':
                                        print('You have choosen right, why?')
                            elif answer == 'straight':
                                        answer = input('You have choosen to go straight ahead and have found an exit what do you do? (enter/continue forward) ').lower().strip()
                                        if answer == 'enter':
                                                print('You have walked into a room full of lava did you think it was that easy?')
                                        elif answer == 'continue forward':
                                                answer = input('continuing forward you come towards two days what do you do? (left/right) ').lower().strip()
                                                if answer == 'left':
                                                    print('That was not the "Right "answer"')
                                                elif answer == 'right':
                                                    answer = input('You choose the "Right" answer good job you stumble upon a choise. get 200 candies every weekend or, get 1000 candies right now. (200/1000) ').lower().strip()
                                                    if answer == '200':
                                                        answer = input('You choose how many candies? (10400/1200) ').lower().strip()
                                                        if answer == '1200':
                                                            print('200 x 52 is not 1200, try again. ')
                                                        elif answer == '10400':
                                                            print('''Congrats. You have won a lot of candy for halloween hope you don't get a sweet tooth. Thanks for playing.''')
                                                    elif answer == '1000':
                                                        print('Why did you do this to your self?')
                        elif answer == 'trick':
                            print('You trick the simpsons and they ban you from thier property. Bruh Moment')
        elif answer == 'ghost':
            print('Your friends think you are lame, they leave you by your self T_T. You Lose')
            if answer == 'joe':
                print('bill will remebmer this. you decide to go to all the houses early')
    else:
        print('''That's too bad, maybe you'll play next time?''')
        break
