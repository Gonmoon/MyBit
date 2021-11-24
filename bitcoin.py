import requests
import re


class bitcoin():
	def __init__(self, address):
		# -----Кошелёк BTC-----
		self.url_purse = 'https://www.blockchain.com/btc/address/' + address

	def get_balance(self):
		# ------получения баланса в BTC-----
		page_purse = requests.get(self.url_purse).text
		btc_purse = re.search(r'Balance</span></div></div><div class="sc-8sty72-0 bFeqhe"><span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" opacity="1">(\S+)', page_purse)
		btc_balance = str(btc_purse.group(1)) + ' BTC'
		# -----Рыночная цена BTC-----
		page_market = requests.get('https://coinmarketcap.com/currencies/bitcoin').text
		usd_market = re.search(r'priceValue "><span>.(\d+.\d+)', page_market)
		usd_market = int(usd_market.group(1).replace(',',''))
		# ------перевод из BTC в USD-----
		usd_balance = usd_market * float(btc_purse.group(1).replace(',','.'))
		usd_balance = str(usd_balance) + ' $'
		# -----Направление рынка-----
		if re.search(r'icon-Caret-down', page_market) == None:
			arrow = ' ↗️'
		else:
			arrow = ' ↘️'
		usd_market = str(usd_market) + '$' + arrow
		return btc_balance, usd_balance, usd_market
