from time import perf_counter

def process_readings(readings):
    processed = []
    for reading in readings:
        generation = float(reading["generation_kw"])
        consumption = float(reading["consumption_kw"])
        processed.append({
            "meter_id": reading["meter_id"],
            "net_kw": generation - consumption
        })
    return processed

def measure_throughput(readings):
    start = perf_counter()
    process_readings(readings)
    elapsed = perf_counter() - start
    if elapsed == 0:
        return float("inf")
    return len(readings) / elapsed
