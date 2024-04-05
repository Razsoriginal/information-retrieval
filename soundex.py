def soundex(word):
    word = word.upper()

    soundex_code = word[0]

    dictionary = {
        'VPFB': '1',
        'CGSKJXZ': '2',
        'DT': '3',
        'L': '4',
        'MN': '5',
        'R': '6'
    }

    for char in word[1:]:
        for key, value in dictionary.items():
            if char in key and value != soundex_code[-1]:
                soundex_code += value

    for char in 'AEIOUWHY':
        soundex_code = soundex_code.replace(char, '')

    soundex_code = soundex_code.ljust(4, '0')
    soundex_code = soundex_code[:4]
    return soundex_code

word = input("Enter a word: ")
print("Soundex code:", soundex(word))