import re
from textblob import TextBlob

def clean_text(text):
    """
    Cleans text by removing links, special characters, and excessive whitespace.
    
    Args:
        text (str): The raw text from a tweet or comment.
        
    Returns:
        str: A cleaned version of the text.
    """
    text = re.sub(r"http\S+", "", text)  # Remove links
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text)  # Remove extra whitespace
    return text.strip()

def analyze_sentiment(tweets):
    """
    Analyzes sentiment for a list of tweets.
    Calculates the average polarity score of the tweets, ranging from -1 (negative) to 1 (positive).
    
    Args:
        tweets (list): A list of tweet texts.
        
    Returns:
        float: The average sentiment polarity score.
    """
    sentiment_scores = []
    for tweet in tweets:
        cleaned_tweet = clean_text(tweet)
        analysis = TextBlob(cleaned_tweet)
        sentiment_scores.append(analysis.sentiment.polarity)
    
    if sentiment_scores:
        average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    else:
        average_sentiment = 0  # Default to neutral sentiment if no scores are available
    
    return round(average_sentiment, 2)

def fetch_trending_hashtags(tweets):
    """
    Extracts hashtags from a list of tweets and ranks them by frequency.
    
    Args:
        tweets (list): A list of tweet texts.
        
    Returns:
        list: A sorted list of hashtags ranked by frequency.
    """
    hashtags = []
    for tweet in tweets:
        hashtags.extend(re.findall(r"#(\w+)", tweet))
    
    hashtag_counts = {tag: hashtags.count(tag) for tag in set(hashtags)}
    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_hashtags

# Example usage
if __name__ == "__main__":
    sample_tweets = [
        "I love $DOGE! It's going to the moon! 🚀 #DOGEArmy #Crypto",
        "Not feeling great about $SHIBA today... seems bearish. #SHIB #CryptoNews",
        "$PEPE might pump soon, strong support at current levels. #PEPE",
    ]
    
    avg_sentiment = analyze_sentiment(sample_tweets)
    print(f"Average Sentiment Score: {avg_sentiment}")
    
    trending_hashtags = fetch_trending_hashtags(sample_tweets)
    print("Trending Hashtags:")
    for tag, count in trending_hashtags:
        print(f"#{tag}: {count} mentions")
