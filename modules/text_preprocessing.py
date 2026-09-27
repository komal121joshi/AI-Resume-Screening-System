# text_preprocessing.py
# This file cleans the extracted resume text.


import re


def clean_text(text):
    """
    Clean resume or job description text.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove spaces from beginning and end
    text = text.strip()

    return text