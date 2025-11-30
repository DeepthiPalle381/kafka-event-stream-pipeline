# Kafka Event Stream Pipeline (Simulated Real-Time Streaming)

This project simulates a **real-time Kafka-style streaming pipeline** using a producer–consumer architecture.  
The producer streams user events from a CSV file into a simulated Kafka topic (JSON lines file), and the consumer reads from this topic to build **real-time analytics** such as events per minute and events per event type.

This pipeline mirrors real industry patterns for:
- clickstream processing  
- user behavior tracking  
- real-time dashboards  
- microservices-based event ingestion  

---

## 🚀 Goals

- Simulate **real-time event ingestion** from a historical CSV
- Build a **producer** that publishes messages to a “topic“
- Build a **consumer** that processes streaming events
- Generate real-time analytics such as:
  - Events per minute
  - Events by event_type
- Store analytics output in `data/output/`
- Add **pytest** data quality tests for aggregated results
- Provide code that can be easily extended to a **real Kafka cluster**

---

## 🧰 Tech Stack

- **Python**
- **Pandas**
- **Producer–Consumer Architecture**
- **JSONL as simulated Kafka topic**
- **Pytest** (data quality tests)
- *(Optional)* Docker + Kafka (`kafka-python` or Confluent)

---

## 📦 Dataset

This project uses a sample of user clickstream events taken from the **Project 2 dataset**.

Source file (copied into this project):

data/raw/events_stream_source.csv

---

Required columns:
- `event_time`
- `user_id`
- `event_type`
- optional: `product_id`, `session_id`

This dataset is replayed row-by-row by the producer to simulate real-time events.

---

## 🧱 Architecture (Kafka Real-Time Pipeline)

![Kafka Architecture](docs/kafka_architecture.png)

---

## 📂 Project Structure

```text
kafka-event-stream-pipeline/
├── data/
│ ├── raw/
│ │ └── events_stream_source.csv
│ └── output/
│ ├── topic_user_events.jsonl
│ ├── events_by_minute.csv
│ └── events_by_type.csv
├── src/
│ ├── producer/
│ │ └── producer.py
│ └── consumer/
│ └── consumer.py
├── tests/
│ └── test_stream_aggregations.py
├── requirements.txt
├── docs/
├── docker/ # (optional Kafka cluster)
└── README.md

```


---

## ▶️ How to Run Locally

### **1. Clone the repository**
```bash
git clone https://github.com/DeepthiPalle381/kafka-event-stream-pipeline.git
cd kafka-event-stream-pipeline

```

### 2. Create & activate virtual environment (Windows)
```bash
python -m venv .venv
.venv\Scripts\activate

```

### 3. Install dependencies
```bash
pip install -r requirements.txt

```
## 🏁 Summary

This project demonstrates:

- Event streaming concepts

- Producer → topic → consumer pattern

- Real-time analytics generation

- Data pipeline engineering

- Testing real-time transformations

- A clean, modern project structure