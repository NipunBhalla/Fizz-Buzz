import random
import timeit
while True:
    first_go = random.randint(0,1)
    if first_go == 0:
        computer_go = True
    else:
        computer_go = False
    print("FIZZ BUZZ\
            \n==============================================RULES================================================\
            \n===================================================================================================\
            \nIf the number is divisible by 3, type FIZZ            || Level Description:\
            \nIf the number is divisible by 5, type BUZZ            || EASY     >> 5 Lives / 10 Seconds to answer\
            \nIf the number is divisible by 3 and 5, type FIZZ BUZZ || NORMAL   >> 3 Lives / 7 Seconds to answer\
            \nIf the number is none of the above, type the number   || HARDCORE >> 1 Life  / 5 Seconds to answer\
            \n\nYou have limited Lives and then the game is over.\
            \nYou have to answer quickly or else the time will run out.\
            \n===================================================================================================\n")
    while True:
        level = input("Level Select: (1)Easy, (2)Normal, (3)HardCore! (1/2/3): ")
        if level in ('1', '2', '3'):
            break
        print ('Invalid input.')
    level =int(level)
    if level == 1:
        lives = 5
        t_out = 10
    elif level == 2:
        lives = 3
        t_out = 7
    elif level == 3:
        lives = 1
        t_out = 5
    input("Press Enter to START! \n")
    score = 0
    for number in range(1,10000):
        if number % 3 == 0 and number % 5 == 0:
            correct_answer = "FIZZ BUZZ"
        elif number % 3 == 0:
            correct_answer = "FIZZ"
        elif number % 5 == 0:
            correct_answer = "BUZZ"
        else:
            correct_answer = str(number)
        if computer_go == True:
            print("\nCPU    :", correct_answer)
            computer_go = False
        elif computer_go == False:
            start_time = timeit.default_timer()
            answer = input("Your go: ")
            elapsed = timeit.default_timer() - start_time
            answer = answer.upper()
            if elapsed >= t_out:
                print('\nTime elapsed : ' +str(elapsed)+ ' seconds')
                print('Timeout! Game Over.\n')
                break             
            if answer == correct_answer:
                computer_go = True
                score = score + 1
            else:
                print("CPU    : "+correct_answer+"\n                Wrong answer!" , end=' ')
                lives = lives-1
                if lives >=0:
                    print("Lives remaining: " +str(lives))
            if lives < 0:
                print('\n\n===================================================================================================\
                    \nGame over! \
                    \n===================================================================================================\n\n')
                break
    while True:
        print("Your Score: "+str(score*10)+ " \n\n")
        ans = input('\nPlay again? (y/n): ')
        ans = ans.upper()
        if ans in ('Y', 'N'):
            break
        print ('Invalid input.')
    if ans == 'Y':
        print("\n\n")
        continue
    else:
        print("\n\n")
        print ('See ya LOOSERRRRRR!!!')
        break