print("Welcome to Quiz Game!")

play = input("Do you wanna play? (yes/no):")

if play.lower() != "yes":
    quit()

print("Okay Let's play! :)")
Score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")


answer = input("What does NPU stand for? ")
if answer.lower() == "neural processing unit":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")


answer = input("What type of memory is RAM? ")
if answer.lower() == "primary memory":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

print(f"You got {Score} questions correct!")
print(f"You got {(Score / 4) * 100}%.")