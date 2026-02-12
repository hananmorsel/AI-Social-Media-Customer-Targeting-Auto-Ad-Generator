import pandas as pd

def recommend_post_times(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour

    best_hours = df.groupby("hour")['likes'].mean().sort_values(ascending=False)
    return {
        "best_hours": list(best_hours.index[:3]),
        "recommendation": f"Post at {list(best_hours.index[:3])} for highest engagement."
    }
