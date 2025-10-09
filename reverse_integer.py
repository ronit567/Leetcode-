def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    sign = -1 if x < 0 else 1
    x *= sign  # make x positive for reversal

    reversed_num = 0
    while x != 0:
        digit = x % 10
        x //= 10

        # Check for overflow before multiplying by 10
        if reversed_num > (INT_MAX - digit) // 10:
            return 0  # would overflow 32-bit range

        reversed_num = reversed_num * 10 + digit

    return sign * reversed_num
