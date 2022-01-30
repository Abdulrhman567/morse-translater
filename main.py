from codes import morse_codes

translator_on = True

while translator_on:
    text = input("Enter text: ").lower()
    try:
        morse_code_list = [morse_codes[letter] for letter in text]
        full_morse_text = ' '.join(morse_code_list)
        print(full_morse_text)
    except KeyError:
        print("Error in input, Can't translate these characters")
    if input("Do you want to enter another text?y/n ").lower() == "n":
        translator_on = False
