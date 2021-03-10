import hashlib as hl
import logging
from timeit import default_timer as timer

logger = logging.getLogger('hashing')
logging.basicConfig(level=logging.DEBUG)

def hash_with_all(str_in: str) -> list:

    l_out = []

    for fun in hl.algorithms_available:
        out = hl.new(fun)
        start = timer()
        out.update(str_in.encode())
        end = timer()
        h = None
        if(fun.startswith('shake')):
            h = str(out.hexdigest(16))
        else:
            h = str(out.hexdigest())
        logger.info(fun+'(): '+h+' , (t = '+str(end-start)+')')
        l_out.append(out)

    return l_out

#hash_with_all('testing321')