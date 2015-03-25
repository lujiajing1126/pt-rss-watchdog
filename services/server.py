import sys,os
import time
from daemon import Daemon
from logger import init_logger
from connector import scarpy
import logging
import threading

class Rssbug(Daemon):
    def run(self):
        """The Real Daemon Worker
        """
        self.logger_ins = logging.getLogger("ptfd_rss_service")
        self.isFirstTime = True
        while True:
            try:
                t = threading.Thread(target=scarpy,args=(self.isFirstTime,))
                t.setDaemon(True)
                t.start()
            except:
                self.logger_ins.warning("Main Loop Error!")
            self.isFirstTime = False
            time.sleep(300)

if __name__ == "__main__":
    init_logger()
    daemon = Rssbug("/tmp/pt_updater.pid")
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print 'Unknown Command'
            sys.exit(2)
    else:
        print 'usage: %s start|stop|restart' % sys.argv[0]
        sys.exit(2)
