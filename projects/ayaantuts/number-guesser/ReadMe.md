# Number Guessing Game Suite 🎮

This project is a small suite of two Python-based number guessing games. The first, **Computer Guesses**, features a computer using a binary search algorithm to guess a number thought of by the user. The second, **Human Guesses**, is the classic game where the user tries to guess a randomly selected number.

The games are designed for simplicity and demonstrate fundamental programming concepts like loops, conditional statements, and user input handling, and the **Computer Guesses** game illustrates the power of the **Binary Search** algorithm.

-----

## Files in the Repository

| File | Description | Algorithm |
| :--- | :--- | :--- |
| `Computer Guesses.py` | The computer attempts to guess the number the user is thinking of. | **Binary Search** |
| `Human Guesses.py` | The user attempts to guess a random number selected by the computer. | **Random Selection** |

-----

## How to Run the Games

Both games are written in Python and can be run from your terminal.

### Prerequisites

You need to have **Python 3** installed on your system.

### Running the Computer Guesses Game

1.  Open your terminal or command prompt.
2.  Navigate to the directory where the file is saved.
3.  Run the script:
    ```bash
    python "Computer Guesses.py"
    ```
4.  Follow the on-screen prompts to set the bounds (default is $1$ to $100$) and provide feedback to the computer's guesses (`L` for too low, `H` for too high, `C` for correct).

### Running the Human Guesses Game

1.  Open your terminal or command prompt.
2.  Navigate to the directory where the file is saved.
3.  Run the script:
    ```bash
    python "Human Guesses.py"
    ```
4.  Follow the on-screen prompts to set the bounds (default is $1$ to $100$) and start guessing\!

-----

## Game Details and Logic

### 1\. Computer Guesses (`Computer Guesses.py`)

This game showcases the **Binary Search** technique.

  * **Logic:** The computer maintains a range (`low` and `high` bounds) and always guesses the midpoint.
      * If the user says the guess is **Too Low (L)**, the computer eliminates the lower half of the range by setting `low = guess + 1`.
      * If the user says the guess is **Too High (H)**, the computer eliminates the upper half by setting `high = guess - 1`.
  * **Efficiency:** Because the search space is cut in half with every guess, the computer is guaranteed to find any number in the default range ($1$ to $100$) in at most **7 attempts** ($\lceil\log_2(100)\rceil = 7$).

### 2\. Human Guesses (`Human Guesses.py`)

This is a classic "higher or lower" guessing game.

  * **Logic:** The computer selects a random integer within the set bounds using `random.randint()`.
  * **Gameplay:** The user inputs their guess, and the computer provides feedback (`Too low!` or `Too high!`) until the correct number is found. The number of attempts is tracked.