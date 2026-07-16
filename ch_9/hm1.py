import random
def game():
    print("you are playing the game...")

    score = random.randint(1,100)
    print(f"Your score is : {score}")

    with open("high_score.txt") as f:
        highscore = f.read()

        if(highscore==""):
            highscore=0
        else:
            highscore = int(highscore)
    
    if(score>highscore):
        with open("high_score.txt", "w") as f:
            f.write(str(score))

    return score

game()