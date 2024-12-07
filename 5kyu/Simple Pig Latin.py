'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !'''

def pig_it(text):
    def process_word(word):
        if word.isalpha():
            return word[1:] + word[0] + "ay"
        else:
            return word
    words = text.split()
    processed_words = [process_word(word) for word in words]
    return " ".join(processed_words)

'''test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')'''