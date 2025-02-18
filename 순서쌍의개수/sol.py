def solution(n):
    answer = 0

    for num in range(1, n+1):
        if n % num == 0:
            answer += 1

    return answer


print(solution(20)) # => 6
print(solution(100)) # => 9


# a * b == n