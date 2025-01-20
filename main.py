DASH = "---"
DOT = "."
SPACE = " "
SPACE_BETWEEN_LETTERS = "   "
SPACE_BETWEEN_WORDS = "       "
MORSE_CODE_DICT = {
    "A": DOT + SPACE + DASH,
    "B": DASH + SPACE + DOT + SPACE + DOT + SPACE + DOT,
    "C": DASH + SPACE + DOT + SPACE + DASH + SPACE + DOT,
    "D": DASH + SPACE + DOT + SPACE + DOT,
    "E": DOT,
    "F": DOT + SPACE + DOT + SPACE + DASH + SPACE + DOT,
    "G": DASH + SPACE + DASH + SPACE + DOT,
    "H": DOT + SPACE + DOT + SPACE + DOT + SPACE + DOT,
    "I": DOT + SPACE + DOT,
    "J": DOT + SPACE + DASH + SPACE + DASH + SPACE + DASH,
    "K": DASH + SPACE + DOT + SPACE + DASH,
    "L": DOT + SPACE + DASH + SPACE + DOT + SPACE + DOT,
    "M": DASH + SPACE + DASH,
    "N": DASH + SPACE + DOT,
    "O": DASH + SPACE + DASH + SPACE + DASH,
    "P": DOT + SPACE + DASH + SPACE + DASH + SPACE + DOT,
    "Q": DASH + SPACE + DASH + SPACE + DOT + SPACE + DASH,
    "R": DOT + SPACE + DASH + SPACE + DOT,
    "S": DOT + SPACE + DOT + SPACE + DOT,
    "T": DASH,
    "U": DOT + SPACE + DOT + SPACE + DASH,
    "V": DOT + SPACE + DOT + SPACE + DOT + SPACE + DASH,
    "W": DOT + SPACE + DASH + SPACE + DASH,
    "X": DASH + SPACE + DOT + SPACE + DOT + SPACE + DASH,
    "Y": DASH + SPACE + DOT + SPACE + DASH + SPACE + DASH,
    "Z": DASH + SPACE + DASH + SPACE + DOT + SPACE + DOT,
    "1": DOT + SPACE + DASH + SPACE + DASH + SPACE + DASH + SPACE + DASH,
    "2": DOT + SPACE + DOT + SPACE + DASH + SPACE + DASH + SPACE + DASH + SPACE,
    "3": DOT + SPACE + DOT + SPACE + DOT + SPACE + DASH + SPACE + DASH,
    "4": DOT + SPACE + DOT + SPACE + DOT + SPACE + DOT + SPACE + DASH,
    "5": DOT + SPACE + DOT + SPACE + DOT + SPACE + DOT + SPACE + DOT,
    "6": DASH + SPACE + DOT + SPACE + DOT + SPACE + DOT + SPACE + DOT,
    "7": DASH + SPACE + DASH + SPACE + DOT + SPACE + DOT + SPACE + DOT,
    "8": DASH + SPACE + DASH + SPACE + DASH + SPACE + DOT + SPACE + DOT,
    "9": DASH + SPACE + DASH + SPACE + DASH + SPACE + DASH + SPACE + DOT,
    "0": DASH + SPACE + DASH + SPACE + DASH + SPACE + DASH + SPACE + DASH
}


def start_text_to_morse_code():
    while True:
        text = input("What do you want to convert to morse code? Press q to exit")
        if text == "q":
            return
        print("Converting to morse code...")
        convert_to_morse_code(text)


def convert_to_morse_code(text):
    words = text.split(" ")
    converted_text = ""
    for word in words:
        for char in word.upper():
            converted_text = converted_text + MORSE_CODE_DICT.get(char, "?") + SPACE_BETWEEN_LETTERS
        converted_text = converted_text.strip()
        converted_text += SPACE_BETWEEN_WORDS
    return converted_text.strip()


if __name__ == '__main__':
    start_text_to_morse_code()
