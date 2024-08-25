# A bigram is a sequence of two adjacent elements from a string of tokens.
# These are typically letters, syllables, or words. 

def get_bigrams(string):
    # Remove spaces and convert to lowercase for consistency
    string = string.replace(" ", "").lower()
    
    # Generate bigrams
    bigrams = []
    for i in range(len(string) - 1):
        bigrams.append(string[i:i+2])
    
    return bigrams

# Testing the function
test_string = "Hello World"
result = get_bigrams(test_string)
print(result)