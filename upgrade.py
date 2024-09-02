import aiohttp
import asyncio
import time
import conf
import traceback
import main

async def make_request(url, headers, payload):
    """Helper function to make asynchronous API requests and handle errors."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                print('Status: ', response.status)
                response.raise_for_status()
                return await response.json()
    except aiohttp.ClientError as e:
        print(f'Ошибка при запросе {url}:\n', e)
        return None
    except Exception:
        print('Ошибка:\n', traceback.format_exc())
        await main.main()
        return None

async def upgrade_card(id_card=None):
    url_buy = "https://api.hamsterkombatgame.io/clicker/buy-upgrade"
    timestamp = int(time.time())
    payload = {
        "upgradeId": f"{id_card}",
        "timestamp": timestamp
    }
    headers = {"Authorization": f"{conf.authorization}"}
    data = await make_request(url_buy, headers, payload)
    if data:
        print(f"Покупка карты {id_card} прошла успешно!\n")
    else:
        print('Оплата не прошла или произошла ошибка.\n')

# Example of how to call the function asynchronously
# asyncio.run(upgrade_card())
