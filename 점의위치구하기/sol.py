def solution(dot):
    
    
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4



print(solution([2, 4])) # => 1
print(solution([-7, 9])) # => 2

# 이것보다 간단하게 풀이하는 방법을 다시 고민해보기