def fibonacci(n):
    num = 0
    num1= 1
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1, 1):
            c = a
            a = b
            b = c + b
        return b

        #write your code here


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')