import aiohttp
import asyncio
import conf
import traceback

async def make_request(url, headers, payload=None):
    """Helper function to make asynchronous API requests and handle errors."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload, headers=headers) as response:
                print(f'Отправка запроса на {url}')
                print('Status: ', response.status)
                response.raise_for_status()  # Will raise an HTTPError for bad responses
                return await response.json()
    except aiohttp.ClientError as e:
        print(f'Ошибка при запросе {url}:\n', e)
        return None
    except Exception:
        print('Ошибка:\n', traceback.format_exc())
        return None

async def get_info_profile():
    url = "https://api.hamsterkombatgame.io/auth/account-info"
    headers = {"Authorization": f"{conf.authorization}"}
    data = await make_request(url, headers)
    if data:
        profile_name = data.get('accountInfo', {}).get('name', 'Unknown')
        print('Имя профиля:', profile_name)
        return profile_name
    return 'Unknown'

async def get_info_diamond():
    url = "https://api.hamsterkombatgame.io/interlude/sync"
    headers = {
        "Authorization": f"{conf.authorization}",
        "Priority": "u=4"
    }
    data = await make_request(url, headers)
    if data:
        info_diamond = float(data.get('clickerUser', {}).get('balanceDiamonds', 0))
        return info_diamond
    return 0

# Example of how to call the functions asynchronously
# asyncio.run(get_info_profile())
# asyncio.run(get_info_money())
