import requests
import time
import conf


def upgrade_card(id_card=None, authorization=conf.authorization):
    url_buy = "https://api.hamsterkombatgame.io/clicker/buy-upgrade"
    timestamp = int(time.time())

    payload = {
        "upgradeId": f"{id_card}",
        "timestamp": timestamp
    }
    headers = {
        "Authorization": f"{authorization}"}
    response = requests.request("POST", url_buy, json=payload, headers=headers)

    print('Info buy card', response.text)


if __name__ == '__main__':
    upgrade_card()
