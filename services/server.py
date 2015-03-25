import sys,os
import time

class Daemon:
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
    def _daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                os.exit(0)
        except OSError,e:
            sys.stderr.write('fork #1 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)
        os.chdir("/")
        os.setsid()
        os.umask(0)
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError,e:
            sys.stderr.write('fork #2 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)

    def start(self):
        self._daemonize()
        self._run()
    def stop(self):

    def restart(self):
        self.stop()
        self.start()
    def _run(self):
        """The Real Worker
        """
        while True:
            time.sleep(300)
if __name__ == "__main__":
    daemon = Daemon("/tmp/pt_updater.pid")
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        else:
            print 'Unknown Command'
            sys.exit(2)
    else:
        print 'usage: %s start|stop|restart' % sys.argv[0]
        sys.exit(2)
