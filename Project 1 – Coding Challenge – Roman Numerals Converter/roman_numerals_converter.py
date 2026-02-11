def convert_to_roman(number):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result= ""
    for value, symbol in roman_numerals:
        while number>= value:
            result+= symbol
            number-= value
    return result

def main():
    print("Hello, Welcome to Convert to Roman Numerals -Hands on Project") 
    print("-"*50, "\n")
    print("This program converts an integer to a Roman Numeral")
    print("-"*50)
    while True:
        user_input = input("Please enter a number between 1 and 3999 (or type 'exit'): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if not user_input.isdigit():
            print("Error: Please enter a valid number between 1 and 3999 - no letter characters allowed.")
            continue
        number  = int(user_input.strip()) # Convert to integer after stripping whitespace because input functuon made input string.
        if number < 1  or number > 3999:
            print("Error: Please enter a valid number between 1 and 3999.")
            continue
        number  = int(user_input.strip())
        convered_roman_number = convert_to_roman(number)
        print(f"The Roman Numeral is: {convered_roman_number}")



if __name__ == "__main__":
    main()

