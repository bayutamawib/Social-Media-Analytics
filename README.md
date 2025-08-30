# 📊 Instagram Social Media Analytics

This repository contains scripts and visualizations for analyzing Instagram page-level engagement metrics. The dataset includes daily records of user interactions, reach, impressions, and video performance, enabling insights into audience behavior and content effectiveness.

## 📁 Dataset Overview

Each row in the dataset represents a single day of activity on an Instagram page. The following variables are included:

### 🗓️ Date
- The calendar date for each record.

### 👍 Daily New Likes
- Number of new users who liked the page that day.  
  *(Metric type: Unique Users)*

### 👎 Daily Unlikes
- Number of users who unliked the page that day.  
  *(Metric type: Unique Users)*

### 🔄 Daily Page Engaged Users
- Number of users who engaged with the page through any interaction (clicks, likes, comments, shares, etc.).  
  *(Metric type: Unique Users)*

### 💬 Daily Positive Feedback From Users – Comment
- Total number of positive comments received on the page.  
  *(Metric type: Total Count)*

### 📣 Daily Viral Reach
- Number of users who saw content from the page due to social interactions (e.g., a friend liked or commented).  
  *(Metric type: Unique Users)*

### 📈 Daily Viral Impressions
- Total number of times content from the page appeared on screens due to social interactions.  
  *(Metric type: Total Count)*

### 📰 Daily Viral Reach of Page Posts
- Number of users who saw a post from the page due to social interactions.  
  *(Metric type: Unique Users)*

### 📊 Daily Viral Impressions of Your Posts
- Total number of times posts from the page appeared on screens due to social interactions.  
  *(Metric type: Total Count)*

### 🎥 Daily Total Organic Views
- Total number of times a video was viewed through organic (non-paid) reach.  
  *(Metric type: Total Count)*

### ▶️ Daily Total Clicked Views
- Total number of times a video was played after a user clicked on it.  
  *(Metric type: Total Count)*

### 🔁 Daily Video Repeats
- Total number of times a video was re-watched beyond the first play.  
  *(Metric type: Total Count)*

---

## 📂 Repository Contents

- `socmedanalytics.ipynb`: Jupyter notebook for data exploration and visualization.
- `socmedanalytics.py`: Python script version for reproducible analysis.
- `dataset/`: Contains the cleaned dataset used for analysis.
- `output/`: Stores generated charts and summary visualizations.

---

## 📌 Notes

- All metrics are aggregated daily.
- Engagement metrics are based on unique users unless otherwise noted.
- Viral metrics reflect organic distribution driven by social interactions.

---

## 🔗 Author & Attribution

Created by [Bayutama](https://github.com/bayutamawib)  
Project repository: [Social Media Analytics](https://github.com/bayutamawib/Social-Media-Analytics)
Kaggle dataset: https://www.kaggle.com/code/salmaneunus/social-media-analysis-dataset-extracting-cleaning/input

