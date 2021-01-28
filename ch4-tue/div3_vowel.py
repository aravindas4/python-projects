def division(number):
    three_num = [num for num in range(1,number) if num%3 == 0]
    return three_num

def select(word):
    vowels = 'a','e','i','o','u'
    vowel_output = [alphabet for alphabet in word.lower() if alphabet in vowels]
    return "".join(vowel_output)
