import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# === 1. Load the Dataset ===
def load_data(file_path):
    df = pd.read_csv(file_path, sep=';', parse_dates=['Date'], dayfirst=True)
    # Convert index to strips
    df.columns = df.columns.str.strip()
    
    return df

# === 2. Prepare the Data ===
def prepare_data(df):

    # Convert published date to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter from April to June 2020
    df = df[(df['Date'] >= '2020-04-01') & (df['Date'] <= '2020-06-30')]

    # Set the date as index
    df.set_index('Date', inplace=True)

    return df

# === 3. Aggregate Data Weekly ===
def aggregate_weekly(df):
    weekly = df.resample('W').agg({
        'Daily New Likes': 'sum',
        'Daily Unlikes': 'sum',
        'Daily Page Engaged Users': 'sum',
        'Daily Viral Reach': 'sum',
        'Daily Viral impressions': 'sum',
        'Daily Viral Reach Of Page Posts': 'sum',
        'Daily Viral Impressions Of Your Posts': 'sum',
        'Daily Total Organic Views': 'sum',
        'Daily Total Clicked Views': 'sum',
        'Daily Video Repeats': 'sum', 
        'Daily Positive Feedback From Users - comment': 'sum'
    })

    # Rename column
    weekly = df.rename(columns={'Daily Positive Feedback From Users - comment': 'Daily Positive Comments'})
    return weekly

# === 4. Find the most frequent topic weekly ===
def weekly_topics(df):
    df = df.copy()
    
     # Convert index to strips
    df = df.reset_index()
    
    # Add week number
    df["Week"] = df["Date"].dt.isocalendar().week
    
    # Find the most frequent topic weekly
    weekly_tops = (
        df.groupby("Week")["Topic"]
        .agg(lambda x: x.value_counts().idxmax())
        .reset_index()
        .rename(columns={"Topic": "Dominant_Topic"})
    )

    return weekly_tops
    
# === 5. Plot Engagement Trends ===
def plot_engagement(weekly_df, output_folder="output"):
    weekly_df['Label'] = weekly_df['Date'].dt.strftime('%b %d') + ' - ' + weekly_df['Dominant_Topic'].str.slice(0, 10)
    os.makedirs(output_folder, exist_ok=True)
    sns.set(style="whitegrid")
    
    # --- PlotT 1: Engagement Metrics
    plt.figure(figsize=(14,7))
    plt.plot(weekly_df.index, weekly_df['Daily New Likes'], label='New Likes', marker='o')
    plt.plot(weekly_df.index, weekly_df['Daily Unlikes'], label='New Unlikes', marker='s')
    plt.plot(weekly_df.index, weekly_df['Daily Positive Comments'], label='Positive Comments', marker='^')
    plt.plot(weekly_df.index, weekly_df['Daily Page Engaged Users'], label='Page Engaged Users', marker='*')
    #plt.ylim(0, 2000) # Adjust based on your data
    plt.title("Social Media Engagement Over Time (Weekly)")
    plt.xlabel("Week")
    skip = 2  # Show every 2nd label
    plt.xticks(ticks=weekly_df.index[::skip], labels=weekly_df['Label'][::skip], rotation=45, fontsize=8)
    plt.ylabel("Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    # Save the plot
    file_path1 = os.path.join(output_folder, "engagement_trend.png")
    plt.savefig(file_path1)
    plt.show()

    # --- PlotT 2: Reach VS Impression Metrics
    plt.figure(figsize=(14,7))
    plt.plot(weekly_df.index, weekly_df['Daily Viral Reach'], label='Viral Reach', marker='o')
    plt.plot(weekly_df.index, weekly_df['Daily Viral impressions'], label='Viral impressions', marker='s')
    #plt.ylim(0, 2000) # Adjust based on your data
    plt.title("Reach VS Impression Metrics")
    plt.xlabel("Week")
    plt.xticks(ticks=weekly_df.index[::skip], labels=weekly_df['Label'][::skip], rotation=45, fontsize=8)
    plt.ylabel("Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    # Save the plot
    file_path2 = os.path.join(output_folder, "reachvsimpressions_trend.png")
    plt.savefig(file_path2)
    plt.show()

    # --- PlotT 3: Reach per posts VS Impression per posts Metrics
    plt.figure(figsize=(14,7))
    plt.plot(weekly_df.index, weekly_df['Daily Viral Reach Of Page Posts'], label='Viral Reach per Posts', marker='o')
    plt.plot(weekly_df.index, weekly_df['Daily Viral Impressions Of Your Posts'], label='Viral impressions per Posts', marker='s')
    #plt.ylim(0, 2000) # Adjust based on your data
    plt.title("Reach per Posts VS Impression per Posts Metrics")
    plt.xlabel("Week")
    plt.xticks(ticks=weekly_df.index[::skip], labels=weekly_df['Label'][::skip], rotation=45, fontsize=8)
    plt.ylabel("Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    # Save the plot
    file_path3 = os.path.join(output_folder, "reachvsimpressions_perposts.png")
    plt.savefig(file_path3)
    plt.show()

    # --- PlotT 4: Video Reach vs Impressions Metrics
    plt.figure(figsize=(14,7))
    plt.plot(weekly_df.index, weekly_df['Daily Total Organic Views'], label='Total Organic Views (not played)', marker='o')
    plt.plot(weekly_df.index, weekly_df['Daily Total Clicked Views'], label='Total Played Videos', marker='s')
    plt.plot(weekly_df.index, weekly_df['Daily Video Repeats'], label='Video Repeats', marker='^')
    #plt.ylim(0, 15000) # Adjust based on your data
    plt.title("Video Metrics")
    plt.xlabel("Week")
    plt.xticks(ticks=weekly_df.index[::skip], labels=weekly_df['Label'][::skip], rotation=45, fontsize=8)
    plt.ylabel("Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    # Save the plot
    file_path4 = os.path.join(output_folder, "videos_trend.png")
    plt.savefig(file_path4)
    plt.show()

# === 5. Main Function ===
def main():
    #Path to the dataset
    file_path = "/Users/narendrabayutamaw/Documents/Qarir Generator/AIEngineering (Homework)/Project Month 2/instagram_dataset.csv"

    # Load and process data
    df = load_data(file_path)
    df = prepare_data(df)
   
   # Define df
    weekly_df = aggregate_weekly(df)

    # Get dominant topics and merge for labelling
    weekly_df = weekly_df.reset_index()
    weekly_df["Week"] = weekly_df["Date"].dt.isocalendar().week
    topics = weekly_topics(df)
    weekly_df = pd.merge(weekly_df, topics, on="Week", how="left")

    # Plot and save
    plot_engagement(weekly_df)

# Run the app
if __name__ == "__main__":
    main()