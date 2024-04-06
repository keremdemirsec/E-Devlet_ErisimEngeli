# E-Devlet Erişim Engeli Sorgulama

Bu proje, belirtilen bir web sitesinin Türkiye Cumhuriyeti e-Devlet Portalı'nda erişim engeli olup olmadığını kontrol eder.

## Başlangıç

Projenin yerel bir kopyasını almak ve çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

Projenin çalışması için aşağıdaki yazılımlara ihtiyaç vardır:

- Python
- Requests
- BeautifulSoup
- argparse

### Kurulum

1. Bu depoyu klonlayın:

    ```bash
    git clone https://github.com/keremdemirsec/E-Devlet_ErisimEngeli
    ```

2. Proje klasörüne gidin:

    ```bash
    cd E-Devlet_ErisimEngeli
    ```

3. Kütüphaneleri Yükleyin:

    ```bash
    pip install requests
    pip install beautifulsoup4
    ```

4. Cookieleri Editle:

    ```bash
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
    ```
Kısmını editleyin ve kendi cookielerinizi ekleyin.

5. Kodu Çalıştırın:

    ```bash
    python3 main.py --domain site.com --token {Token}
    ```

## Kullanım

- `domaim`: Sorgulanacak Domaini belirtmek için kullanılır.
- `token`: Giden İstekteki Token'i belirtmemiz için kullanılır.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Detaylar için lisans dosyasını inceleyin.

## İletişim

Eğer sorularınız, önerileriniz veya geri bildirimleriniz varsa, bana [e-posta](mailto:keremdemirsec@email.com) üzerinden ulaşabilirsiniz.
