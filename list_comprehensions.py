def process_numbers(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    negatives = [num for num in numbers if num < 0]

    return evens, odds, negatives


def process_numbers_with_filter(numbers):
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 != 0, numbers))
    negatives = list(filter(lambda x: x < 0, numbers))

    return evens, odds, negatives


def work(fun):
    input_str = input("Введите числа, разделенные пробелами: ")
    numbers = list(map(int, input_str.split()))
    evens, odds, negatives = fun(numbers)
    print("Четные числа:", evens)
    print("Нечетные числа:", odds)
    print("Числа меньше 0:", negatives)


print("С помощью list comprehensions:")
work(process_numbers)
print("С помощью filter:")
work(process_numbers_with_filter)
