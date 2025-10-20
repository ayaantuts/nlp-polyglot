import random

# Update the bound variables to select random number
LOW, HIGH = 1, 100

def play():
	guess = random.randint(LOW, HIGH)
	attempts = 0
	while True:
		humanGuess = int(input(f"Guess a number between {LOW} and {HIGH}: "))
		attempts += 1
		if humanGuess < guess:
			print("Too low! Try again.")
		elif humanGuess > guess:
			print("Too high! Try again.")
		else:
			print(f"Congratulations! You've guessed the number {guess} in {attempts} attempts.")
			break

if __name__ == "__main__":
	print("Welcome to the Number Guessing Game!")
	print(f"The default bounds are {LOW} to {HIGH}.")
	default = input("Do you want to change bounds? (Y/N): ")
	if default.lower() == 'y':
		LOW = int(input("Enter the lower bound: "))
		HIGH = int(input("Enter the upper bound: "))
	play()