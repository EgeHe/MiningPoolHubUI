import utils
import logging
import requests

log = logging.getLogger(__name__)

COINS = ['zcash',
         'musicoin']

class DataGetter:
    def __init__(self):
        self.token = None
        self.initialized = False
        self.url_template = 'https://{:s}.miningpoolhub.com/index.php?page=api&action={:s}&api_key={:s}'
        self._coin = None

    @property
    def coin(self):
        return self._coin

    @coin.setter
    def coin(self, value):
        if value in COINS:
            self._coin = str(value)
        else:
            raise ValueError('Coin {} not available'.format(value))

    def init(self):
        token_ok = self.read_token()
        self.coin = 'zcash'
        coin_ok = True

        if token_ok and coin_ok:
            self.initialized = True
            log.info('Initialized!')

    def get_userhashrate(self):
        data = self.get_json_from_action(action='getuserhashrate')
        log.debug(data)
        log.info('Hashrate is: {}'.format(data['getuserhashrate']['data']))

    def get_miningandprofitsstatistics(self):
        data = self.get_json_from_action(action='getminingandprofitsstatistics')
        log.debug(data)

    def get_blockcount(self):
        data = self.get_json_from_action(action='getblockcount')
        log.debug(data)


    def get_json_from_action(self, action, **kwargs):
        url = self.construct_url(action, **kwargs)
        data = self.get_json_from_url(url)
        return data

    def construct_url(self, action, **kwargs):
        url = self.url_template.format(self.coin, action, self.token)
        for key in kwargs.keys():
            url += '&{}={}'.format(key, kwargs[key])
        return url

    def get_json_from_url(self, url):
        log.debug('Requesting url {}'.format(url))
        r = requests.get(url)
        return r.json()

    def read_token(self):
        with open('token.txt', 'r') as f:
            token = f.readline().strip()
        if utils.validate_token(token):
            self.token = token
            return True
        else:
            return False
