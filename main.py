import asyncio
import pandas as pd
import conf
import info_profile
import numpy as np
import traceback
import Card
from Request import Request

save_to_excel = False
UPGRADE = True


def process_data(data):
	"""Process the data into a DataFrame and filter it."""
	try:
		df = pd.DataFrame(data['upgradesForBuy'])
		# Efficient filtering
		df = df[(df['isAvailable']) & (~df['isExpired'])]
		df = df[(df['level'] < df['maxLevel']) | df['maxLevel'].isna()]
		df['profit'] = df['price'] / df['profitPerHourDelta']
		df.sort_values(by='profit', inplace=True)
		return df
	except:
		print('Ошибка в обработке данных:\n', traceback.format_exc())
		return None


async def save_to_excel_file(df, key):
	"""Save the DataFrame to an Excel file."""
	try:
		name_file = await info_profile.get_info_profile(key=key)
		df.to_excel(f"{name_file}.xlsx", sheet_name='hamster')
		print('Save to Excel')
	except:
		print('Ошибка при сохранении в Excel:\n', traceback.format_exc())


async def perform_upgrade(df, key):
	"""Attempt to upgrade cards based on current money asynchronously."""
	try:
		diamond = await Request(key=key).get_info_diamond()
		print('__________________________________________________________________')
		index = df.index[:5].tolist()
		for i in index:
			card = Card.Card()
			card_id = df.at[i, 'id']
			card_price = df.at[i, 'price']
			card_cooldown = df.at[i, 'cooldownSeconds']
			card_name = df.at[i, "name"]
			card_profit_per_hour_delta = df.at[i, "profitPerHourDelta"]
			card_is_expired = df.at[i, "isExpired"]
			card_is_available = df.at[i, "isExpired"]
			card_new = card.Card(card_id=card_id, card_price=card_price, card_name=card_name,
			                     card_cooldown=card_cooldown,
			                     card_profit_per_hour_delta=card_profit_per_hour_delta,
			                     card_is_available=card_is_available,
			                     card_is_expired=card_is_expired)
			if card_new.card_cooldown <= 0 or np.isnan(card_cooldown):
				print('Кд на ', card_id, ' нет')
				if diamond >= card_price:
					diamond = await info_profile.get_info_diamond(key=key)
					if diamond >= card_price:
						print('Деньга на ', card_id, ' есть\n')
						await Request(key=key).upgrade_card(card_id=card_id)
				else:
					print(
						f'Алмазов нет на {df.at[i, "id"]} стоимостью {card_price} алмазов. Сейчас алмазов: {diamond}\n')
			elif card_cooldown > 0:
				print(f'{card_id} в кд {card_cooldown}\n')
		print('__________________________________________________________________')
	except:
		print('Ошибка при обновлении карты:\n', traceback.format_exc())
		await asyncio.sleep(60)


async def main():
	while True:
		try:
			for key in conf.authorization:
				await Request(key=key).get_info_profile()
				data = await Request(key=key).upgrades_for_buy()
				if data is None:
					return

				df = process_data(data)
				if df is None or df.empty:
					return

				if save_to_excel:
					await save_to_excel_file(df, key=key)

				if UPGRADE:
					await perform_upgrade(df, key=key)
			await asyncio.sleep(60)
		except:
			print(traceback.format_exc())
			await asyncio.sleep(60)
			await main()


# Running the main function asynchronously
asyncio.run(main())
