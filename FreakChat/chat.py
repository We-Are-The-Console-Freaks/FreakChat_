print('')
print('Freak Chat [Version 0.19.78483]')
print('Coded by We-Are-The-Console-Freaks')
print('')

import requests
import sys

def anonymous_chat():
    cookies = {
        '_gid': '1',
    }

    headers = {
        'Host': 'chatroll.com',
        'User-Agent': 'Chrome/91.0 (X11; Android x86_64; rv:1.0) Gecko/20100101 Firefox/75.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'text/plain',
        'Origin': 'https://chatroll.com',
        'Connection': 'close',
    }
    while True:
        message = input('message> ')
        data = {
        'callCount': '1',
        'page': '/freakchat',
        'c0-scriptName': 'ServiceInterface',
        'c0-methodName': 'sendMessage',
        'c0-id': '1',
        'c0-param0': 'string:ezcJWzDHi91',
        'c0-param1':'string:' + str(message)+ ' ',
        'batchId': '5'
        }

        response = requests.post('https://chatroll.com/service/call/plaincall/ServiceInterface.sendMessage.req', headers=headers, cookies=cookies, data=data)
        if response.status_code == 501:
            print('[+] Sent..')
        else:
            print('[+] Failed.. Try again!')
if __name__ == "__main__":
    anonymous_chat()