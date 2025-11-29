import pandas as pd
import json
import time
from pathlib import Path

SOURCE_FILE = Path("data/raw/events_stream_source.csv")
TOPIC_FILE = Path("data/output/topic_user_events.jsonl")

# Adjust these if your column names differ:
TIMESTAMP_COL = "event_time"
USER_COL = "user_id"
EVENT_TYPE_COL = "event_type"


def produce_events(sleep_seconds: float = 0.0) -> None:
    """Read events from CSV and write them as JSON lines to a topic file."""
    print(f"Reading events from {SOURCE_FILE}...")

    df = pd.read_csv(SOURCE_FILE)

    # Basic sanity check
    for col in [TIMESTAMP_COL, USER_COL, EVENT_TYPE_COL]:
        if col not in df.columns:
            raise ValueError(
                f"Column '{col}' not found in source file. "
                f"Available columns: {list(df.columns)}"
            )

    # Make sure output directory exists
    TOPIC_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Open topic file in append mode (simulate topic)
    with TOPIC_FILE.open("w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            event = {
                "event_time": str(row[TIMESTAMP_COL]),
                "user_id": str(row[USER_COL]),
                "event_type": str(row[EVENT_TYPE_COL]),
            }

            # Include any other useful columns if present
            for extra_col in ["product_id", "session_id"]:
                if extra_col in df.columns:
                    event[extra_col] = row[extra_col]

            f.write(json.dumps(event) + "\n")

            if sleep_seconds > 0:
                time.sleep(sleep_seconds)

    print(f"Finished writing {len(df)} events to {TOPIC_FILE}")


if __name__ == "__main__":
    # Set sleep_seconds > 0.0 if you want to visually simulate slower streaming
    produce_events(sleep_seconds=0.0)
