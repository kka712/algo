def solution(numbers):
    answer = 0
    for number in numbers:
        numbers.sort(reverse=True)
        return numbers[0] * numbers[1]



print(solution([1, 2, 3, 4, 5])) # => 20
print(solution([0, 31, 24, 10, 1, 9])) # => 744

# def solution(numbers:)
#        numbers.sort(reverse=True)
#        return numbers[0] * numbers[1]