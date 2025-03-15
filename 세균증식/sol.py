def solution(n, t):
    return n << t

print(solution(2, 10)) # => 2048
print(solution(7, 15)) # => 229376

# <<  =>  a << b (a의 비트를 b번 왼쪽으로 이동시킴)
# >>  =>  a >> b (a의 비트를 b번 오른쪽으로 이동시킴)
