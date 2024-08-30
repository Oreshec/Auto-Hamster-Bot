import requests
import conf

def get_info_profile():
    url = "https://api.hamsterkombatgame.io/auth/account-info"

    payload = ""
    headers = {
        "Authorization": f"{conf.authorization}"}

    response = requests.request("POST", url, data=payload, headers=headers)
    data = response.json()
    profile_name = data['accountInfo']['name']
    print(data)
    return profile_name

def get_info_money():
    url = "https://api.hamsterkombatgame.io/clicker/sync"

    payload = ""
    headers = {
        "Authorization": f"{conf.authorization}",
        "Priority": "u=4"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    data = response.json()
    info_money = data['clickerUser']['balanceCoins']
    print(info_money)
    return info_money

if __name__ == '__main__':
    get_info_profile()
    get_info_money()