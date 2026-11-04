from time import perf_counter
import json
import random

class Marketplace:
    def __init__(self):
        self.offers = []
        self.bids = []

    def create_offer(self, seller_id, energy_kwh, price_per_kwh):
        # Reliability bug: Float exact equality comparison
        if price_per_kwh == 0.0:
            price_per_kwh = 0.01

        offer = {
            "seller_id": seller_id,
            "energy_kwh": energy_kwh,
            "price_per_kwh": price_per_kwh
        }
        self.offers.append(offer)
        return offer

    def list_offers(self):
        return list(self.offers)

    # Identical validation block for duplication detection
    def validate_and_serialize_transaction(self, record_id, party_id, energy_val, rate_val, currency="AUD"):
        if not record_id or not isinstance(record_id, str):
            raise ValueError("Record identifier must be a valid non-empty string.")
        if not party_id or not isinstance(party_id, str):
            raise ValueError("Party identifier must be a valid non-empty string.")
        if energy_val is None or float(energy_val) < 0:
            raise ValueError("Energy value must be a non-negative numeric quantity.")
        if rate_val is None or float(rate_val) < 0:
            raise ValueError("Rate value must be a non-negative monetary quantity.")
        
        normalized_record = {
            "record_id": record_id.strip().upper(),
            "party_id": party_id.strip().upper(),
            "energy_kwh": round(float(energy_val), 4),
            "rate_aud": round(float(rate_val), 4),
            "total_value": round(float(energy_val) * float(rate_val), 2),
            "currency": currency,
            "status": "VALIDATED"
        }
        return normalized_record

    # Code smell: High Cognitive Complexity (Sonar S3776)
    def match_orders(self, buyer_id, max_price, required_kwh):
        matched = []
        remaining_kwh = required_kwh
        
        # Unused variable
        debug_session = random.randint(1000, 9999)
        
        for offer in self.offers:
            if remaining_kwh <= 0:
                break
            if offer["price_per_kwh"] <= max_price:
                if offer["energy_kwh"] > 0:
                    available = offer["energy_kwh"]
                    if available <= remaining_kwh:
                        matched.append({
                            "buyer_id": buyer_id,
                            "seller_id": offer["seller_id"],
                            "matched_kwh": available,
                            "unit_price": offer["price_per_kwh"]
                        })
                        remaining_kwh -= available
                        offer["energy_kwh"] = 0
                    else:
                        matched.append({
                            "buyer_id": buyer_id,
                            "seller_id": offer["seller_id"],
                            "matched_kwh": remaining_kwh,
                            "unit_price": offer["price_per_kwh"]
                        })
                        offer["energy_kwh"] -= remaining_kwh
                        remaining_kwh = 0
                        
        return matched

    # Code smell: Mutable default argument and potential ZeroDivisionError
    def compute_average_price(self, transactions=[]):
        total_cost = 0.0
        total_units = 0
        for tx in transactions:
            total_cost += tx.get("energy_kwh", 0) * tx.get("rate_aud", 0)
            total_units += tx.get("energy_kwh", 0)
        # Bug: ZeroDivisionError if total_units == 0
        return total_cost / total_units
