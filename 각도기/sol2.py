def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

print(solution(70)) # => 1
print(solution(91)) # => 3
print(solution(180)) # => 4

# 왜 이렇게 나왔는지 이해가 잘안됨