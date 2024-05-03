from itertools import permutations

def getUnique(words, sum_word):
    dictionary = []
    for word in words:
        for letter in word:
            if letter not in dictionary:
                dictionary.append(letter)
    for letter in sum_word:
        if letter not in dictionary:
            dictionary.append(letter)
    return dictionary

def wordSum(word, possibility):
    total = 0
    i = 0
    for letter in word[::-1]:
        total += possibility[letter]*(10**i)
        i += 1
    return total

def main():
    words = [word.strip().lower() for word in input("Enter the words(Comma separated):").split(",")]
    sum_word = input("Enter the sum word: ").strip().lower()
    letters = getUnique(words, sum_word)
    if len(letters) > 10:
        print("The no such combination since the number of unique characters are greater than number of digits")
        return
    possibilities = list(permutations(list(range(10)), len(letters)))
    count = 0
    for possibility in possibilities:
        possibility = {letters[i]: possibility[i] for i in range(len(possibility))}
        if sum([wordSum(i, possibility) for i in words]) == wordSum(sum_word, possibility):
            print("True")
            print("\n\nOne of the possibility is: ")
            # print(possibility)
            for letter in possibility.keys():
                print(f"{letter.upper()} => {possibility[letter]}")
            return
    print("False")
    
if __name__ == "__main__":
    main()