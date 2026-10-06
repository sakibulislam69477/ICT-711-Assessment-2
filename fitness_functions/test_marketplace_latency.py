from time import perf_counter
from prototype.marketplace import Marketplace

def test_marketplace_latency():
    marketplace = Marketplace()

    for i in range(100):
        marketplace.create_offer(
            seller_id=f"SELLER-{i}",
            energy_kwh=5,
            price_per_kwh=0.25
        )

    response_times = []
    for _ in range(500):
        start = perf_counter()
        marketplace.list_offers()
        response_times.append(perf_counter() - start)

    response_times.sort()
    index = int(len(response_times) * 0.95) - 1
    p95 = response_times[index]

    assert p95 < 0.5
