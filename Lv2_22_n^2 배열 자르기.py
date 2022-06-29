# n^2 배열 자르기

def solution(n, left, right):
    r_list = []
    for i in range(left, right + 1):      
        y = i // n
        x = i % n
        r_list += [max(y, x)+1]
    return r_list

n = 3
left = 2
right = 5
solution(n, left, right)
