def division(number):
    three_num = []
    for num in range(1,number):
        if num%3 == 0:
            three_num.append(num)
    return three_num

print(division(100))

def select(word):
    vowels = 'a','e','i','o','u'
    vowel_output = []
    for alphabet in word.lower():
        if alphabet in vowels:
            vowel_output.append(alphabet)
    return "".join(vowel_output)
