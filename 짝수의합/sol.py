def solution(n):
    result = 0
    if n % 2 == 0:
        result = result + n
    return result

print(solution(10)) # => 30
print(solution(4)) # => 6