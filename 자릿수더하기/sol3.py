def solution(n):
    answer = 0

    return sum(map(int, list(str(n))))

    return answer


print(solution(1234)) # => 10
print(solution(930211)) # => 16