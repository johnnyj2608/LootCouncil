import requests
from auth import clientID
from auth import clientSecret

tokenURL = "https://www.warcraftlogs.com/oauth/token"
publicURL = "https://classic.warcraftlogs.com/api/v2/client"

def access_token():
    data={"grant_type":"client_credentials"}
    auth = clientID(), clientSecret()
    with requests.Session() as session:
        response = session.post(tokenURL, data = data, auth = auth)
    return response.json().get("access_token")

def retrieve_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {access_token()}"}

reportQuery = """query($code:String){
                reportData{
                    report(code:$code){
                        masterData(translate: true) {
                            actors(type: "Player") {
                                name
                            }
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
    response = get_data(reportQuery, **kwargs)['data']['reportData']['report']['masterData']
    names = []
    for name in response['actors']:
        names.append(name['name'])
    return names

report_names = get_names(code='bPpcTmQrzGXdMxA6')

charQuery = """query($name:String, $byBracket:Boolean) {
                characterData{
                    character(name:$name, serverSlug: "Mankrik", serverRegion: "US") {
                        zoneRankings(zoneID:1017, byBracket:$byBracket)
                    }
                }
            }"""

def get_perf(**kwargs):
    response = get_data(charQuery, **kwargs)['data']['characterData']['character']['zoneRankings']
    perfs = {'Best':int(response['bestPerformanceAverage']), 'Med':int(response['medianPerformanceAverage'])}
    return perfs