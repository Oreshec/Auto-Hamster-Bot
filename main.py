import asyncio
import json
import traceback
import conf
from Card import Card
from Request import Request

UPGRADE = True
PRINT_INFO_CARD = False


async def sort_data(data):
	"""Process the data into a DataFrame and filter it."""
	try:
		objects = [Card(**upgrade) for upgrade in data["upgradesForBuy"]]
		filtered_objects = [
			obj for obj in objects
			if (obj.get_maxLevel() is None or obj.get_level() <= obj.get_maxLevel())
			   and not obj.get_isExpired() and obj.get_isAvailable()
		]
		sorted_objects = sorted(filtered_objects, key=lambda x: x.get_profit())
	except json.JSONDecodeError as e:
		print(f"Ошибка при декодировании JSON: {e}")
		return None
	return sorted_objects


async def upgrade_card(card, diamond, req):
	"""Upgrade a single card asynchronously."""
	if card.get_cooldownSeconds() <= 0:
		print('Кд на ', card.get_name(), ' нет')
		if diamond >= card.get_price():
			diamond = await req.get_info_diamond()  # Обновляем количество алмазов
			if diamond >= card.get_price():
				print('Деньга на ', card.get_name(), ' есть')
				await req.card_upgrade(card_id=card.get_id())
			else:
				print(f'Алмазов нет на {card.get_name()} стоимостью {card.get_price()} алмазов.')
				print(f' Сейчас алмазов: {diamond}')
		else:
			print(f'Алмазов нет на {card.get_name()} стоимостью {card.get_price()} алмазов.')
			print(f'Сейчас алмазов: {diamond}')
	else:
		print(f'{card.get_name()} в кд {card.get_cooldownSeconds()}')
	print("")
	return diamond


async def perform_upgrade(data, req):
	"""Attempt to upgrade cards based on current money asynchronously."""
	try:
		diamond = await req.get_info_diamond()
		print('__________________________________________________________________')
		data_limited = data[:5]
		# Создаем задачи для обновления каждой карты
		tasks = []
		for card in data_limited:
			if PRINT_INFO_CARD:
				print("_=_= CARD INFO =_=_=")
				print("Card name: ", card.get_name())
				print("Card ID: ", card.get_id())
				print("Cooldown: ", card.get_cooldownSeconds())
				print("Price: ", card.get_price())
				print("Profit Delta: ", card.get_profitPerHourDelta())
				print("Profit: ", card.get_profit())
				print("level: ", card.get_level())
				print("Max level: ", card.get_maxLevel())
				print("_=_=_=_=_=_=_=_=_=_=")

			tasks.append(upgrade_card(card, diamond, req))

		# Запускаем все задачи параллельно
		diamond_updates = await asyncio.gather(*tasks)
		diamond = max(diamond_updates)  # Обновляем количество алмазов после всех операций
		print('__________________________________________________________________')
	except:
		print('Ошибка при обновлении карты:\n', traceback.format_exc())
		await asyncio.sleep(60)


async def main():
	while True:
		try:
			for key in conf.authorization:
				req = Request(key=key)
				await req.get_info_profile()
				data = await req.card_list()
				if data is None:
					return

				data = await sort_data(data)

				if UPGRADE and data:
					await perform_upgrade(data=data, req=req)
			await asyncio.sleep(60)
		except:
			print(traceback.format_exc())
			await asyncio.sleep(60)
			await main()


# Running the main function asynchronously
asyncio.run(main())
