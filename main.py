import asyncio
import aiohttp
import pandas as pd
import conf
import info_profile
import upgrade
import numpy as np
import traceback

save_to_excel = False
UPGRADE = True


async def fetch_data():
    """Fetch data from the API asynchronously and return as JSON."""
    url_info = "https://api.hamsterkombatgame.io/interlude/upgrades-for-buy"
    headers = {
        "Authorization": f"{conf.authorization}"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url_info, json="", headers=headers) as response:
                print(f'Получение информации о картах с {url_info}')
                print('Status: ', response.status)
                if response.status == 200:
                    return await response.json()
                else:
                    print('Ошибка получения данных от API')
                    await main()
                    return None
    except:
        print('Произошел прикок в fetch_data', traceback.format_exc())
        asyncio.run(main())


def process_data(data):
    """Process the data into a DataFrame and filter it."""
    try:
        df = pd.DataFrame(data['upgradesForBuy'])
        df = df[(df['isAvailable']) & (~df['isExpired'])]  # Efficient filtering
        df['profit'] = df['price'] / df['profitPerHourDelta']
        df.sort_values(by='profit', inplace=True)
        return df
    except Exception:
        print('Ошибка в обработке данных:\n', traceback.format_exc())
        return None


async def save_to_excel_file(df):
    """Save the DataFrame to an Excel file."""
    try:
        name_file = await info_profile.get_info_profile()
        df.to_excel(f"{name_file}.xlsx", sheet_name='hamster')
        print('Save to Excel')
    except Exception:
        print('Ошибка при сохранении в Excel:\n', traceback.format_exc())


async def perform_upgrade(df):
    """Attempt to upgrade cards based on current money asynchronously."""
    try:
        diamond = await info_profile.get_info_diamond()
        print('__________________________________________________________________')
        index = df.index[:5].tolist()
        for i in index:
            cooldown = df.at[i, 'cooldownSeconds']
            id_card = df.at[i, 'id']
            if cooldown <= 0 or np.isnan(cooldown):
                print('Кд на ', id_card, ' нет')
                price = df.at[i, 'price']
                if diamond >= price:
                    diamond = await info_profile.get_info_diamond()
                    if diamond >= price:
                        print('Деньга на ', id_card, ' есть\n')
                        await upgrade.upgrade_card(id_card=id_card)
                else:
                    print(f'Алмазов нет на {df.at[i, "id"]} стоимостью {price} алмазов. Сейчас алмазов: {diamond}\n')
            elif cooldown > 0:
                print(f'{id_card} в кд {cooldown}\n')

        min_cd = df['cooldownSeconds'][:5].min()
        if min_cd == 0:
            print('__________________________________________________________________')
            await asyncio.sleep(30)
            await main()
        else:
            print('Сон на: ', min_cd)
            print('__________________________________________________________________')
            await asyncio.sleep(min_cd)
            await main()
    except Exception:
        print('Ошибка при обновлении карты:\n', traceback.format_exc())
        await main()


async def main():
    data = await fetch_data()
    if data is None:
        return

    df = process_data(data)
    if df is None or df.empty:
        return

    if save_to_excel:
        await save_to_excel_file(df)

    if UPGRADE:
        await perform_upgrade(df)


# Running the main function asynchronously
asyncio.run(main())
