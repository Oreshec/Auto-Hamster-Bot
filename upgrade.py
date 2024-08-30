import requests
import time
import conf
import traceback

def make_request(url, headers, payload):
    """Helper function to make API requests and handle errors."""
    try:
        response = requests.post(url, json=payload, headers=headers)
        print('Status: ', response.status_code)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Ошибка при запросе {url}:\n', e)
        return None
    except Exception:
        print('Ошибка:\n', traceback.format_exc())
        return None

def upgrade_card(id_card=None):
    url_buy = "https://api.hamsterkombatgame.io/clicker/buy-upgrade"
    timestamp = int(time.time())
    payload = {
        "upgradeId": f"{id_card}",
        "timestamp": timestamp
    }
    headers = {"Authorization": f"{conf.authorization}"}
    data = make_request(url_buy, headers, payload)
    if data:
        print(f"Покупка карты {id_card} прошла успешно!")
    else:
        print('Оплата не прошла или произошла ошибка.')

if __name__ == '__main__':
    upgrade_card()
