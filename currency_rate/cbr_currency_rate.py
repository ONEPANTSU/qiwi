import argparse
from datetime import datetime
from xml.etree import ElementTree

import requests

from currency_rate.currency_rate import CurrencyRate


class CBRCurrencyRate(CurrencyRate):
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req={converted_date}"

    def get_currency_rate(self, date, code):
        try:
            self._validate_date_format(date)
            self._validate_currency_code(code)

            currency_name, currency_rate = self._get_currency_rate_info(code, date)

            if currency_name and currency_rate:
                print(f"{code} ({currency_name}): {currency_rate}")
            else:
                print(f"Currency with code {code} not found for date {date}")

        except ValueError as ve:
            print(f"An error occurred: {str(ve)}")

    def _get_currency_rate_info(self, code, date):
        url = self.url.format(converted_date=self._convert_date(date))
        response = requests.get(url)
        root = ElementTree.fromstring(response.content)

        for currency in root.findall("Valute"):
            if currency.find("CharCode").text == code:
                name = currency.find("Name").text
                rate = currency.find("Value").text
                return name, rate

        return None, None

    def get_currency_rate_cmd(self):
        cmd_args = self._parse_args()
        self.get_currency_rate(date=cmd_args.date, code=cmd_args.code)

    @staticmethod
    def _parse_args():
        cmd_parser = argparse.ArgumentParser(
            description="Get currency rates from CBR RF"
        )
        cmd_parser.add_argument(
            "--code", type=str, help="Currency code (ISO 4217)", required=True
        )
        cmd_parser.add_argument(
            "--date", type=str, help="Date in format YYYY-MM-DD", required=True
        )
        cmd_args = cmd_parser.parse_args()
        return cmd_args

    @staticmethod
    def _convert_date(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        converted_date = date_obj.strftime("%d/%m/%Y")
        return converted_date

    @staticmethod
    def _validate_date_format(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def _validate_currency_code(self, code):
        url = self.url.format(
            converted_date=self._convert_date(datetime.now().strftime("%Y-%m-%d"))
        )
        response = requests.get(url)
        root = ElementTree.fromstring(response.content)

        currency_codes = [
            currency.find("CharCode").text for currency in root.findall("Valute")
        ]

        if code not in currency_codes:
            raise ValueError(
                "Invalid currency code. Please provide a valid ISO 4217 currency code."
            )
