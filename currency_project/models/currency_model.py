import requests
import time
from vietnam_number import n2w
from num2words import num2words

class CurrencyModel:
    _instance = None
    _cache = None
    _last_update = 0
    _cache_duration = 3600

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrencyModel, cls).__new__(cls)
        return cls._instance

    def get_all_rates(self):
        current_time = time.time()
        if self._cache and (current_time - self._last_update < self._cache_duration):
            return self._cache

        url = "https://api.exchangerate-api.com/v4/latest/USD"
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            self._cache = data['rates']
            self._last_update = current_time
            return self._cache
        except Exception as e:
            raise Exception(f"API Connection Error: {str(e)}")

    def calculate_conversion(self, amount, from_curr, to_curr):
        rates = self.get_all_rates()
        if from_curr not in rates or to_curr not in rates:
            raise ValueError("Invalid currency code!")
        return (amount / rates[from_curr]) * rates[to_curr]

    def get_text_representation(self, amount, currency_code):
        """Convert number to words based on currency code (VND -> Vietnamese, Others -> English)"""
        try:
            val = int(amount)
            if currency_code == "VND":
                return n2w(str(val)).capitalize() + " dong"
            else:
                text = num2words(val, lang='en')
                return text.capitalize() + f" {currency_code}"
        except:
            return ""