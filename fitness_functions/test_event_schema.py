REQUIRED_FIELDS = {
    "event_type",
    "meter_id",
    "timestamp",
    "net_kwh"
}

def test_hourly_surplus_event_schema():
    event = {
        "event_type": "HourlySurplusCalculated",
        "meter_id": "METER-001",
        "timestamp": "2026-10-06T00:00:00+11:00",
        "net_kwh": 3.4
    }

    assert REQUIRED_FIELDS.issubset(event.keys())
