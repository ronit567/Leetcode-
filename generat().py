def generate_parenthesis(n):
    res = []

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)

    backtrack("", 0, 0)
    return res


# Example test cases
print(generate_parenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(generate_parenthesis(1))  # ["()"]
