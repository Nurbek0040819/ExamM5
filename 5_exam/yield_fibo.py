def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input("Iltimos, Fibonachchi sonlarni nechta chiqarishni kiriting: "))
for fib_num in fib_generator(n):
    print(fib_num)
