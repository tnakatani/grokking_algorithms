"""Ch.3 Recursion"""


def factorial(n: int) -> int:
    """Calculates factorial from given number."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
