from unittest.mock import patch
from currency_rate.cbr_currency_rate import CBRCurrencyRate


class TestCBRCurrencyRate:
    @patch("builtins.print")
    def test_get_currency_rate_success(self, mock_print):
        args = {"code": "USD", "date": "2022-10-08"}
        CBRCurrencyRate().get_currency_rate(date=args["date"], code=args["code"])
        mock_print.assert_called_with("USD (Доллар США): 61,2475")

    @patch("builtins.print")
    def test_get_currency_rate_invalid_date_format(self, mock_print):
        args = {"code": "USD", "date": "2021/09/01"}
        CBRCurrencyRate().get_currency_rate(date=args["date"], code=args["code"])
        mock_print.assert_called_with(
            "An error occurred: Invalid date format. Please use YYYY-MM-DD."
        )

    @patch("builtins.print")
    def test_get_currency_rate_invalid_currency_code(self, mock_print):
        args = {"code": "ABC", "date": "2022-10-08"}
        CBRCurrencyRate().get_currency_rate(date=args["date"], code=args["code"])
        mock_print.assert_called_with(
            "An error occurred: Invalid currency code. Please provide a valid ISO 4217 currency code."
        )
