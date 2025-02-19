def solution(s1, s2):
    answer = 0
    result = 0
    for char in s1 and s2:
        result = result + 1
        if s1 == s2:
            return result


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"])) # => 2
print(solution(["n", "omg"], ["m", "dot"])) # => 0