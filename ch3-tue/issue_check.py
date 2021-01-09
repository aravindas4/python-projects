def check_es(word):
    if 'es' in word:
        return True
    else:
        return False

def check_ing(word):
    if 'ing' == word[-3:]:
        return True
    else:
        return False

def equality(word1,word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if word1 == word2:
        return 'Both words are same'


def exponent(num):
    if num < 10:
        return num**2
    else:
        return num
