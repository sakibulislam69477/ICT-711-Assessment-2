from prototype.settlement import SettlementService

def test_duplicate_transaction_creates_one_ledger_entry():
    settlement = SettlementService()

    settlement.settle("TX10025", 18.50)
    settlement.settle("TX10025", 18.50)
    settlement.settle("TX10025", 18.50)

    assert len(settlement.ledger) == 1
    assert settlement.ledger[0]["transaction_id"] == "TX10025"
