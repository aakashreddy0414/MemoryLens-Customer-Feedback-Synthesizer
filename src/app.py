import pandas as pd

df = pd.read_csv("data/feedback_march.csv")

def get_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

df["sentiment"] = df["rating"].apply(get_sentiment)

print(df[["review", "rating", "sentiment"]])

print("\nSentiment Summary:")
print(df["sentiment"].value_counts())


def get_topic(review):
    review = review.lower()

    if "battery" in review:
        return "Battery"
    elif "hot" in review or "charging" in review:
        return "Heating"
    elif "camera" in review:
        return "Camera"
    elif "performance" in review:
        return "Performance"
    elif "expensive" in review or "price" in review:
        return "Price"
    else:
        return "Other"

df["topic"] = df["review"].apply(get_topic)

print("\nTopic Summary:")
print(df["topic"].value_counts())
print("\nNegative Feedback by Topic:")

negative_feedback = df[df["sentiment"] == "Negative"]

print(negative_feedback["topic"].value_counts())
print("\n===== MEMORYLENS FEEDBACK SUMMARY =====")

total = len(df)
positive = len(df[df["sentiment"] == "Positive"])
negative = len(df[df["sentiment"] == "Negative"])

print("Total Feedback:", total)
print("Positive Feedback:", positive)
print("Negative Feedback:", negative)

print("\nTop Customer Topics:")
print(df["topic"].value_counts().head(5))

print("\nMain Negative Topics:")
print(
    df[df["sentiment"] == "Negative"]["topic"]
    .value_counts()
    .head(3)
)
top_topic = df["topic"].value_counts().idxmax()
negative_topic = (
    df[df["sentiment"] == "Negative"]["topic"]
    .value_counts()
    .idxmax()
)

print("\n===== AI-STYLE INSIGHT =====")
print(
    f"Customers discussed {top_topic} most frequently. "
    f"The topic with the most negative feedback is {negative_topic}."
)
print("\n===== JANUARY vs MARCH COMPARISON =====")

jan = pd.read_csv("data/feedback_january.csv")
mar = pd.read_csv("data/feedback_march.csv")

jan_positive = len(jan[jan["rating"] >= 4])
jan_negative = len(jan[jan["rating"] < 4])

mar_positive = len(mar[mar["rating"] >= 4])
mar_negative = len(mar[mar["rating"] < 4])

print("\nJanuary:")
print("Positive Feedback:", jan_positive)
print("Negative Feedback:", jan_negative)

print("\nMarch:")
print("Positive Feedback:", mar_positive)
print("Negative Feedback:", mar_negative)

print("\nChange:")
print("Positive feedback change:", mar_positive - jan_positive)
print("Negative feedback change:", mar_negative - jan_negative)