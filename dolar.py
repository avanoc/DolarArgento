import requests
from bs4 import BeautifulSoup as bs

# Define websites to scrap
DolarHoy = 'https://dolarhoy.com/'
Buenbit = 'https://www.infodolar.com/cotizacion-dolar-entidad-buenbit.aspx'

# Get "Dolar Blue" and "Dolar Cripto" & "Dolar Tarjeta" exchange rate from "DolarHoy"
def dolarBlue():
        try:
                URLDolarHoy = requests.get(DolarHoy)
                if URLDolarHoy.ok:
                        ContentDolarHoy = URLDolarHoy.content
                        SoupDolarHoy = bs(ContentDolarHoy,"lxml")
                        blue = SoupDolarHoy.find(class_='tile is-child only-mobile').find(class_='venta').find(class_='val').string
                        return blue
        except requests.exceptions.ConnectionError as exc:
                print(exc)

def dolarTC():
        try:
                URLDolarHoy = requests.get(DolarHoy)
                if URLDolarHoy.ok:
                        ContentDolarHoy = URLDolarHoy.content
                        SoupDolarHoy = bs(ContentDolarHoy,"lxml")
                        tarjeta = SoupDolarHoy.find_all(class_='val')
                        tarjeta = tarjeta[12].get_text().strip()
                        return tarjeta
        except requests.exceptions.ConnectionError as exc:
                print(exc)

# Get exchange rate from "Buenbit"
def dolarCripto():
        try:
                URLBuenbit = requests.get(Buenbit)
                if URLBuenbit.ok:
                        ContentBuenbit = URLBuenbit.content
                        SoupBuenbit = bs(ContentBuenbit,"lxml")
                        cripto = SoupBuenbit.find_all('td', attrs={'class':'colCompraVenta'})
                        cripto = cripto[2].get_text().strip()
                        return cripto
        except requests.exceptions.ConnectionError as exc:
                print(exc)