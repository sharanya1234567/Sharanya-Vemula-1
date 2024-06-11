#10.5. Text Analyzer (Bonus Challenge):
#Create a function analyze_text(text) that takes a block of text as input.
#The function should:
#Count the number of words in the text (split by whitespace).
#Count the number of characters (excluding whitespaces).
#Find the most frequent word (you can assume case-insensitive matching for simplicity).
#Return a dictionary containing these counts and the most frequent word.


def analyze_text(text):

    words = text.split()
    num_words = len(words)
    num_chars = len(''.join(words))
    words_lower = [word.lower() for word in words]
    
    word_frequency = {}
    for word in words_lower:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    most_frequent_word = max(word_frequency, key=word_frequency.get)
    
    analysis = {
        'word_count': num_words,
        'char_count': num_chars,
        'most_frequent_word': most_frequent_word
    }

    return analysis

 
input_text = "This is a Practice problem. This test is only a test."
results = analyze_text(input_text)
print(results)
