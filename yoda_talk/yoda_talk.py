import random
import string

def yoda_talk(sentence):
    """
    Translate the input sentence into Yoda-speak.
    
    :param sentence: input string
    :return: translation to Yoda-speak
    """
    sentence = sentence.lower()
    for p in string.punctuation.replace("'", ''):
        sentence = sentence.replace(p, '')
    words = sentence.split()
    random.shuffle(words) 
    new_sent = ' '.join(words)
    print()
    print('Your Yodenglish sentence:')
    print(new_sent.capitalize())
    
if __name__ == '__main__':
    print('Your English sentence:')
    sentence = str(input())
    yoda_talk(sentence)
