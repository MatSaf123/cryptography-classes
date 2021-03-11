import hashlib as hl
import logging
import timeit

logger = logging.getLogger('hashing')
logging.basicConfig(level=logging.DEBUG)

def hash_with_all(str_in: str, display = True) -> dict:

    d_out = {}

    for fun in hl.algorithms_available:

        out = hl.new(fun, str_in.encode("UTF-8"))
        t = timeit.timeit('lambda: hl.new(fun, str_in.encode("UTF-8"))')
        h = None
        if(fun.startswith('shake')):
            h = str(out.hexdigest(16))
        else:
            h = str(out.hexdigest())
        if display:
            logger.info(fun+'(): '+h+' , (t = '+str(t)+')')
        d_out[fun] = h

    return d_out

def hash_from_file(file_path: str, display = True) -> str:

    try:
        with open(file_path, 'rb') as file:
            out = hl.sha256()
            while True:
                chunk = file.read(out.block_size)
                if not chunk:
                    break
                out.update(chunk)
            if display:
                logger.info(out.hexdigest())
        return out.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError('There is no file within given path')

#hash_with_all('helloworld')