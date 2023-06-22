import requests

cookies = {
    '_pbjs_userid_consent_data': '3524755945110770',
    'na-unifiedid': '%7B%22TDID%22%3A%22cb5fceb2-1413-46f6-a00d-8655a477ce4c%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-04-30T20%3A46%3A34%22%7D',
    'raidGroupFilter': '',
    '_sharedid': '8431f58c-39cb-47cf-beff-e0a2ff1c5b60',
    'closedAddonPrompt': '1',
    '_gid': 'GA1.2.423834584.1687305555',
    'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6ImY3cTVNZzJEVEErRVFmbVBQa1hmZmc9PSIsInZhbHVlIjoiVUdjbUV2Q0tTTjlJcDdkSnFSREZFT0t0eU9MU0VQNmczZk9Ecm1hZmxQaWxvdWdxTDJld1BjR0ZGcVYreUw0TGwrN08xeEN6UDBmV0xMRk5zMUF6SzQ5S0hodG5Ybk5RcWlRQUVnZnRFMmxDYWxQbG1nRHRwb1AzTERFTVJNdkNpRlozZStkYzNyR3d4c2pZSG1HRkZ3PT0iLCJtYWMiOiIxMWM0ZjE3M2EwMWQzNmEyOGEzYmE2YzAyMTc2ZjNiNTI2M2ZiMmJjMTZmMzI1ZjYyYTUwZmRlNDU3MzM5YzVlIiwidGFnIjoiIn0%3D',
    'cto_bundle': 'RKlw0F83YjhQMEFJQXVxU1dSQ1N1MnBnc2RKQ2VUZDdJZjdpUEE4VjRrRWlQWGZ1M0ppcnolMkY0UGlXMG1TJTJCNnh6YVdtSENDWnJiS2VlNGtDVVRybkF3dGRaeUV3UmdoTGtTYm8xdHhkalc5NzNyZUljUU5Cd0o5ZkhNMW0lMkZGVmJqNW9hRUQ1R1FaWVhyOVplclk1YjRDJTJCQkJOZyUzRCUzRA',
    'cto_bidid': 'z80eh182V2Z5ejRzZTBod1ZiU1cza2VjdGY5SmJPaEZZVUZpJTJGMFdmejlvdjFFU0pVVk0lMkJ4NlZmelE5cTM1SEJvaVhSMm5yRmc3bHBBZXlNNSUyQk1xRXJzYUc5UnVPQVNIYyUyQlRLWE5PSFBpQ1hLc0Fyc3UxejJBOXolMkZLbGE5VXpwUWRabzI',
    'cto_bundle': 'Spvlel83YjhQMEFJQXVxU1dSQ1N1MnBnc2RFMjJtNUpGYXJKTmZYcVBxOTkwTzNDUGp6aTJST0Jra0RLdXpzRlJVdyUyQjEwOWQzejk4JTJGZ2xuRFBjSEVSZ1g4JTJGNndOJTJGZ2d6aUZQR1FqMWVGMXl5MzB4TkFsWUYxNzhXZ09lMEJKRkJ6bVdqN3VDdWJCcEhVaThtY2pzcnl1S1R4dyUzRCUzRA',
    'XSRF-TOKEN': 'eyJpdiI6InpiMU1iZjNPKzVyaVVLL1ZvcTJSYlE9PSIsInZhbHVlIjoiWGc2Mm0yS1hMOG5weWFxZUsySzZqblBJaHh2OFA5Y1phOFIyaWc2UjZhbWw1VnN0eXlTeXRWK0hSZENpMmtSUHBMQVdqL2JIaUpwOFo3QXA3ZTRRZnVEVU0yK0hKODEzbGRyaGcvQVdmaW11Zjd0OFhHaW04Y0FwamNPTnppM1QiLCJtYWMiOiI5NTBjMzFmZDllMDAxN2UwY2YzYjFmMTQ0NGU5OTY4Y2E1NGU2NzUzMGFiOGY1MzJjZDA0MzAzMDY3NDBmODEwIiwidGFnIjoiIn0%3D',
    'thats_my_bis_session': 'eyJpdiI6IkhBRmRTaU1lYkF2bnJpanFaQmFRcEE9PSIsInZhbHVlIjoiN1VoZDVEZUNkaXdqbnVXSnRHcExKVVZoU3poVS9xcXNLL3RKMzM0TEVOZitGODZGaGVxYU9SWTJmWEIyQ04yamNZU2RJbURqYmFycC9KbDhzU2E2Y3RyVTMxcEY2a3dxV0RYYVRDQkZPbGdQU2IxalRnOHNOc0dMcWFXU0JPVEEiLCJtYWMiOiI1MTBjOTNmZWFlMmM2ZDIyNjZjMmY1ZjQ2MjNmMWFkM2NlZWFhYjMzN2RlYTgxZTliNTE4ZWU2NzBkMzlkNjAyIiwidGFnIjoiIn0%3D',
    '_gat_gtag_UA_173732351_1': '1',
    '_ga_CJF7R0JQMV': 'GS1.1.1687467083.16.1.1687467234.59.0.0',
    '_ga': 'GA1.1.1613304969.1685479571',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_pbjs_userid_consent_data=3524755945110770; na-unifiedid=%7B%22TDID%22%3A%22cb5fceb2-1413-46f6-a00d-8655a477ce4c%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-04-30T20%3A46%3A34%22%7D; raidGroupFilter=; _sharedid=8431f58c-39cb-47cf-beff-e0a2ff1c5b60; closedAddonPrompt=1; _gid=GA1.2.423834584.1687305555; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImY3cTVNZzJEVEErRVFmbVBQa1hmZmc9PSIsInZhbHVlIjoiVUdjbUV2Q0tTTjlJcDdkSnFSREZFT0t0eU9MU0VQNmczZk9Ecm1hZmxQaWxvdWdxTDJld1BjR0ZGcVYreUw0TGwrN08xeEN6UDBmV0xMRk5zMUF6SzQ5S0hodG5Ybk5RcWlRQUVnZnRFMmxDYWxQbG1nRHRwb1AzTERFTVJNdkNpRlozZStkYzNyR3d4c2pZSG1HRkZ3PT0iLCJtYWMiOiIxMWM0ZjE3M2EwMWQzNmEyOGEzYmE2YzAyMTc2ZjNiNTI2M2ZiMmJjMTZmMzI1ZjYyYTUwZmRlNDU3MzM5YzVlIiwidGFnIjoiIn0%3D; cto_bundle=RKlw0F83YjhQMEFJQXVxU1dSQ1N1MnBnc2RKQ2VUZDdJZjdpUEE4VjRrRWlQWGZ1M0ppcnolMkY0UGlXMG1TJTJCNnh6YVdtSENDWnJiS2VlNGtDVVRybkF3dGRaeUV3UmdoTGtTYm8xdHhkalc5NzNyZUljUU5Cd0o5ZkhNMW0lMkZGVmJqNW9hRUQ1R1FaWVhyOVplclk1YjRDJTJCQkJOZyUzRCUzRA; cto_bidid=z80eh182V2Z5ejRzZTBod1ZiU1cza2VjdGY5SmJPaEZZVUZpJTJGMFdmejlvdjFFU0pVVk0lMkJ4NlZmelE5cTM1SEJvaVhSMm5yRmc3bHBBZXlNNSUyQk1xRXJzYUc5UnVPQVNIYyUyQlRLWE5PSFBpQ1hLc0Fyc3UxejJBOXolMkZLbGE5VXpwUWRabzI; cto_bundle=Spvlel83YjhQMEFJQXVxU1dSQ1N1MnBnc2RFMjJtNUpGYXJKTmZYcVBxOTkwTzNDUGp6aTJST0Jra0RLdXpzRlJVdyUyQjEwOWQzejk4JTJGZ2xuRFBjSEVSZ1g4JTJGNndOJTJGZ2d6aUZQR1FqMWVGMXl5MzB4TkFsWUYxNzhXZ09lMEJKRkJ6bVdqN3VDdWJCcEhVaThtY2pzcnl1S1R4dyUzRCUzRA; XSRF-TOKEN=eyJpdiI6InpiMU1iZjNPKzVyaVVLL1ZvcTJSYlE9PSIsInZhbHVlIjoiWGc2Mm0yS1hMOG5weWFxZUsySzZqblBJaHh2OFA5Y1phOFIyaWc2UjZhbWw1VnN0eXlTeXRWK0hSZENpMmtSUHBMQVdqL2JIaUpwOFo3QXA3ZTRRZnVEVU0yK0hKODEzbGRyaGcvQVdmaW11Zjd0OFhHaW04Y0FwamNPTnppM1QiLCJtYWMiOiI5NTBjMzFmZDllMDAxN2UwY2YzYjFmMTQ0NGU5OTY4Y2E1NGU2NzUzMGFiOGY1MzJjZDA0MzAzMDY3NDBmODEwIiwidGFnIjoiIn0%3D; thats_my_bis_session=eyJpdiI6IkhBRmRTaU1lYkF2bnJpanFaQmFRcEE9PSIsInZhbHVlIjoiN1VoZDVEZUNkaXdqbnVXSnRHcExKVVZoU3poVS9xcXNLL3RKMzM0TEVOZitGODZGaGVxYU9SWTJmWEIyQ04yamNZU2RJbURqYmFycC9KbDhzU2E2Y3RyVTMxcEY2a3dxV0RYYVRDQkZPbGdQU2IxalRnOHNOc0dMcWFXU0JPVEEiLCJtYWMiOiI1MTBjOTNmZWFlMmM2ZDIyNjZjMmY1ZjQ2MjNmMWFkM2NlZWFhYjMzN2RlYTgxZTliNTE4ZWU2NzBkMzlkNjAyIiwidGFnIjoiIn0%3D; _gat_gtag_UA_173732351_1=1; _ga_CJF7R0JQMV=GS1.1.1687467083.16.1.1687467234.59.0.0; _ga=GA1.1.1613304969.1685479571',
    'Referer': 'https://thatsmybis.com/15596/raid-team-two/roster',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

def curl(link):
    return requests.get(link, cookies=cookies, headers=headers)

def clientID():
    return '997960ef-8fca-4bbc-b714-d818115051a1'

def clientSecret():
    return 'DI7yZHGlUh6N8bnFBIV73z1dWBeTOJQJzdTAlFmm'

    # Get WCL API
    # Get report
    # Get names
    # Intersect with raider dict
    # Append max(median/bracket) performance (convert to 1-5)
    # Intersect raider dict with items dict
    # New dict to store item:name
    # Funciton to rerun ^ after +=1 received
    # Dockerize & Functions