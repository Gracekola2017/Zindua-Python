# while True:
#     print("Hello world!")
#     break

# # for loop
# for i in range(2,50):
#     print(i)

# write a for loop that prints numbers between 0 and 100

for x in range(0,100):
    if (x % 2 == 0):
        print(x, 'is even!')


for num in range(0,28):
    if (num % 2 == 1):
        print(num, 'is odd!')

# write a python programs that prints all the multiples of 7 between 0 and 1000

for num in range(0,1000,7):
    print(num, 'is a multiple of 7')

    def evenNumbers(n):
        for i in range(n):
            if (1 % 2 == 0):
                print(1, 'is even!')
                evenNumbers(290)
                

