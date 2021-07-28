from typing import List


def is_palindrime(string: str) -> bool:
    string = string.replace(" ", "").lower()

    return string == string[::-1]

def run():
    print(is_palindrime('Ana lava la tina'))

def its_prime(number: int) -> bool:
    count: List[int] = [n for n in range(1, number+1) if number % n == 0]
# Este es un condicional ternario, el else es obligatorio
    value : bool = False if len(count) > 2 else True
    return value


if __name__ == '__main__':
    run()
    n: int = int(input('Enter a number: '))
    print(its_prime(n))

