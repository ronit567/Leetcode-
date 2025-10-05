def generate_parenthesis(n):
    res = []

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:  # can add '('
            backtrack(s + "(", left + 1, right)
        if right < left:  # can add ')'
            backtrack(s + ")", left, right + 1)

    backtrack("", 0, 0)
    return res
