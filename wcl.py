import requests
from client import clientID
from client import clientSecret

tokenURL = "https://www.warcraftlogs.com/oauth/token"
publicURL = "https://classic.warcraftlogs.com/api/v2/client"

def access_token():
    """
    access_token() gets the access token
    :return: the access token
    """ 
    data={"grant_type":"client_credentials"}
    auth = clientID(), clientSecret()
    with requests.Session() as session:
        response = session.post(tokenURL, data = data, auth = auth)
    return response.json().get("access_token")

def retrieve_headers() -> dict[str, str]:
    """
    retrieve_headers() gets the headers
    :return: the headers
    """ 
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
    """
    get_data gets details about a WCL report
    :param report: the report code
    :return: all info about the report
    """ 
    data = {"query":query, "variables": kwargs}
    with requests.Session() as session:
        session.headers = retrieve_headers()
        response = session.get(publicURL, json=data)
        return response.json()


def get_names(**kwargs):
    """
    get_names gets all names from a WCL report
    :param report: the report code
    :return: all names in the WCL report
    """ 
    response = get_data(reportQuery, **kwargs)['data']['reportData']['report']['masterData']
    names = []
    for name in response['actors']:
        names.append(name['name'])
    return names

charQuery = """query($name:String) {
                characterData{
                    character(name:$name, serverSlug: "Mankrik", serverRegion: "US") {
                        zoneRankings(zoneID:1017)
                    }
                }
            }"""

def get_perf(**kwargs):
    """
    get_perf gets raider's performance. Currently set to Ulduar (P2) performance
    :param name: the name of the raider
    :return: the best and median performance of the raider
    """ 
    response = get_data(charQuery, **kwargs)['data']['characterData']['character']['zoneRankings']
    perfs = {'Best':response['bestPerformanceAverage'], 'Med':response['medianPerformanceAverage']}
    return perfs

shadowQuery = """query($name:String) {
                characterData{
                    character(name:$name, serverSlug: "Mankrik", serverRegion: "US") {
                        zoneRankings(zoneID:1017, metric:dps)
                    }
                }
            }"""

def get_perf_shadow(**kwargs):
    """
    get_perf_shadow gets specifically shadow spec's performance due to incorrect quries for metric (hps)
    :param name: the name of the raider
    :return: the best and median performance of the raider
    """ 
    response = get_data(shadowQuery, **kwargs)['data']['characterData']['character']['zoneRankings']
    perfs = {'Best':response['bestPerformanceAverage'], 'Med':response['medianPerformanceAverage']}
    return perfs

def get_spec(**kwargs):
    """
    get_spec gets the specialization of the raider
    :param name: the name of the raider
    :return: the spec of the raider
    """ 
    response = get_data(charQuery, **kwargs)['data']['characterData']['character']['zoneRankings']
    spec = response['allStars'][0]['spec']
    if spec == 'Fury' or spec == 'Arms':
        spec = 'Warrior'
    elif spec == 'Survival' or spec == 'Marksmanship':
        spec = 'Hunter'
    elif spec == 'Affliction' or spec == 'Demonology':
        spec = 'Warlock'
    elif spec == 'Arcane' or spec == 'Fire':
        spec = 'Mage'
    elif spec == 'Protection':
        spec = 'Paladin'
    return {'Spec':spec}
