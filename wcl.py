import requests
from client import clientID
from client import clientSecret

tokenURL = "https://www.warcraftlogs.com/oauth/token"
publicURL = "https://www.warcraftlogs.com/api/v2/client"

def access_token():
    data={"grant_type":"client_credentials"}
    auth = clientID(), clientSecret()
    with requests.Session() as session:
        response = session.post(tokenURL, data = data, auth = auth)
    return response.json().get("access_token")

def retrieve_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {access_token()}"}

query = """query($code:String){
            reportData{
                report(code:$code){
                    masterData(translate: true) {
                        actors(type: "Player") {
                        name
                        id
                        }
                    }
                    fights(killType: Encounters) {
                        friendlyPlayers
                    }
                }
            }
        }"""

def get_data(query:str, **kwargs):
    data = {"query":query, "variables": kwargs}
    with requests.Session() as session:
        session.headers = retrieve_headers()
        response = session.get(publicURL, json=data)
        return response.json()


def get_names(**kwargs):
    response = get_data(query, **kwargs)['data']['reportData']['report']['masterData']
    names = []
    for name in response['actors']:
        names.append(name['name'])
    return names