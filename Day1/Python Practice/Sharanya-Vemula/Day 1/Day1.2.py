#10.3. List Statistics:
#Create a function analyze_list(numbers) that takes a list of numbers as input.
#The function should calculate and return the following in a dictionary:
#Minimum value in the list
#Maximum value in the list
#Average value in the list (use sum and division)
#Use a dictionary to store and return the calculated statistics.



def analyze_list(numbers):
    if not numbers: 
        return None

    
    min_value = min(numbers)
    max_value = max(numbers)
    avg_value = sum(numbers) / len(numbers)

    
    statistics = {
        'min': min_value,
        'max': max_value,
        'average': avg_value
    }

    return statistics


numbers = [10, 20, 30, 40, 50]
stats = analyze_list(numbers)
print(stats) 
