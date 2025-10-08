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
    if i == n:
        return 0

    # 2) signedness
    sign = 1
    if s[i] in ('+', '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # 3) read digits (ignore leading zeros explicitly)
    #    stop at first non-digit
    num_started = False
    value = 0

    # skip leading zeros in the numeric portion
    while i < n and s[i] == '0':
        num_started = True
        i += 1

    # read remaining digits
    while i < n and s[i].isdigit():
        num_started = True
        digit = ord(s[i]) - ord('0')
        value = value * 10 + digit
        i += 1

    if not num_started:
        return 0

    return sign * value
