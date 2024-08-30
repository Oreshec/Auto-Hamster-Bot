import time

import requests
import pandas as pd
import conf
import info_profile
import upgrade

save_to_excel = False
UPGRADE = True


def main():
    # Просто получение информации
    data = response.json()
    print(data)
    df = pd.DataFrame(data['upgradesForBuy'])

    # Удаление недоступных и истекших карт
    df.drop(df[df['isAvailable'] == False].index, inplace=True)
    df.drop(df[df['isExpired'] == True].index, inplace=True)
    df.drop(df[df['cooldownSeconds'] > 0].index, inplace=True)

    # Деление цены на доход в час для выявления самой выгодной карты
    df['profit'] = df['price'] / df['profitPerHourDelta']
    df.sort_values(by="profit", inplace=True)
    print('Top 5\n', df[['id', 'profit']][:5])

    index = df.index[0]

    # сохранение в Excel
    if save_to_excel:
        try:
            name_file = f'{info_profile.get_info_profile()}'
            df.to_excel(f"{name_file}.xlsx", sheet_name='hamster')
            print('Save to Excel')
        except Exception as e:
            print(e)
            time.sleep(10)
            main()
    if UPGRADE:
        if info_profile.get_info_money() > df['price'][index]:
            print('Деньга есть, покупаю')
            card = df['id'][index]
            upgrade.upgrade_card(id_card=card)
            print("Прошло", card)
        else:
            print('Деньга нет на', df['id'][index], df['price'][index], 'Сейчас деняк:', info_profile.get_info_money())


if __name__ == "__main__":
    url_info = "https://api.hamsterkombatgame.io/clicker/upgrades-for-buy"

    payload = ""
    headers = {
        "Authorization": f"{conf.authorization}"}
    # запрос
    response = requests.post(url_info, json=payload, headers=headers)
    main()
