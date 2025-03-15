def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

print(solution([1, 2, 3, 4, 5])) # =>[2, 3]
print(solution([1, 3, 5, 7])) # =>[0, 4]

# num_list에 있는 원소들을 순서대로 2로 나눌때,나눈 나머지가 0 이면 answer[0] 에 1을 더하고, 1이면(홀수면) answer[1]에 1을 더하라


# def solution(num_list):
#     answer = [0, 0]
#     for num in num_list:
#         if num % 2 == 0:
#             pass
#         else:
#             pass

#     return answer