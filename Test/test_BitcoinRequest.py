import pytest
from UnitTesting.BitcoinRequest import BitcoinRequest

@pytest.fixture
def exchange_rate():
    """I know this wasn't necessary but I wanted to use fixtures"""
    return float(1.28)


def test_get_Bitcoin_price():
    bitcoinRequest = BitcoinRequest()
    rate, status_code = bitcoinRequest.get_Bitcoin_price()
    assert status_code == 200, "Request to Coindesk API as failed"

def test_convert_to_CAD(exchange_rate):
    bitcoinRequest = BitcoinRequest()
    CAD, USD = bitcoinRequest.convert_to_CAD(exchange_rate)
    assert CAD/USD == exchange_rate, "Conversion from USD to CAD is wrong"
