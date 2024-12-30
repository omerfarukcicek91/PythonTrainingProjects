import requests
from bs4 import BeautifulSoup

# Amazon ürün URL'si
url = input("Please enter URL: ").__add__("''")

# URL geçerliliğini kontrol et
if not url.startswith("http"):
    print("Geçerli bir URL giriniz.")
    exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response = requests.get(url, headers=headers)

# HTTP durum kodunu kontrol et
if response.status_code != 200:
    print(f"HTTP isteği başarısız oldu. Durum kodu: {response.status_code}")
    exit()

html_content = response.content

# HTML içeriğini parse et
soup = BeautifulSoup(html_content, 'html.parser')

# Fiyat bilgisini bulmaya çalış
price_span = soup.find('span', {'class': 'a-offscreen'})
if not price_span:
    price_span = soup.find('span', {'class': 'a-price-whole'})  # Alternatif kontrol

# Fiyat bilgisini al ve yazdır
if price_span:
    price = price_span.get_text(strip=True)  # Fiyat bilgisini al
    print(f"Ürünün fiyatı: {price}")
else:
    print("Fiyat bilgisi bulunamadı.")


