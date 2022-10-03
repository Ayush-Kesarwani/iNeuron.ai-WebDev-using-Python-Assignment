import random

def WordPuzzelGame(wrd,score):
    random_letters_list=random.sample(wrd,k=len(wrd))
    random_letter_word=''.join(random_letters_list)
    print("\nSolve the puzzel by guessing the correct word : ")
    print(random_letter_word)
    userInput=input()
    if userInput.upper()==wrd:
        print("Yay! You gussed it right.")
        score+=1
    else:
        print("Alas! You gussed it wrong.")
        score-=1
    return score


words=["DARJEELING","MYSORE","CHANDIGARH","HIMALAYAN","BANGALORE"]
words=random.sample(words,k=len(words))
score=0

for word in words:
    score=WordPuzzelGame(word,score)

print()
print("Your total score : ",score)