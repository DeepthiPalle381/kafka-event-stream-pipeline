# Kafka Event Stream Pipeline

This project simulates a real-time data pipeline using Kafka-style event streaming.
It reads user events from a historical CSV file, publishes them as a stream of messages to a Kafka topic (or simulated queue), and consumes them to build real-time analytics outputs (events per minute, per user, and by event type).

## Goals
- Simulate real-time event ingestion from a CSV source
- Implement a producer that sends events to a Kafka topic (or simulated topic)
- Implement a consumer that aggregates streaming events in near real-time
- Write aggregated outputs to data/output/ for analytics and monitoring
- (Optional) Use Docker and a real Kafka cluster for a more realistic setup

