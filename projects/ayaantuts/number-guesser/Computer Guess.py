LOW, HIGH = 1, 100

def play():
	print(f"Think of a number between {LOW} and {HIGH} (inclusive). I will try to guess it!")
	input("Press Enter when you're ready...")

	low, high = LOW, HIGH
	attempts = 0

	while low <= high:
		attempts += 1
		guess = (low + high) // 2
		response = input(f"My guess is {guess}. Is it too low (L), too high (H), or correct (C)? ").lower()

		if response == 'c':
			print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
			return
		elif response == 'l':
			low = guess + 1
		elif response == 'h':
			high = guess - 1
		else:
			print("Invalid input. Please respond with L, H, or C.")

	print("Hmm, it seems there was a misunderstanding. Let's try again!")

if __name__ == "__main__":
	print("Welcome to the Computer Number Guessing Game!")
	print(f"The default bounds are {LOW} to {HIGH}.")
	default = input("Do you want to change bounds? (Y/N): ")
	if default.lower() == 'y':
		LOW = int(input("Enter the lower bound: "))
		HIGH = int(input("Enter the upper bound: "))
	play()