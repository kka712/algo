#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
#int solution(const char* my_string) {
#    int answer = 0; 
#    return answer;
#}

result = 0
int solution(my_string):
    

print(solution("aAb1B2cC34oOp")) # => 10
print(solution("1a2b3c4d123")) # => 16

# 문자를 제거한후 숫자만남김 -> 남은숫자를 다 더함 replace(char, '') -> 숫자만 남음? -> 
# words = words.replace(char, '') result = 0 result = result + number