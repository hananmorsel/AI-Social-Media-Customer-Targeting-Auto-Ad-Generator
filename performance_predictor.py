import re

def predict_performance(text):
    length = len(text.split())
    emojis = len(re.findall(r"[😀-🙏🔥✨⭐❤️💥💯]", text))
    hashtags = text.count("#")
    score = (length * 0.01) + (emojis * 0.3) + (hashtags * 0.2)
    score = min(round(score, 2), 1.0)
    return score
