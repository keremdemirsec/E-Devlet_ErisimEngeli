# Coded By Kerem Demir
# 06/04/2024 
# E-Devlet Erişim Engeli Sorgulama

import argparse
import requests
from bs4 import BeautifulSoup

class WebsiteAccessChecker:
    def __init__(self, url, cookies, headers):
        self.url = url
        self.cookies = cookies
        self.headers = headers

    def check_access(self, website, token):
        payload = {
            "website": website,
            "token": token,
            "btn": "Sorgula"
        }

        response = requests.post(self.url, cookies=self.cookies, headers=self.headers, data=payload)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.find("table", {"class": "resultTable striped"})
            if result:
                tbody = result.find("tbody")
                if tbody:
                    tr = tbody.find_all("tr")
                    for row in tr:
                        print(row.text.strip())
                else:
                    print("Tablo içeriği bulunamadı.")
            else:
                print("Sonuç tablosu bulunamadı.")
        else:
            print(f"Hata: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='E-Devlet Erişim Engeli Sorgulama')
    parser.add_argument('--domain', required=True, help='Erişim engeli sorgulanacak domain')
    parser.add_argument('--token', required=True, help='Token verisi')
    args = parser.parse_args()

    url = "https://www.turkiye.gov.tr/esb-web-sitesi-erisim-engeli-sorgulama?submit"
    cookies = {
        "ridbb": "COOKIE",
        "w3p": "COOKIE",
        "language": "COOKIE",
        "_lastptts": "COOKIE",
        "_uid": "COOKIE",
        "TS015d3f68": "COOKIE",
        "TURKIYESESSIONID": "COOKIE",
        "w3a": "COOKIE"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.9999.99 Safari/537.36",
    }
    checker = WebsiteAccessChecker(url, cookies, headers)
    checker.check_access(args.domain, args.token)
