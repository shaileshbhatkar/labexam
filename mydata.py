def simple_interest(p,t,r):
    #print('The principal is', p)
    #print('The time period is', t)
    #print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
print(" ")
simple_interest(8, 6, 8)
print(" ")

def compound_interest(principal, rate, time):

 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
compound_interest(10000, 10.25, 5)
print(" ")