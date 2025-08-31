import time
import httpx
from app.config import API_BASE_URL


# Кэш для хранения последних цен криптовалют
PRICE_CACHE = {}

# Время жизни кэша в секундах
CACHE_TTL = 30


async def get_crypto_price(crypto_id: str):

    now = time.time()

    # Возвращаем кэшированное значение, если оно ещё актуально
    if crypto_id in PRICE_CACHE:
        cached = PRICE_CACHE[crypto_id]
        if now - cached["time"] < CACHE_TTL:
            return cached["price"]

    url = f"{API_BASE_URL}/simple/price"
    params = {
        "ids": crypto_id,
        "vs_currencies": "usd"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            price = data[crypto_id]["usd"]

            # Обновляем кэш
            PRICE_CACHE[crypto_id] = {"price": price, "time": now}
            
            return price
        
        # Ошибка при запросе или неверный формат ответа
        except (httpx.RequestError, httpx.HTTPStatusError, KeyError):
            return None