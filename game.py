import random
word_bank=['Hello','College',"education",'Christ','Xmas','Love','faithfulness','goodness','what','no']
word=random.choice(word_bank).lower()
guessed_word=['_']*len(word)
attempts=5
while attempts>0:
    print('\nCurrent Word: '+' '.join(guessed_word))
    guess=input('Guess a letter:').lower()
    if guess in word:
        for i in range(len(word)):
            if(word[i]==guess):
                guessed_word[i]=guess
        print('Correct Guess')
    else:
        attempts-=1
        print('Wrong Guess Attempts left: '+str(attempts))
    if '_' not in guessed_word:
        print('\nCongratulations! You have guessed the word correctly. It was:',word)
        break
if attempts==0:
    print('\nYou have exhausted all attempts. The correct word is: ',word)