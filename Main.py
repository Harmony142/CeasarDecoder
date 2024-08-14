def main():
    cipher = input("Please enter the string to be decoded.\n").upper()
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let_acco = {}  # letter of the alphabet associated with each number
    num_acco = {}  # number associated with each letter of the alphabet
    num = 0

    # Build two dictionaries, one that associates a letter with its numeric value
    # and one that associates a numeric value with its

    for letter in alph:
        let_acco[num] = letter
        num_acco[letter] = num
        num += 1
    decrypt(cipher, let_acco, num_acco)

def decrypt(cipher, let_acco, num_acco):
    shift = 1
    plaintext = ""
    while shift < 25:
        for letter in cipher:
            if letter == " ":
                plaintext = plaintext + " "
            elif num_acco[letter] - shift >= 0:
                attempt_shift = num_acco[letter] - shift
                plaintext = plaintext + let_acco[attempt_shift]
            else:
                attempt_shift = 26 + (num_acco[letter] - shift)
                plaintext = plaintext + let_acco[attempt_shift]
        print(plaintext,'\n')
        plaintext = ""
        shift += 1

if __name__ == '__main__':
    main()