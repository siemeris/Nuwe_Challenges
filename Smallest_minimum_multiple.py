# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest(min,max):
    numero=1
    while numero:
        for div in range(min,max+1):
            if numero%div==0 and div==max:
                return numero
            elif numero%div==0:
                continue
            else:
                numero+=1
                break
                
print(smallest(1,20))

