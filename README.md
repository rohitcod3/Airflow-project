# 🐦 Twitter ETL Pipeline with Apache Airflow on AWS

This project demonstrates a complete end-to-end ETL pipeline for extracting tweets from the Twitter API, transforming the data using pandas, and storing the results in AWS S3. The workflow is orchestrated using Apache Airflow and deployed on an EC2 instance running Ubuntu.

---

## 🚀 Tech Stack

- **Python**
- **Tweepy** (Twitter API)
- **pandas** (Data transformation)
- **Apache Airflow** (Workflow orchestration)
- **AWS EC2** (Airflow hosting)
- **AWS S3** (Cloud storage)

---


## 🔐 Environment Variables

Create a `.env` file in the `root` folder with your credentials:

```

> You only need the `TWITTER_BEARER_TOKEN` if you’re using Twitter’s v2 API with bearer authentication (no consumer keys or access tokens needed).

```

---

## 💠 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/twitter-airflow-pipeline.git
cd twitter-airflow-pipeline
```

### 2. Set Up Python Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Deploy to EC2
- Launch a Ubuntu-based EC2 instance (t3.medium recommended)
- SSH into the instance and install Python, Airflow, and required packages
- Transfer project files to the instance
- Run the Airflow webserver and scheduler

### 4. Start Airflow
```bash
airflow db init
airflow scheduler &
airflow webserver -p 8080
```

---

## 🗓 DAG Overview

The Airflow DAG is configured to:
- Extract tweets from a specific user using Tweepy
- Transform the tweet data using pandas
- Upload the result as a CSV file to an S3 bucket

You can monitor the DAG run status via the Airflow UI hosted on your EC2 instance.

---

## 📦 Output Example

Sample data stored in S3:

| username   | tweet text                        | likes | retweets | timestamp           |
|------------|------------------------------------|--------|----------|----------------------|
| elonmusk   | Just launched Starship! 🚀         | 523K   | 48.1K    | 2024-04-18 10:34:00  |

---

## 📌 Future Improvements
- Add sentiment analysis to tweets
- Stream tweets continuously via Twitter’s streaming API
- Build a dashboard with Streamlit to visualize results

---

## 📧 Contact

If you have questions, ideas, or feedback, feel free to open an issue or reach out.

---

## 📜 License

This project is licensed under the MIT License.

