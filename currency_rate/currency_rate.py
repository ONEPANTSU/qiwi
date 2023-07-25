from abc import ABC, abstractmethod


class CurrencyRate(ABC):
    @abstractmethod
    def _get_currency_rate_info(self, code, date):
        pass
