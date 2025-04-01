import argparse
import re
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')


# Function to analyze the text file
def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize words and sentences
    words = word_tokenize(text.lower())
    sentences = sent_tokenize(text)

    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]


    # Calculating required metrices
    total_words = len(words)
    most_common_words = Counter(words).most_common(5)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words else 0
    num_sentences = len(sentences)

    # Print Results
    print("Text File Analysis Report")
    print("------------------------------")
    print(f"Total Number of words: {total_words}")
    print("Top 5 most Frequent Words: ")
    for word, count in most_common_words:
        print(f" {word}: {count}")
    print(f"Average Word Length: {avg_word_length:.2f}")
    print(f"Number of Sentences: {num_sentences}")


# CLI Argument Parser
def main():
    parser = argparse.ArgumentParser(description='File Analyzer CLI Tool')
    parser.add_argument("file",type=str, help="Path to the text file : sample_text.txt")
    args = parser.parse_args()

    analyze_text(args.file)

if __name__ == "__main__":
    main()

