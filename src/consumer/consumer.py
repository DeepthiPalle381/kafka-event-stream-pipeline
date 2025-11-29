import json
from pathlib import Path
from datetime import datetime

import pandas as pd

TOPIC_FILE = Path("data/output/topic_user_events.jsonl")
OUTPUT_DIR = Path("data/output")

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"  # adjust if needed


def load_events_from_topic() -> pd.DataFrame:
    """Load events from the topic file into a DataFrame."""
    events = []

    if not TOPIC_FILE.exists():
        raise FileNotFoundError(f"Topic file not found: {TOPIC_FILE}")

    with TOPIC_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            evt = json.loads(line)
            events.append(evt)

    df = pd.DataFrame(events)
    if "event_time" not in df.columns:
        raise ValueError("Expected 'event_time' in events")

    # Try to parse timestamp
    try:
        df["event_time"] = pd.to_datetime(df["event_time"])
    except Exception:
        # If format mismatch, try generic parsing
        df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

    return df


def aggregate_events_by_minute(df: pd.DataFrame) -> pd.DataFrame:
    df["minute"] = df["event_time"].dt.floor("Min")
    agg = (
        df.groupby("minute")
        .size()
        .reset_index(name="events_count")
        .sort_values("minute")
    )
    return agg


def aggregate_events_by_type(df: pd.DataFrame) -> pd.DataFrame:
    if "event_type" not in df.columns:
        raise ValueError("Expected 'event_type' in events")
    agg = (
        df.groupby("event_type")
        .size()
        .reset_index(name="events_count")
        .sort_values("events_count", ascending=False)
    )
    return agg


def main():
    print(f"Reading events from topic file: {TOPIC_FILE}")
    df = load_events_from_topic()
    print(f"Loaded {len(df)} events")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    events_by_minute = aggregate_events_by_minute(df)
    events_by_type = aggregate_events_by_type(df)

    out_minute = OUTPUT_DIR / "events_by_minute.csv"
    out_type = OUTPUT_DIR / "events_by_type.csv"

    events_by_minute.to_csv(out_minute, index=False)
    events_by_type.to_csv(out_type, index=False)

    print(f"Saved events_by_minute to {out_minute}")
    print(f"Saved events_by_type to {out_type}")


if __name__ == "__main__":
    main()
