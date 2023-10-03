def log_input_output(func):
    def wrapper(*args, **kwargs):
        print(f"Входные параметры: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper


@log_input_output
def multiply(a, b):
    return a * b


multiply(2, 3)
