from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kargs):
        inicial_time = datetime.now()
        func(*args, **kargs)
        final_time = datetime.now()

        time_elapse = final_time -  inicial_time
        print(f'Pasaron {time_elapse.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

random_func()
suma(5, 4)


