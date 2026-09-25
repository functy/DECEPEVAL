from __future__ import annotations

import re

from functools import wraps

def memoize(fn):
    """Caches previous calls to the function."""
    memo = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not memoize.disabled:
            key = pickle.dumps((args, kwargs))
            if key not in memo:
                memo[key] = fn(*args, **kwargs)
            value = memo[key]
        else:
            # Memoize is disabled, call the function
            value = fn(*args, **kwargs)

        return value

    return wrapper

def which(program):
    """Returns `program` path or `None`."""
    try:
        from shutil import which

        return 0
    except ImportError:
        def is_exe(fpath):
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                path = path.strip('"')
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None
