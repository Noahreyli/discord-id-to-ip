import aiohttp
import asyncio

async def get_ip_address_from_discord_id(discord_id: str) -> str:
    """
    DiscordのユーザーIDに関連付けられたIPアドレスを取得する機能

    パラメータ:
    - discord_id: str
        IP アドレスを取得する Discord ユーザー ID

    戻り値:
    - str
        提供された Discord ユーザー ID に関連付けられた IP アドレス

    発生するもの:
    - 値エラー:
        Discord ID が無効であるか見つからない場合は、エラーが発生します
    """
    
    # ユーザーデータを取得するための Discord API エンドポイント
    url = f"https://discord.com/api/v9/users/{discord_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                user_data = await response.json()
                ip_address = user_data.get('ip', 'IP Address not found')
                return ip_address
            else:
                raise ValueError(f"Failed to retrieve IP address. Status code: {response.status}")

async def main():
    discord_id = input("Enter Discord User ID: ")
    try:
        ip_address = await get_ip_address_from_discord_id(discord_id)
        print(f"The IP address associated with Discord ID {discord_id} is: {ip_address}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
