# Comment
## print("hello world"[::-1])

# my_list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# list_sum = 0
# for item in my_list:
#     if item % 2 == 0:
#         print(f'{item} is even')
#         list_sum += item
#     else:
#         print(f'{item} is odd')

# print(list_sum)

# my_string = "hello world"

# for string in my_string:
#     print(string)
#     pass

# my_tuple_lust = [(1, 2), (3, 4), (5, 6)]

# for a, b in my_tuple_lust:
#     print(f'{a} | {b}')
#     pass

# my_dict = { 'name': 'Joshua', 'surname':'Britz', 'age':20 }

# for (key, value) in my_dict.items():
#     print(f'{key} is equal to {value}')
#     pass

# is_hungry = True

# while is_hungry:
#     print('Feeding')
#     is_hungry = False
#     pass
# else:
#     print('You are no longer hungry')
#     pass

# list_of_lists = [[1, 2], [3, 4], [5, 6], [7, 8]]

# for _list in list_of_lists:
#     for _list_item in _list:
#         print(_list_item)

# for num in range(1, 11, 2):
#     print(num ** num)

# gen = list(range(1, 11, 2))
# print(gen)

## ENUMERATOIN

# word = 'serendipity'
# for index, letter in enumerate(word):
#     print(word[index])

## ZIPPING

# list_1 = [1, 2, 3, 4, 5]
# list_2 = ['a', 'b', 'c', 'd', 'e']

# for item in zip(list_1, list_2):
#     print(item)

## USING IN KEYWORD

# print(1 in [1, 2, 3])
# print('a' in 'apple')

## LIST MIN AND MAX VALUES

# a_list = [100, 200, 300, 400, 500]
# print(min(a_list))
# print(max(a_list))

## LIST SHUFFLING

# from random import shuffle

# list_to_shuffle = [100, 200, 300, 400, 500, 600, 700]

# shuffle(list_to_shuffle)

# print(list_to_shuffle)

## RANDOM INTEGER

# from random import randint

# random_num = randint(0, 100)

# print(random_num)

## INPUT

# name = input('What is your name?: ')
# print(f'Hello {name}')

# age = input('What is your age?: ')
# print(int(age))

## LIST COMPREHEMSION

# comp = [letter for letter in 'hello']
# print(comp)

## LIST COMPREHEMSION WITH IF STATEMENT

# comp = [x for x in range(1,11) if x % 2 == 0]
# print(comp)

## LIST INSERT

# my_list = [1, 2, 3, 4, 5]

# print(my_list)

# my_list.insert(1, 'hello')

# print(my_list)

# def name_function(name: str = None):
#     if name != None:
#         return f'Hello {name}'
#     else:
#         return 'Hello'

# result = name_function()

# print(result)

# def contains_dog(string):
#     return 'dog' in str(string).lower()

# print(contains_dog('My dog ran away'))


def pig_latin(string: str):
    string = string.lower()
    pig_latin_string = []

    for word in string.split():
        is_vowel = not word[0] in ['a', 'e', 'i', 'o', 'u']

        if is_vowel:
            pig_latin_string.append(f'{word[1:]}{word[0]}ay')
        else:
            pig_latin_string.append(f'{word}ay')
            
    return ' '.join(pig_latin_string)


print(pig_latin(input('Give me a sentence: ')))
