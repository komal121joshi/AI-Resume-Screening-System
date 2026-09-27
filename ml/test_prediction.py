import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


data = pd.read_csv(
    "ml/training_data.csv",
    encoding="utf-8-sig"
)

data.columns = data.columns.str.strip()


data["text"] = (
    data["resume_text"].astype(str)
    + " "
    + data["job_description"].astype(str)
)

X_text = data["text"]
y = data["label"]


vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X = vectorizer.fit_transform(X_text)


model = LogisticRegression(
    max_iter=1000
)

model.fit(X, y)


resume = """
Frontend Developer with experience in HTML, CSS,
JavaScript, React and Git.
"""


job_description = """
We are looking for a Frontend Developer with experience
in HTML, CSS, JavaScript, React and Git.
"""


test_text = resume + " " + job_description

test_vector = vectorizer.transform([test_text])


prediction = model.predict(test_vector)[0]

probabilities = model.predict_proba(test_vector)[0]

confidence = max(probabilities) * 100


print("========== ML PREDICTION ==========")

print("Prediction:", prediction)

print(
    "Confidence:",
    round(confidence, 2),
    "%"
)