def solution(n, t):
    return n * (2**t)

print(solution(2, 10)) # => 2048
print(solution(7, 15)) # => 229376

# (n ** t) * 2 로 생각을 했었음