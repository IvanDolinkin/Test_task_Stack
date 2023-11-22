# есть последовательность с заранее неизвестным количеством произвольных букв
# необходимо написать функцию, группирующую части последовательности по типу символа:
# Пример:
# имеется строка aaabbbbccddaaabb
# Результат работы:
# aaaaaa
# bbbbbb

some_str = 'aaabbbbccddaaabb'


def print_sorted_chars_v1(some_string):
    some_list = sorted(list(some_string))
    one_ch_string = some_list[0]
    counter = 0
    for i in some_list:
        counter += 1
        if i in one_ch_string:
            one_ch_string += i
        else:
            print(one_ch_string)
            one_ch_string = i
        if counter == len(some_list):
            print(one_ch_string)


print_sorted_chars_v1(some_str)     # неверное решение, печатает 1 лишний первый символ, который появляется в строке 14


def print_sorted_chars_v1(some_string):
    some_list = sorted(list(some_string))
    one_ch_string = some_list[0]
    counter = 1                             # меняем начало отсчета
    for i in some_list[1:]:                 # меняем начало цикла
        counter += 1
        if i in one_ch_string:
            one_ch_string += i
        else:
            print(one_ch_string)
            one_ch_string = i
        if counter == len(some_list):
            print(one_ch_string)


print_sorted_chars_v1(some_str)


def print_sorted_chars_v2(some_string):
    unique_chars = set(some_string)
    count_chars = {}
    for ch in unique_chars:
        count_chars[ch] = some_string.count(ch)
    result = '\n'.join(sorted(key*val for key, val in count_chars.items()))
    print(result)


print_sorted_chars_v2(some_str)
