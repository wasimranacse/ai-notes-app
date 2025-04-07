from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """Analyzes sentiment and returns 'positive', 'neutral', or 'negative'."""
    sentiment_score = TextBlob(text).sentiment.polarity  # Get polarity (-1 to 1)

    if sentiment_score > 0:
        return "positive"
    elif sentiment_score < 0:
        return "negative"
    else:
        return "neutral"
