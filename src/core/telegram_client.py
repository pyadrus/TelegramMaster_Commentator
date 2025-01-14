from telethon.sync import TelegramClient


async def connect_telegram_account(api_id, api_hash) -> TelegramClient:
    """
    Подключается к Telegram аккаунту используя api_id и api_hash.

    :param api_id: Идентификатор API Telegram.
    :param api_hash: Ключ API Telegram.
    :return: TelegramClient объект, подключенный к Telegram.
    """
    client = TelegramClient('user_data/accounts/session_name', api_id, api_hash)
    await client.connect()
    return client
