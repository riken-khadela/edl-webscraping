import asyncio
import websockets
import json, datetime
from bot import Bot

# Initialize bot

connected = set()
bot_ = Bot()
bot_.get_local_driver()
bot_.work()

async def echo(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                await conn.send(json.dumps({"data": "websocket has been connected !"}))
                await websocket.send(f"Echo: {message}")
                try:
                    main_data = await bot_.return_main_data_for_all_windows_parallel()
                except Exception as e : websocket.send(f"error: {message}")
                await conn.send(json.dumps({"data": main_data}))
                print(f'\n\n\n Dattime : {datetime.datetime.now()}')
            await websocket.send(f"Echo: {message}")
    finally:
        connected.remove(websocket)

start_server = websockets.serve(echo, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
