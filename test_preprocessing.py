from modules.text_preprocessing import clean_text


text = "Python Developer | 2 Years Experience! Skills: Python, SQL, Pandas."

cleaned_text = clean_text(text)

print("Original Text:")
print(text)

print("\nCleaned Text:")
print(cleaned_text)