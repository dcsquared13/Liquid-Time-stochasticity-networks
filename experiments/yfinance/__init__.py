from . import version
from .ticker import Ticker
from .tickers import Tickers
from .multi import download
from .utils import set_tz_cache_location, enable_debug_mode

__version__ = version.version
__author__ = "Ran Aroussi"


def pdr_override():
    """
    make pandas datareader optional
    otherwise can be called via fix_yahoo_finance.download(...)
    """
    try:
        import pandas_datareader
        pandas_datareader.data.get_data_yahoo = download
        pandas_datareader.data.get_data_yahoo_actions = download
        pandas_datareader.data.DataReader = download
    except Exception:
        pass


__all__ = ['download', 'Ticker', 'Tickers', 'pdr_override', 'enable_debug_mode', 'set_tz_cache_location']