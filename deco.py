from functools import wraps
import time 

def to_luke(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Son, {original_val}'
    return wrapper

@to_luke
def luke_saying(txt):
    return txt

def to_vader(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Father, {original_val}'
    return wrapper

@to_vader
def vader_saying(txt):
    return txt 

def borat(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'{original_val} ... NOT!'
    return wrapper 

@borat
def borat_saying(txt):
    return txt 

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run = end - start
        print(f'Finished {func.__name__!r} in {run:.4f} secs')
        return value
    return wrapper 

def calculate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return original_val
    return wrapper

@timer
@calculate
def addition(x, y):
    return x + y

@timer
@calculate
def multiplication(x, y):
    return x * y

@timer
def waste_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

if __name__ == "__main__":
    print(luke_saying('you have to grow up someday'))
    print(vader_saying('but i dont wanna'))
    print(borat_saying('i like your shirt'))
    print(addition(3, 4))
    print(multiplication(3, 4))
    print(waste_time(100))