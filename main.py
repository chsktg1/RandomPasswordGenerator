import random
def generate_random_length(start,end):
    return random.randint(start,end)
length=generate_random_length(7,12)
number_of_alpha=generate_random_length(1,length)
alphabets=[random.choice("qwertyuioplkjhgfdsazxcvbnm") for i in range(number_of_alpha)]
number_of_numbers=length-number_of_alpha
numbers=[generate_random_length(0,9) for i in range(number_of_numbers+1)]
number_of_special_cha=generate_random_length(3,5)
special_chars=[random.choice("!@#$%^&*()") for i in range(number_of_special_cha)]
alphabets.extend(numbers)
alphabets.extend(special_chars)
random.shuffle(alphabets)
alphabets=list(map(lambda a:str(a),alphabets))
print(alphabets)
print(len(alphabets))
print("".join(alphabets))


