def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer


print(solution((1, 2, 3, 4, 5), 1, 3))  # => [2, 3, 4]
print(solution((1, 3, 5), 1, 2))  # => [3, 5]

# 끝의 인덱스는 원래 값보다 1을 더 크게 설정