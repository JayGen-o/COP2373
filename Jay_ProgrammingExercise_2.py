"""
Name: Jay Genao
Date: February 9, 2026

Program Description:
This program analyzes a user-entered email message to estimate how likely it is to be spam.
It checks the message for 30 common spam words/phrases. Each occurrence adds 1 point
to the spam score. The program displays the spam score, the likelihood rating, and
the specific words/phrases that caused the message to be flagged.
"""

import re


def get_spam_phrases():
    """
    Returns the list of 30 spam words/phrases used to score a message.

    Parameters:
        None

    Variables:
        spam_phrases (list[str]): The list of spam words/phrases.

    Logic:
        1. Create a list containing 30 common spam words/phrases.
        2. Return the list.

    Return:
        list[str]: The list of spam words/phrases.
    """
    spam_phrases = [
        "free", "winner", "win", "cash", "prize", "limited time", "act now", "urgent",
        "click here", "buy now", "order now", "special offer", "guaranteed", "risk free",
        "no cost", "no obligation", "congratulations", "claim", "credit", "loan",
        "pre-approved", "investment", "bitcoin", "crypto", "deal", "discount",
        "100% free", "get rich", "make money", "gift card", "exclusive"
    ]
    return spam_phrases


def analyze_message(message, spam_phrases):
    """
    Analyzes a message and counts spam phrase occurrences (case-insensitive).

    Parameters:
        message (str): The email message entered by the user.
        spam_phrases (list[str]): The list of spam words/phrases to search for.

    Variables:
        phrase_counts (dict[str, int]): Tracks how many times each phrase appears.
        total_score (int): The spam score (1 point per occurrence).
        phrase (str): The current spam word/phrase being checked.
        matches (list[str]): All matches found for a phrase.

    Logic:
        1. Create a dictionary to store counts for each spam phrase.
        2. For each phrase, find all case-insensitive occurrences in the message.
        3. Add the count of matches to the total spam score.
        4. Return the total score and the dictionary of phrase counts.

    Return:
        tuple[int, dict[str, int]]: (total spam score, phrase counts dictionary)
    """
    phrase_counts = {}
    total_score = 0

    for phrase in spam_phrases:
        # Escape special regex chars and search case-insensitively
        pattern = re.escape(phrase)

        # For single words, use word boundaries so "win" doesn't match "window"
        if " " not in phrase:
            pattern = r"\b" + pattern + r"\b"

        matches = re.findall(pattern, message, flags=re.IGNORECASE)
        count = len(matches)

        if count > 0:
            phrase_counts[phrase] = count
            total_score += count

    return total_score, phrase_counts


def rate_spam_likelihood(score):
    """
    Converts a spam score into a human-readable likelihood rating.

    Parameters:
        score (int): The spam score.

    Variables:
        None

    Logic:
        1. Use ranges of scores to assign a likelihood label.

    Return:
        str: The likelihood rating ("Low", "Medium", "High", "Very High").
    """
    if score <= 3:
        return "Low"
    if score <= 7:
        return "Medium"
    if score <= 12:
        return "High"
    return "Very High"


def display_results(score, likelihood, phrase_counts):
    """
    Displays the spam analysis results, including which phrases were found.

    Parameters:
        score (int): The total spam score.
        likelihood (str): The likelihood rating.
        phrase_counts (dict[str, int]): Found spam phrases and their counts.

    Variables:
        phrase (str): A spam phrase found in the message.
        count (int): The number of times the phrase occurred.

    Logic:
        1. Print the spam score and likelihood rating.
        2. If phrases were found, print each phrase and its count.
        3. If none were found, print a message saying so.

    Return:
        None
    """
    print("\n--- Spam Analysis Results ---")
    print(f"Spam Score: {score}")
    print(f"Likelihood of Spam: {likelihood}")

    if phrase_counts:
        print("\nWords/Phrases that caused it to be spam:")
        for phrase, count in sorted(phrase_counts.items(), key=lambda item: item[0]):
            print(f"- {phrase} (count: {count})")
    else:
        print("\nNo spam words/phrases were found in the message.")


def main():
    """
    Program entry point. Prompts for an email message and runs the spam analysis.

    Parameters:
        None

    Variables:
        message (str): The email message entered by the user.
        spam_phrases (list[str]): The 30 spam words/phrases.
        score (int): The spam score for the message.
        phrase_counts (dict[str, int]): Which phrases were found and how often.
        likelihood (str): The spam likelihood rating.

    Logic:
        1. Prompt the user to enter an email message.
        2. Load the spam phrase list.
        3. Analyze the message to compute score and found phrases.
        4. Convert score into a likelihood rating.
        5. Display the results.

    Return:
        None
    """
    message = input("Enter the email message to analyze:\n")

    spam_phrases = get_spam_phrases()
    score, phrase_counts = analyze_message(message, spam_phrases)
    likelihood = rate_spam_likelihood(score)

    display_results(score, likelihood, phrase_counts)


if __name__ == "__main__":
    main()
