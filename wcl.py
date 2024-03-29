import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def header(link):
    """
    header uses cookies to bypass login for web scrape
    :param report: the link (tmb)
    :return: the response
    """ 
    res = requests.get(link, cookies={os.getenv("tmb_key"):os.getenv("tmb_val")})
    if res.status_code == 200:
        return res
    else:
        return 3

tokenURL = "https://www.warcraftlogs.com/oauth/token"
publicURL = "https://classic.warcraftlogs.com/api/v2/client"

def access_token():
    """
    access_token() gets the access token
    :return: the access token
    """ 
    data={"grant_type":"client_credentials"}
    auth = os.getenv("client_id"), os.getenv("client_secret")
    with requests.Session() as session:
        response = session.post(tokenURL, data = data, auth = auth)
    return response.json().get("access_token")

accessToken = access_token()

def retrieve_headers() -> dict[str, str]:
    """
    retrieve_headers() gets the headers
    :return: the headers
    """ 
    return {"Authorization": f"Bearer {accessToken}"}

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
    try:
        response = get_data(reportQuery, **kwargs)['data']['reportData']['report']['masterData']
    except:
        return 0
    names = []
    for name in response['actors']:
        names.append(name['name'])
    return names

charQuery = """query($name:String) {
                characterData{
                    character(name:$name, serverSlug: "Mankrik", serverRegion: "US") {
                        zoneRankings(zoneID:1018)
                    }
                }
            }"""

shadowQuery = """query($name:String) {
                characterData{
                    character(name:$name, serverSlug: "Mankrik", serverRegion: "US") {
                        zoneRankings(zoneID:1017, metric:dps)
                    }
                }
            }"""

def get_perf(**kwargs):
    """
    get_perf gets raider's performance
    :param name: the name of the raider
    :return: the best and median performance of the raider
    """ 
    try:
        response = get_data(charQuery, **kwargs)['data']['characterData']['character']['zoneRankings']
    except:
        return 1
    
    spec = response['allStars'][0]['spec']
    if spec == 'Shadow':
        response = get_data(shadowQuery, **kwargs)['data']['characterData']['character']['zoneRankings']

    if spec == 'Fury' or spec == 'Arms':
        spec = 'Warrior'
    elif spec == 'Survival' or spec == 'Marksmanship':
        spec = 'Hunter'
    elif spec == 'Arcane' or spec == 'Fire':
        spec = 'Mage'
    elif spec == 'Protection':
        spec = 'Paladin'

    wcl = {'Best':response['bestPerformanceAverage'], 'Med':response['medianPerformanceAverage'], 'Spec':spec}
    return wcl

recentQuery = """query($guildID:Int){
                reportData{
                    reports(guildID: $guildID, zoneID: 1018, limit: 10){
                        data {
                            code
                            startTime
                            fights (killType: Kills){
                                size
                            }
                        }
                    }
                }
            }"""

def get_recentReport(**kwargs):
    """
    get_recentReport gets the 10 most recent reports from guild ID
    :param name: the guild ID
    :return: the most recent 25M report
    """ 
    try:
        response = get_data(recentQuery, **kwargs)['data']['reportData']['reports']['data']
    except:
        return 0
    for code in response:
        if code['fights'][0]['size'] == 25:
            date = datetime.fromtimestamp(code['startTime']/1000)
            if (datetime.now() - date).days > 14:
                break
            return code['code']
    return 4