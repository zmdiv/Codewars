''' A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?'''

# version 1. Correct version, calculations are OK, but the test is failed due to high execution time (O(n**2))

def remov_nb(n):
    lst = []   
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


# version 2. Efficient, test passed - O(n)

def remov_nb(n):
    result = []
    # Sn=n(a1 + a2)2  - Sum of the Terms of an Arithmetic Sequence (Arithmetic Series), where n is the number of terms, a1 is the first term and an is the last term.
    sum_nums = n * (n + 1) // 2
    for a in range(1, n+1):
        b = (sum_nums - a) // (a + 1) # taking into consideration that (sum_nums - a - b = a * b) that means -->> b = (sum_nums - a) / (a + 1)
        if b <= n and sum_nums - a - b == a * b:
            result.append((a, b))
    return result
