# Grade analyzer
print("Enter Marks Obtained in 5 Subjects: ")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

tot = mark1+mark2+mark3+mark4+mark5
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A")
elif avg>=81 and avg<91:
    print("Your Grade is B")
elif avg>=71 and avg<81:
    print("Your Grade is C")
elif avg>=61 and avg<71:
    print("Your Grade is D")
elif avg>=51 and avg<61:
    print("Your Grade is FAIL")
else:
    print("Invalid Input!")
