def int_to_roman(num: int) -> str:
    """Convert an integer to a Roman numeral."""
    roman_map = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

    result = ""
    for symbol, value in roman_map:
        while num >= value:
            result += symbol
            num -= value
    return result

if __name__ == "__main__":
    test_cases = [3, 4, 9, 58, 1994, 2025]
    for n in test_cases:
        print(f"{n} -> {int_to_roman(n)}")

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        print(f"Roman numeral: {int_to_roman(num)}")
    except ValueError:
        print("Please enter a valid integer.")
