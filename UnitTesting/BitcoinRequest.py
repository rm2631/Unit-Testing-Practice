
import requests
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

class BitcoinRequest():
    def __init__(self):
        self.rate_USD = None
        self.rate_CAD = None

    def get_Bitcoin_price(self) -> tuple:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        self.rate_USD = locale.atof(response.json()['bpi']['USD']['rate'])
        print(f"Current rate in USD is {self.rate_USD}")
        return self.rate_USD, response.status_code

    def convert_to_CAD(self, fx_rate: float) -> float:
        if self.rate_USD is None: self.get_Bitcoin_price()
        self.rate_CAD = self.rate_USD * fx_rate if self.rate_CAD is None else self.rate_CAD
        print(f"Current rate in CAD is {self.rate_CAD}")
        return self.rate_CAD, self.rate_USD

if __name__ == "__main__":
    bitcoinRequest = BitcoinRequest()
    rate = bitcoinRequest.convert_to_CAD(1.3)
    pass