import os
import sys
import pty
import time
import errno
import signal
import select

from datetime import datetime, timedelta

from stve.exception import *

def run_bg(cmd, debug=False, cwd=''):
    if type(cmd) in [str, unicode]:
        cmd = [c for c in cmd.split() if c != '']
    if debug:
        sys.stderr.write(''.join(cmd) + '\n')
        sys.stderr.flush()

    try:
        ( child_pid, child_fd ) = pty.fork()
    except OSError as e:
        raise RunError(cmd, None, message='pty.fork() failed: %s' % str(e))
    if child_pid == 0:
        try:
            if cwd != '':
                os.chdir(cwd)
            os.execvp(cmd[0], cmd)
        except Exception as e:
            raise RunError(cmd, None, message='os.execvp() failed: %s' % str(e))
    else:
        return child_pid, child_fd

def run(cmd, timeout, debug=False, cwd='', output_file=None):
    if type(cmd) in [str, unicode]:
        cmd = [c for c in cmd.split() if c != '']
    if debug:
        sys.stderr.write(''.join(cmd) + '\n')
        sys.stderr.flush()
    if output_file and type(output_file) is not file:
        raise OSError('Parameter "output_file" must be type file')

    out = ''
    try:
        ( child_pid, fd ) = pty.fork()
    except OSError as e:
        raise RunError(cmd, None, message='pty.fork() failed: %s' % str(e))
    if child_pid == 0:
        try:
            if cwd != '':
                os.chdir(cwd)
            os.execvp(cmd[0], cmd)
        except Exception as e:
            raise RunError(cmd, None, message='os.execvp() failed: %s' % str(e))
    else:
        if time > 0:
            limit = datetime.now() + timedelta(seconds=timeout)
        else:
            limit = None
        p = select.poll()
        mask = (
            select.POLLERR | select.POLLHUP | select.POLLNVAL | select.POLLIN | select. POLLPRI
        )
        p.register(fd, mask)
        stop = False
        try:
            while (not stop):
                if limit and datetime.now() > limit:
                    raise TimeoutError({
                        'cmd'       : cmd,
                        'out'       : out,
                        'message'   : 'command time out'
                    })
                try:
                    events = p.poll(100) #ms
                except select.error as e:
                    if e[0] == errno.EINTR:
                        continue
                for efd, flags in events:
                    if debug:
                        sys.stderr.write('flags: 0x%02x\n' % flags)
                        sys.stderr.flush()

                    if (flags & select.POLLIN or flags & select.POLLPRI):
                        tmp = os.read(efd, 4096)
                        if debug:
                            sys.stderr.write('read %d\n' % len(tmp))
                            sys.stderr.write(tmp)
                            sys.stderr.write('\n')
                            sys.stderr.flush()
                        out += tmp
                        if output_file:
                            output_file.write(tmp)
                    elif (flags & select.POLERR or flags & select.POLLHUP or flags & select.POLLNVAL):
                        stop = True

        except Exception as e:
            os.kill(child_pid, signal.SIGKILL)
            os.waitpid(child_pid, 0)
            os.close(fd)
            raise e

        s = os.waitpid(child_pid, 0)
        result = s[1]
        if result >> 15 == 1:
            a = 256 - (result >> 8)
            a *= -1
        else:
            a = result >> 8
        os.close(fd)
        return (a, out, '')

run('sleep 10', timeout=5)
