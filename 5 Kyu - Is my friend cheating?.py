''' A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?'''

def remov_nb(n):
    lst = []  # final list
    num_list = [x for x in range(1, n + 1)]  # list with all numbers
    f_lst = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a * b == sum(num_list) - a - b:
                lst.append(a)
                lst.append(b)             
    try:
        f_lst = [(lst[0], lst[1]), (lst[2], lst[3])]
    except:
        pass
    return f_lst
