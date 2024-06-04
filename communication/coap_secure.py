import asyncio
from aiocoap import *
from utils.logger import log

async def coap_request():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coaps://coap.example.com/secure-resource')

    try:
        response = await protocol.request(request).response
        log(f'Result: {response.code}\n{response.payload}')
    except Exception as e:
        log('Failed to fetch resource:')
        log(e)

if __name__ == "__main__":
    asyncio.run(coap_request())
