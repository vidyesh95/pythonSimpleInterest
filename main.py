# Python program to find simple interest

def simple_interest(p, r, t):
    print("The initial principal balance : ", p)
    print("The annual interest rate : ", r)
    print("The time(in years) : ", t)

    si = (p * t * r) / 100
    print("The simple interest : ", si)
    return si


principal = input("Initial principal balance : ")
rate = input("Annual interest rate : ")
time = input("Time in years : ")

simple_interest(int(principal), int(rate), int(time))
