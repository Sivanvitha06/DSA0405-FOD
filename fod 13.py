from collections import Counter
import re

# Sample customer reviews dataset
reviews = [
    "The product is amazing. I love it!",
    "Not satisfied with the quality. Disappointing.",
    "Great value for the price. Highly recommended.",
    "Terrible experience. Would not buy again."
]

# Combine all reviews into a single string
all_reviews = ' '.join(reviews)

# Remove non-alphanumeric characters and convert to lowercase
cleaned_reviews = re.sub(r'[^a-zA-Z\s]', '', all_reviews).lower()

# Tokenize the text into words
words = cleaned_reviews.split()

# Calculate the frequency distribution of words
word_freq = Counter(words)

# Print the word frequency distribution
print("Word Frequency Distribution:")
for word, count in word_freq.items():
    print(f"{word}: {count}")
