def countAndSay(n):
    if n < 1 or n > 30:
        raise ValueError("n must be between 1 and 30 inclusive.")
    if n == 1:
        return "1"
    
    prev = countAndSay(n - 1)
    result = ""
    count = 1
    
    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            count += 1
        else:
            result += str(count) + prev[i - 1]
            count = 1
    result += str(count) + prev[-1]
    
    return result

