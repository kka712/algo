def solution(n):
    answer = 0

    for i in range(n+1):
        if i % 2 == 0:
            answer = answer + i
            # answer += i


    return answer

print(solution(10)) # => 30
print(solution(4)) # => 6