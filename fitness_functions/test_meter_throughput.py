from prototype.smart_meter import measure_throughput

def test_meter_throughput():
    readings = [
        {
            "meter_id": f"METER-{i}",
            "generation_kw": 4.2,
            "consumption_kw": 2.8
        }
        for i in range(10000)
    ]

    throughput = measure_throughput(readings)
    assert throughput >= 1000
