import random
correct=random.randint(1,10)
def numberguess():
  guess=int(input("Guess a number"))
  if guess>10 or guess<1:
    print("from 1 to 10")
    numberguess()
  elif guess==correct:
    print("Correct!")
  else:
    print("Try again.")
    numberguess()
numberguess()