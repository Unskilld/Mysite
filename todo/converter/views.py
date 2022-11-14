import requests
import configparser

config = configparser.ConfigParser()
config['EXCHANGE'] = {'api':'cmr8yk9kKd5F43ML7okrBmB5W6OLO3cJ'}
with open('exchange_api_key.ini','w') as cfg:
        config.write(cfg)


# url = f"https://api.apilayer.com/currency_data/convert?to={currency}&from=USD&amount={amount}"

payload = {}
headers = {
    "apikey": f"{config['EXCHANGE']['api']}"
}
print(headers)
# response = requests.request("GET", url, headers=headers, data=payload)

# status_code = response.status_code
# result = response.text
