import requests
import json

from .league_client import LeagueClient


class LCUCall:
    _league_client = None
    _url = None
    _headers = None

    def __init__(self, league_client: LeagueClient) -> None:
        self._league_client = league_client
        self._url = f'https://127.0.0.1:{self._league_client.get_lcu_port()}'
        self.set_headers()

    def set_headers(self) -> None:
        '''
        Set headers for requests.
        '''
        self._headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic ' + self._league_client.get_lcu_session_token()
        }

    def get(self, path: str) -> str:
        r = requests.get(f'{self._url}{path}',
                         headers=self._headers, verify=False)
        return json.loads(r.text)

    def post(self, path: str, data: str) -> str:
        r = requests.post(f'{self._url}{path}',
                          headers=self._headers, data=data, verify=False)
        return json.loads(r.text)

    def put(self, path: str, data: str) -> str:
        r = requests.put(f'{self._url}{path}',
                         headers=self._headers, data=data, verify=False)
        return json.loads(r.text)

    def delete(self, path: str) -> str:
        r = requests.delete(f'{self._url}{path}',
                            headers=self._headers, verify=False)
        return json.loads(r.text)

    def get_current_summoner(self) -> str:
        '''
        Get current summoner information.
        '''
        return self.get(f'/lol-summoner/v1/current-summoner')

    def get_summoner_by_name(self, summoner_name: str) -> str:
        '''
        Get summoner information by summoner name.
        '''
        return self.get(f'/lol-summoner/v1/summoners?name={requests.utils.quote(summoner_name)}')

    def send_report(self, data) -> str:
        '''
        Send report to summoner.
        '''
        return self.post(f'/lol-end-of-game/v2/player-complaints', data=data)