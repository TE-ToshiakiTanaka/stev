import os
import sys
import time
import errno
import threading
import subprocess

from stve.exception import *

class ThreadWithReturn(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ThreadWithReturn, self).__init__(*args, **kwargs)
        self._return = None

    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)

    def join(self, timeout=None):
        super(ThreadWithReturn, self).join(timeout=timeout)
        return self._return

def run_bg(cmd, cwd=None, debug=False):
    if type(cmd) in [str, unicode]:
        cmd = [c for c in cmd.split() if c != '']
    if debug:
        sys.stderr.write(''.join(cmd) + '\n')
        sys.stderr.flush()

    try:
        proc = subprocess.Popen(cmd,
                                cwd     = cwd,
                                stdout  = subprocess.PIPE,
                                stderr  = subprocess.PIPE)
        proc_thread = ThreadWithReturn(target=proc.communicate)
        proc_thread.daemon = True
        proc_thread.start()
    except OSError as e:
        raise RunError(cmd, None, message='Raise Exception : %s' % str(e))
    returncode = proc.returncode
    return (returncode)

def run(cmd, cwd=None, timeout=60, debug=False):
    if type(cmd) in [str, unicode]:
        cmd = [c for c in cmd.split() if c != '']
    if debug:
        sys.stderr.write(''.join(cmd) + '\n')
        sys.stderr.flush()

    try:
        proc = subprocess.Popen(cmd,
                                cwd     = cwd,
                                stdout  = subprocess.PIPE,
                                stderr  = subprocess.PIPE)
        proc_thread = ThreadWithReturn(target=proc.communicate)
        proc_thread.start()
        result = proc_thread.join(timeout)
        if proc_thread.is_alive():
            try:
                proc.kill()
            except OSError as e:
                out = "{}: {}\n{}".format(type(e).__name__, e, traceback.format_exc())
                raise RunError(cmd, None, message='Raise Exception : %s' % out)
            raise TimeoutError({
                'cmd'       : cmd,
                'out'       : None,
                'message'   : 'command %s is time out' % cmd
            })
        returncode = proc.returncode
        if result == None:
            out = None; err = None;
        else:
            out = result[0]; err = result[1]

    except WindowsError as e:
        out = "{}: {}\n{}".format(type(e).__name__, e, traceback.format_exc())
        raise RunError(cmd, None, message='Raise Exception : %s' % out)

    except RuntimeError as e:
        out = "{}: {}\n{}".format(type(e).__name__, e, traceback.format_exc())
        raise RunError(cmd, None, message='Raise Exception : %s' % out)
    try:
        if isinstance(out, bytes): out = out.decode("utf8")
        if isinstance(err, bytes): err = err.decode("utf8")
    except UnicodeDecodeError as e:
        out = "{}: {}\n{}".format(type(e).__name__, e, traceback.format_exc())
        print out
    return (returncode, out, err)
