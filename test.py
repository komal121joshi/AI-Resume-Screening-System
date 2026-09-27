from modules.resume_parser import extract_resume_text

# Name of the resume PDF
file_path = "sample_resume.pdf"

# Extract text from the resume
text = extract_resume_text(file_path)

# Display the extracted text
print("----- EXTRACTED RESUME TEXT -----")
print(text)