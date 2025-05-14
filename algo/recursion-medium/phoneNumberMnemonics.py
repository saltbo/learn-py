DIGIT_LETTERS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def phoneNumberMnemonics(phoneNumber):
    mnemonicsFound = []
    currentMnemonics = [""] * len(phoneNumber)
    helper(0, phoneNumber, currentMnemonics, mnemonicsFound)
    return mnemonicsFound


def helper(idx, phoneNumber, currentMnemonics, mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic = "".join(currentMnemonics)
        mnemonicsFound.append(mnemonic)
        return

    digit = phoneNumber[idx]
    letters = DIGIT_LETTERS[digit]
    for letter in letters:
        currentMnemonics[idx] = letter
        helper(idx+1, phoneNumber, currentMnemonics, mnemonicsFound)


phoneNumber = "1905"
print(phoneNumberMnemonics(phoneNumber))
