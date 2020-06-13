def main():
    """Executes the collatz function call"""
    try:
        number = int(input("Please enter a positive integer: "))
        while True:
            solution = collatz(number)
            if solution == 1:
                break
    except ValueError:
        print(f"Invalid input! {number}")


def collatz(number):
    """Returns a sequence of numbers that stops when the return value is 1"""
    if number % 2 == 0:
        solve = number // 2
        return solve
    elif number % 2 == 1:
        solve = 3 * number + 1
        return solve


if __name__ == '__main__':
    main()
