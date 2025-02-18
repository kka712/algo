def solution(num_list):
    answer = []
    answer = num_list.reverse()
    return num_list


print(solution([1, 2, 3, 4, 5])) # => [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # => [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # => [5, 3, 1, 1, 1, 0, 1]

# 반복문(for문)을 사용한 경우 우연의 일치로 홀수만 정답이 나왔으므로 for문을 제외한 답을 작성