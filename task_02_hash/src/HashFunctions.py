import hashlib as hl
import logging
import timeit
import random
import string
import plotly.express as px


class Hashing:
    logger = logging.getLogger('hashing')
    logging.basicConfig(level=logging.DEBUG)

    @staticmethod
    def hash_with_all(str_in: str, display: bool = True) -> dict:

        """Returns and (optionally) displays hashing results and hashing times for all available hash algorithms."""

        d_out = {}

        for fun in hl.algorithms_available:

            out = hl.new(fun, str_in.encode("UTF-8"))
            t = timeit.timeit(lambda: hl.new(fun, str_in.encode("UTF-8")))

            if fun.startswith('shake'):
                h = str(out.hexdigest(20))
            else:
                h = str(out.hexdigest())
            if display:
                Hashing.logger.info(fun + '(): ' + h + ' , (t = ' + str(t) + ')')
            d_out[fun] = h

        return d_out

    @staticmethod
    def hash_from_file(file_path: str, display: bool = True) -> str:

        """Returns and (optionally) displays hash for a given file."""

        try:
            with open(file_path, 'rb') as file:
                out = hl.sha256()
                while True:
                    chunk = file.read(out.block_size)
                    if not chunk:
                        break
                    out.update(chunk)
                if display:
                    Hashing.logger.info(out.hexdigest())
            return out.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError('There is no file within given path')

    @staticmethod
    def present_hash_time_for_strings(r: int = 30, algorithm: str = 'md5'):

        """Displays hashing times for strings with various lengths on a plot.
        Can be provided with custom string-count and hash algorithm."""

        results = {
            'string_lengths': [],
            'hash_speed': []
        }

        assert (algorithm in hl.algorithms_available), 'There is no available hash algorithm as given in params'

        for i in range(1, r + 1):
            s = ''.join(random.choices(string.ascii_lowercase + string.digits, k=i))
            results['string_lengths'].append(i)
            results['hash_speed'].append(timeit.timeit(lambda: hl.new(algorithm, s.encode("UTF-8"))))
            print(i)

        fig = px.line(results, x='string_lengths', y='hash_speed')
        fig.show()