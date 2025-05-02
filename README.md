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
Replace **sample_text.txt** with the path to your text file.




# Example Command:
```bash
python file_analyzer.py sample_text.txt
```
# Output
After running the script, you will see a report with the following details:

```yaml
Text File Analysis Report
----------------------------
Total Number of Words: 201
Top 5 Most Frequent Words:
  news: 11
  story: 10
  fake: 9
  stories: 6
  look: 6
Average Word Length: 5.67
Number of Sentences: 30
```
![image](https://github.com/user-attachments/assets/3b3c04b7-64d8-45fa-a414-87817c65549d)

# License
This project is open-source and free to use.

# Author
Developed by **Rushikesh** 🚀






   
