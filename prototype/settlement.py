class SettlementService:
    def __init__(self):
        self.processed_transactions = set()
        self.ledger = []

    def settle(self, transaction_id, amount):
        if transaction_id in self.processed_transactions:
            return "already_processed"

        self.processed_transactions.add(transaction_id)
        self.ledger.append({
            "transaction_id": transaction_id,
            "amount": amount
        })
        return "processed"
