# Skapar en lista med numrerna 2 till 99
number_list = [*range(2,100)]

# Lista som håller primtalen
prime_list = []


for number in number_list:
    for devider in range(2, number + 1):
        result = number / devider
        if str(result).endswith("0"):
            if (number / (devider - 1)) > (number - 1 / (devider - 2 or 1  )):
                prime_list.append(number)
        
            
        
print(prime_list)
