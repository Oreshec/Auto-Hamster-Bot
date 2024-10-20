import asyncio
import json
import time
import traceback
from importlib.metadata.diagnose import inspect

import aiohttp

import conf


class Request:
	def __init__(self, key):
		self.key = key

	# Upgrade
	async def __make_request(self, url, payload=None):
		"""Helper function to make asynchronous API requests and handle errors."""
		headers = {
			"Authorization": f"{self.key}"
		}
		try:
			async with aiohttp.ClientSession() as session:
				async with session.post(url, json=payload, headers=headers) as response:
					print(f'Связь с {url}')
					print('Status: ', response.status)
					response.raise_for_status()
					response_text = await response.text()
					data = json.loads(response_text)
					return data
		except aiohttp.ClientResponseError as e:
			print(f"Request failed: {e.status} {e.message}")
		except aiohttp.ClientError as e:
			print(f'Ошибка при запросе {url}:\n', e)
			return None
		except json.JSONDecodeError as e:
			print(f"Error decoding JSON: {e}")

		except:
			print('Ошибка:\n', traceback.format_exc())
			return None

	async def upgrade_card(self, card_id):
		url = "https://api.hamsterkombatgame.io/interlude/buy-upgrade"
		timestamp = int(time.time())
		payload = {
			"upgradeId": f"{card_id}",
			"timestamp": timestamp
		}
		print("Улучшение карты")
		data = self.__make_request(url=url, payload=payload)
		print(data)

	async def upgrades_for_buy(self):
		"""Fetch data from the API asynchronously and return as JSON."""
		url = "https://api.hamsterkombatgame.io/interlude/upgrades-for-buy"
		try:
			print("Получение информации по картам")
			data = await self.__make_request(url=url)
			print(data)
			return data
		except:
			print('Произошел прикок в upgrades_for_buy', traceback.format_exc())

	async def get_info_profile(self):
		url = "https://api.hamsterkombatgame.io/auth/account-info"
		data = await self.__make_request(url)
		try:
			if data:
				user_name = data.get('accountInfo', None).get('name', None)
				user_id = data.get("accountInfo", None).get("id", None)
				user_data = "Name: " + user_name + "\nID: " + user_id
				print(user_data)
				return
			return 'Unknown'
		except:
			print(f"Ошибка в {Request.get_info_profile.__name__}: s", traceback.format_exc())

	async def get_info_diamond(self):
		url = "https://api.hamsterkombatgame.io/interlude/sync"
		data = await self.__make_request(url=url)
		print(data)
		if data:
			if data.get('interludeUser'):
				info_diamond = data.get('interludeUser', {}).get('balanceDiamonds')
				print(info_diamond)
				return info_diamond
			else:
				print("Ошибка: data.get('interludeUser')")
		return 0

#asyncio.run(Request(conf.v1).get_info_diamond())
