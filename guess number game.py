import random

def guess(x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        guess = int(input (f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print("sorry, the number is too low, guess again.")
        elif guess > random_number:
            print("sorry, the number is too high, guess again.")
    
    print(f'Yay, congrats. You guessed the number {random_number} right!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        if low != high:
           guess = random.randint (low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too High (H), too Low(L), or Correct(C)??') .lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
        
    print(f'Yay, the computer guessed your number, {guess}, correctly!')

computer_guess(1000) # you can change the variable to change the game, make it guess() to play the first game and computer_guess() to play the second game