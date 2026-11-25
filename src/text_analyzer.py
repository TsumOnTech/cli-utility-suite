def getText():        
    Text = input("Enter a text: ")
    while not Text.strip():
        print("Text cannot be empty")
        Text = input("Enter a text: ")
    return Text
def word_count(Text):
    number_of_words = 0
    sentence = Text.split()
    for word in sentence:
        number_of_words += 1
    return number_of_words
def character_count(Text):
    number_of_characters = 0
    for character in Text:
        if not character.isspace():
            number_of_characters += 1
    return number_of_characters
def vowel_count(Text):
    vowels = "aeiou"
    number_of_vowels = 0
    for character in Text:
        if character.lower() in vowels:
            number_of_vowels += 1
    return number_of_vowels
def digit_count(Text):
    number_of_digits = 0
    for character in Text:
        if character.isdigit():
            number_of_digits += 1
    return number_of_digits
def uppercase_count(Text):
    uppercasecount = 0
    for character in Text:
        if character.isupper():
            uppercasecount += 1
    return uppercasecount
def lowercase_count(Text):
    lowercasecount = 0
    for character in Text:
        if character.islower():
            lowercasecount += 1
    return lowercasecount
import string 
def word_frequency(text):
    frequency = {}
    for word in text.split():
        word = word.lower().strip(string.punctuation)
        if word == "":
            continue
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def main():
    Text = getText()
    while True:
        print("\n=== Text ANALYZER ===")
        print("1.Find the number of words")
        print("2.Find the number of characters")
        print("3.Find the number of vowels")
        print("4.Find the number of digits")
        print("5.Find the number of uppercase letters")
        print("6.Find the number of lowercase letters")
        print("7.Find the word frequency")
        print("8.EXIT")
        while True:
            try:
                choice = int(input("Which operation would you like to do: "))
                break
            except ValueError:
                print("Wrong input")
            
        if choice == 1:
            number_of_words = word_count(Text)
            print("The number of words is: ", number_of_words)
        elif choice == 2:
            number_of_characters = character_count(Text)
            print("The number of characters is: ", number_of_characters)
        elif choice == 3:
            number_of_vowels = vowel_count(Text)
            print("The number of vowel is: ", number_of_vowels)
        elif choice == 4:
            number_of_digits = digit_count(Text)
            print("The number of digits is: ", number_of_digits)
        elif choice == 5:
            uppercasecount = uppercase_count(Text)
            print("The number of uppercase letters is(are) : ", uppercasecount)

        elif choice == 6:
            lowercasecount = lowercase_count(Text)
            print("The number of lowercase letters is(are) : ", lowercasecount)
        elif choice == 7:
            frequency = word_frequency(Text)
            print(frequency)
        elif choice == 8:
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid option, please choose among the available options")

if __name__ == "__main__":
    main()








