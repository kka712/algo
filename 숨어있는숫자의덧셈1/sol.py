def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))

    return sum(numbers)

print(solution("aAb1B2cC34oOp")) # => 10
print(solution("1a2b3c4d123")) # => 16

# 문자를 제거한후 숫자만남김 -> 남은숫자를 다 더함 replace(char, '') -> 숫자만 남음? -> 
# words = words.replace(char, '') result = 0 result = result + number