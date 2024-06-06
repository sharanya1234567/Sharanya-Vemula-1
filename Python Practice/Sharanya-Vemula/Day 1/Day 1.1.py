#10.2. String Manipulation:
#Create a function reverse_words(text) that takes a string as input.
#The function should reverse the order of words in the string while maintaining the order of characters within each word. -Return the modified string.

def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    reversed_text = ' '.join(reversed_words)
    return reversed_text


input_text = "Hello world"
output_text = reverse_words(input_text)
print(output_text)  