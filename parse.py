#The following code tokenizes a given paragraph, performs parts of speech tagging, defines a grammar for noun phrases, parses the tagged tokens and visualizes the parsed tree structure.


# Importing the libraries
import nltk
from nltk.tokenize import word_tokenize 

# Download necessary resources
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Input paragraph
para = "Java is the name of a programming language created by Sun Microsystems."

# Tokenizing the words
tokenized_text = nltk.word_tokenize(para)

# Parts of speech tagging
tagged_token = nltk.pos_tag(tokenized_text)

# Print tokenized words and their POS tags
print("Tokenized Text:")
print(tokenized_text)
print("\nParts of Speech Tags:")
print(tagged_token)

# Defining grammar for the chunks
grammar = "NP: {<DT>?<JJ>*<NN>}"
phrases = nltk.RegexpParser(grammar)

# Parsing the tagged tokens
result = phrases.parse(tagged_token)

# Visualize the parsed tree structure
result.draw()
