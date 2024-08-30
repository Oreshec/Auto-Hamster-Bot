import time
import traceback
import requests
import pandas as pd
import conf
import info_profile
import upgrade

save_to_excel = False
UPGRADE = True

def fetch_data():
    """Fetch data from the API and return as JSON."""
    url_info = "https://api.hamsterkombatgame.io/clicker/upgrades-for-buy"
    headers = {
        "Authorization": f"{conf.authorization}"
    }
    response = requests.post(url_info, json="", headers=headers)
    print('Получение информации о картах')
    print('Status: ', response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        print('Ошибка получения данных от API')
        return None

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

def save_to_excel_file(df):
    """Save the DataFrame to an Excel file."""
    try:
        name_file = f'{info_profile.get_info_profile()}'
        df.to_excel(f"{name_file}.xlsx", sheet_name='hamster')
        print('Save to Excel')
    except Exception:
        print('Ошибка при сохранении в Excel:\n', traceback.format_exc())

def perform_upgrade(df):
    """Attempt to upgrade cards based on current money."""
    try:
        index = df.index[:5].tolist()
        money = info_profile.get_info_money()
        for i in index:
            price = df.at[i, 'price']
            if money > price:
                id_card = df.at[i, 'id']
                print('Деньга на ', id_card, ' есть')
                cooldown = df.at[i, 'cooldownSeconds']
                if cooldown <= 0:
                    print('Кд тоже нет покупаю')
                    upgrade.upgrade_card(id_card=id_card)
                else:
                    print(f'Кд {cooldown}\n')
            else:
                print(f'Деньга нет на {df.at[i, "id"]} стоимостью {price} монет. Сейчас деняк: {money}')

        min_cd = df['cooldownSeconds'][:5].min()
        print('Сон на: ', min_cd)
        time.sleep(min_cd)
    except Exception:
        print('Ошибка при обновлении карты:\n', traceback.format_exc())

def main():
    data = fetch_data()
    if data is None:
        return

    df = process_data(data)
    if df is None or df.empty:
        return

    if save_to_excel:
        save_to_excel_file(df)

    if UPGRADE:
        perform_upgrade(df)

if __name__ == "__main__":
    main()
