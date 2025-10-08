# my_atoi.py

INT_MIN = -2**31
INT_MAX = 2**31 - 1

def myAtoi(s: str) -> int:
    """
    Convert a string to a 32-bit signed integer following rules:
      1) Ignore leading whitespace
      2) Optional '+' or '-' sign
      3) Read consecutive digits (ignore leading zeros)
      4) Stop at first non-digit
      5) Clamp to [-2^31, 2^31-1]
    """
    i = 0
    n = len(s)

    # 1) skip leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # if only spaces
    if i == n:
        return 0

    # 2) signedness
    sign = 1
    if s[i] == '+' or s[i] == '-':
        if s[i] == '-':
            sign = -1
        i += 1

    # parsing to be added
    return 0
