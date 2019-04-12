import asyncio
import aiohttp
import datetime


#Receiving the agent_id  and system_id to be queried in the database
id = int(input("Enter agent id: "))
sys_id = input("Enter system id: ")
d = {'agent_id': id, 'system_id' : sys_id}

#fetch_info function initialises a session with the localhost and sends the user input above as a post request
async def fetch_info():
     async with aiohttp.ClientSession() as session:
         async with session.post('http://localhost:8080/', json = d) as resp:
             print(await resp.text())

asyncio.run(fetch_info())
