import datagetter
import logging
import utils

utils.setup_logging()
log = logging.getLogger(__name__)


def main():
    dg = datagetter.DataGetter()
    dg.init()
    dg.coin = 'zcash'
    dg.get_userhashrate()
    dg.get_miningandprofitsstatistics()
    dg.get_blockcount()


if __name__ == '__main__':
    main()
