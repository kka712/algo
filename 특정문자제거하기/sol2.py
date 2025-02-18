def solution(my_string, letter):
    answer = ''

    for char in my_string:
        if char != letter:
            answer = answer + char # 문자열은 concatenation

    return answer

print(solution("abcdef", "f")) # => "abcde"
print(solution("BCBdbe", "B")) # => "Cdbe"
