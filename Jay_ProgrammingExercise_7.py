import re

"""
Name: Jay Genao
Date: March 16, 2026
Program Description:
This program asks the user to enter a paragraph and then uses a regular expression
with a look-ahead feature to find each sentence. It prints each sentence on its own
line and displays the total number of sentences found. It supports sentences that
begin with numbers and avoids breaking on common cases like abbreviations and
decimal numbers by only ending a sentence when punctuation is followed by a space
and the start of a new sentence (capital letter or number) or the end of the text.
"""


def extract_sentences(paragraph):
    """
    Brief Description:
        Uses a regular expression (with look-ahead) to extract sentences from a paragraph.

    Parameters:
        paragraph (str): The paragraph entered by the user.

    Variables:
        pattern (str): Regex pattern used to find sentences.
        matches (list[str]): A list of sentences found by the regex.

    Logical Steps:
        1. Define a regex pattern that starts a sentence with a capital letter OR a digit.
        2. Match up to the next sentence-ending punctuation (. ! ?).
        3. Use look-ahead to ensure the punctuation is followed by:
           - whitespace + (capital letter OR digit), OR
           - end of the string.
        4. Return the list of matched sentences (trimmed).

    Return:
        list[str]: List of extracted sentences.
    """
    # Sentence starts with a capital letter OR a digit (to allow numbered sentences)
    # Ends at . ! ? only when a new sentence likely begins (look-ahead) or end of text
    pattern = r"(?:[A-Z0-9]).*?[.!?](?=\s+(?:[A-Z0-9])|\s*$)"

    matches = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    # Clean up whitespace on each sentence
    return [s.strip() for s in matches]


def display_sentences(sentences):
    """
    Brief Description:
        Prints each sentence on its own line and prints the total count.

    Parameters:
        sentences (list[str]): The list of extracted sentences.

    Variables:
        count (int): The number of sentences.

    Logical Steps:
        1. Print each sentence on a new line.
        2. Count how many sentences are in the list.
        3. Print the total sentence count.

    Return:
        None
    """
    # Print each sentence found
    for sentence in sentences:
        print(sentence)

    # Print the total count
    count = len(sentences)
    print(f"\nTotal sentences: {count}")


def main():
    """
    Brief Description:
        Gets a paragraph from the user, extracts sentences, and displays results.

    Parameters:
        None

    Variables:
        paragraph (str): The paragraph entered by the user.
        sentences (list[str]): Extracted sentences.

    Logical Steps:
        1. Prompt the user to enter a paragraph.
        2. Extract sentences using extract_sentences().
        3. Display sentences and the count using display_sentences().

    Return:
        None
    """
    paragraph = input("Enter a paragraph:\n")
    print("\n--- Sentences Found ---")
    sentences = extract_sentences(paragraph)
    display_sentences(sentences)


if __name__ == "__main__":
    main()