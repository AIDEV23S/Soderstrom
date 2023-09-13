# Skapar en lista med numrerna 2 till 99
number_list = [*range(2,100)]

# Lista som håller primtalen
prime_list = []

# Ittererar igenom numrerna.
for number in number_list:
    
    # Delar numret med numrerna 2 till 99.
    for devider in range(2, number + 1):
        result = number / devider
        
        # Kollar om float värdet delas jämnt och om variablerna är densamma.
        if str(result).endswith("0"):
            if number != devider:
                break
            else:
                prime_list.append(number)
        
# Printar resultatet.
print(prime_list)
