#10.4. Filtering with Lambda:
#Create a list of product names (strings).
#Define a function filter_short_names(names, max_length) that takes the list of names and a maximum length as arguments.
#Use filter with a lambda function to return a new list containing only names shorter than the provided max_length.



def filter_short_names(names, max_length):
    
    short_names = list(filter(lambda name: len(name) < max_length, names))
    return short_names

 
product_names = ["Apple", "Banana", "Cherry", "Date", "Grape", "Mango", "Blue berry"]
max_length = 6
filtered_names = filter_short_names(product_names, max_length)
print(filtered_names)  
