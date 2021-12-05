import logging
from contextlib import contextmanager
from time import perf_counter
import sys
FORMAT = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
log = logging.getLogger(__name__)

@contextmanager
def EEL(methodDescr, raiseExcp=False):
    '''EEL = Entry Exit Log'''
    log.debug(f"About to run {methodDescr}")
    start = perf_counter()
    try:
        yield
    except Exception as ex:
       
       print( ex)
    finally:
        end = perf_counter()
        time_taken = "{:.3g}".format(end - start)
        log.debug(f"Done running {methodDescr} ({time_taken}s)")