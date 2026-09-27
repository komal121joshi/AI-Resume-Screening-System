import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


data = pd.read_csv(
    "ml/training_data.csv",
    encoding="utf-8-sig"
)

data.columns = data.columns.str.strip()

required_columns = {
    "resume_text",
    "job_description",
    "label"
}

missing_columns = required_columns - set(data.columns)

if missing_columns:
    raise ValueError(
        f"Missing columns: {missing_columns}\n"
        f"Found columns: {data.columns.tolist()}"
    )


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


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("========== ML MODEL RESULTS ==========")

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)