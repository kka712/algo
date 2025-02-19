def solution(n):
    answer = 0
    i = 1
    for i in range(n):
        if n == i ** 2:
            return 1
        else:
            return 2

    


print(solution(144)) # => 1
print(solution(976)) # => 2