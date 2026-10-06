class Marketplace:
    def __init__(self):
        self.offers = []

    def create_offer(self, seller_id, energy_kwh, price_per_kwh):
        offer = {
            "seller_id": seller_id,
            "energy_kwh": energy_kwh,
            "price_per_kwh": price_per_kwh
        }
        self.offers.append(offer)
        return offer

    def list_offers(self):
        return list(self.offers)
