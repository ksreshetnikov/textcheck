import re
from spellchecker import SpellChecker
#https://github.com/ksreshetnikov/textcheck

def load_text_file(file_path: str) -> str:
    """Load text data from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        exit(1)

def check_spelling(text: str) -> dict:
    """Check spelling in the provided text"""
    spell = SpellChecker()
    
    # Clean and tokenize text
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Find misspelled words and suggestions
    misspelled = spell.unknown(words)
    results = {}
    
    for word in misspelled:
        suggestions = list(spell.candidates(word))[:3]  # Top 3 suggestions
        results[word] = {
            'count': words.count(word),
            'suggestions': suggestions
        }
    
    return results

def display_results(spelling_errors: dict):
    """Display spelling check results"""
    if not spelling_errors:
        print("No spelling errors found!")
        return
    
    print("Spelling Errors Found. Possible scam text")
    for word, details in spelling_errors.items():
        print(f"\nWord: {word}")
        print(f"Occurrences: {details['count']}")
        print(f"Suggestions: {', '.join(details['suggestions'])}")

def main():
    # File path to check (change this to your file path)
    input_file = ".txt"
    
    #check the text for spelling errors
    print(f"Checking spelling in file: {input_file}")
    text_data = load_text_file(input_file)
    spelling_errors = check_spelling(text_data)
    display_results(spelling_errors)

    #check the file for the link and if it is https



if __name__ == "__main__":
    main()
