def solution(numbers):
    result = 0
    for number in numbers:
        result = (result + number) 
    return result


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # => 5.5
print(solution([89, 90, 91, 92, 92, 94, 95, 96, 97, 98, 99])) # => 94.0


# 1.numbers의 값을 모두 더한다
# 2.numbers의 수만큼 나눈다