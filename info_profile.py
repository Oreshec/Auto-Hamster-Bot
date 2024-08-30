import requests
import conf
import traceback

def make_request(url, headers, payload=""):
    """Helper function to make API requests and handle errors."""
    try:
        response = requests.post(url, data=payload, headers=headers)
        print(f'Отправка запроса на {url}')
        print('Status: ', response.status_code)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f'Ошибка при запросе {url}:\n', e)
        return None
    except Exception:
        print('Ошибка:\n', traceback.format_exc())
        return None

def get_info_profile():
    url = "https://api.hamsterkombatgame.io/auth/account-info"
    headers = {"Authorization": f"{conf.authorization}"}
    data = make_request(url, headers)
    if data:
        profile_name = data.get('accountInfo', {}).get('name', 'Unknown')
        print('Имя профиля:', profile_name)
        return profile_name
    return 'Unknown'

def get_info_money():
    url = "https://api.hamsterkombatgame.io/clicker/sync"
    headers = {
        "Authorization": f"{conf.authorization}",
        "Priority": "u=4"
    }
    data = make_request(url, headers)
    if data:
        info_money = int(data.get('clickerUser', {}).get('balanceCoins', 0))
        print('Монет: ', info_money)
        return info_money
    return 0

if __name__ == '__main__':
    get_info_profile()
    get_info_money()
