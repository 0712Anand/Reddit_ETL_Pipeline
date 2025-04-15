# 🚀 Reddit ELT Pipeline: r/dataengineering → S3 → Redshift → Data Studio

This project implements a robust ELT (Extract, Load, Transform) pipeline for collecting Reddit posts and comments from the `r/dataengineering` subreddit. The pipeline loads raw data into AWS S3, transforms it using Amazon Redshift, and then feeds it to Google Data Studio for real-time visualization.

---

## 📊 Use Case

Gain insights into discussions, trends, and sentiment in the `r/dataengineering` subreddit by:

- Tracking post frequency and engagement
- Analyzing user activity
- Visualizing keyword trends over time
- Creating dashboards for analytics teams

---

## 🏗️ Architecture Overview

```mermaid
Flowchart 
    A[Reddit API] --> B[Extract Script]
    B --> C[S3 (Raw Data)]
    C --> D[Redshift (Staging & Transformation)]
    D --> E[Google Data Studio via Redshift Connector]

```
# 🚀 Quick Start
## 1. Clone the Repo
```bash
git clone https://github.com/0712Anand/Reddit_ETL_Pipeline
```
## 2. Set Up Environment Variables(config.conf)
```bash
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_user_agent

AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
S3_BUCKET_NAME=your_s3_bucket
REDSHIFT_CLUSTER_ID=your_redshift_cluster
REDSHIFT_DB=your_database
REDSHIFT_USER=your_user
REDSHIFT_PASSWORD=your_password
REDSHIFT_PORT=5439
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```