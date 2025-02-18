def solution(n):
    answer = 0

    while n > 0:
         # a = divmod(n, 10)[0] # n // 10
        # b = divmod(n, 10)[1] # n % 10
        a, b = divmod(n, 10)


        answer = answer + b
        n = a
       
    return answer
# 수학적으로 계산


# 자릿수 더하기
# 일의 자리 + 십의 자리 + 백의 자리 + ... + 10**n 자리의 숫자를 더한다

print(solution(1234)) # => 10
print(solution(930211)) # => 16