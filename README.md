# python-text-file-analyzer
The File Analyzer CLI Tool is a Python-based command-line utility that analyzes .txt files. It provides a report with total word count, top 5 frequent words (excluding stopwords), average word length, and sentence count. Perfect for quick text analysis and insights.

# python-text-file-analyzer

## Overview
The **python-text-file-analyzer** is a Python-based command-line tool that analyzes a `.txt` file and provides valuable text insights such as:

- Total number of words
- Top 5 most frequent words (excluding common stopwords like "the", "is", and "and")
- Average word length
- Number of sentences

The tool uses **NLTK** (Natural Language Toolkit) for tokenizing the text and processing it.

## Features
- **Command-line interface** for easy file input.
- **NLTK**-based analysis (tokenization, stopword removal).
- Outputs the text analysis in a clean and readable format.


  

## NLTK Resources:
The script requires NLTK's punkt and stopwords resources. You can download them by running the following Python code:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```
# Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/rushikeshya/python-text-file-analyzer.git
   cd python-text-file-analyzer
   ```
2. Install the required dependencies:
   ```bash
   pip install nltk
   ```
# Usage
1. Open Command Prompt (Windows) or Terminal (Mac/Linux).
2. Navigate to the directory where the script is located:
   ```bash
   cd path/to/python-text-file-analyzer
   ```
3. Run the Python script with the path to the .txt file you want to analyze:
   ```bash
      python file_analyzer.py sample_text.txt
   ```
Replace sample_text.txt with the path to your text file.











   
