import logging
import os
import logging.config
import yaml

log = logging.getLogger(__name__)


def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def validate_token(token):
    log.debug('Validating token {}'.format(token))
    if len(token) == 64:
        return True
    return False
