# Even or Odd 
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

# Conver number(integer) to a string
def number_to_string(num):
    return str(num)


# Vowel Count
def get_count(sentence):
    x = str(sentence)
    z = list(x)
    y = ["a", "e", "i", "o", "u"]
    count = 0
    for i in z:
        if i in y:
            count = count +1
        else:
            pass
    return count
