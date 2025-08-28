# Country Guessing Game

This is a fun and interactive country guessing game built using Python and the Tkinter library. The game randomly selects a country and replaces some letters in its name with underscores (`_`). The player must guess the missing letters to complete the country name.

## Features
- Randomly selects a country from a predefined list.
- Dynamically replaces letters with underscores.
- Provides up to 3 chances to guess the correct letters.
- Displays messages for correct and incorrect guesses.
- Restarts with a new country after the game is over.

## How to Play
1. Run the program.
2. A country name with missing letters will be displayed.
3. Enter a letter in the input box and click "Submit".
   - If the letter is correct, it will be filled in the appropriate positions.
   - If the letter is incorrect, you lose one chance.
4. The game ends when:
   - You fill in all the missing letters correctly.
   - You run out of chances.
5. A message box will display the result, and a new game will begin.

## Prerequisites
- Python 3.x
- Tkinter (comes pre-installed with Python on most platforms)

## Installation
1. Clone or download this repository.
2. Ensure you have Python 3.x installed on your system.

## Running the Game
1. Open a terminal or command prompt.
2. Navigate to the directory containing the game script.
3. Run the script using the following command:
   ```
   python main.py
   ```
   Replace `main.py` with the name of the script file.

## File Description
- `main.py`: The main Python script containing the logic for the country guessing game.

## Code Explanation
1. **Country List**: Contains a comprehensive list of country names.
2. **Random Country Selection**: Uses Python's `random` library to select a country randomly.
3. **Generate Question**: Replaces random letters in the selected country name with underscores (`_`).
4. **User Interaction**: Captures user input via a Tkinter GUI.
5. **Answer Validation**: Checks if the guessed letter is correct and updates the displayed country name.
6. **Game Logic**: Tracks the number of chances and determines the game's outcome.

## Dependencies
- **random**: Used to select a random country and generate missing letters.
- **tkinter**: Used to create the graphical user interface.
- **messagebox**: Provides feedback to the user with pop-up messages.

## Customization
- You can add or remove countries from the `countries` list in the `get_country()` function.
- Adjust the appearance of the GUI by modifying parameters in the Tkinter widget constructors.

## Example Output
1. **Initial Screen**:
   - `Fill the blank space for this country: G__rmany`
2. **Correct Guess**:
   - Message box: "Correct!"
   - Updated country: `Ge_rmany`
3. **Incorrect Guess**:
   - Message box: "Incorrect!"
   - Remaining chances: 2
4. **Game Over**:
   - Message box: "Game Over! The correct country was Germany"

## Acknowledgements
This game is designed to help improve geographic knowledge in an engaging way. Inspired by word-guessing games, it adds an educational twist with country names.

Enjoy the game!


## 💡 Credits

Made by [Abhay Surya K S](https://github.com/AbhaySuryaKS/) 
