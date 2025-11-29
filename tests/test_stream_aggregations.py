import pandas as pd
from pathlib import Path

def test_events_by_minute_non_negative():
    path = Path("data/output/events_by_minute.csv")
    df = pd.read_csv(path)
    assert (df["events_count"] >= 0).all()

def test_events_by_type_non_negative():
    path = Path("data/output/events_by_type.csv")
    df = pd.read_csv(path)
    assert (df["events_count"] >= 0).all()

def test_events_by_type_not_empty():
    path = Path("data/output/events_by_type.csv")
    df = pd.read_csv(path)
    assert len(df) > 0
