import sys,os
import time
from daemon import Daemon
from logger import init_logger
from connector import scarpy
import logging
import threading

class Rssbug(Daemon):
    logger = logging.getLogger("ptfd_rss_service")
    def run(self):
        """The Real Worker
        """
        while True:
            try:
                t = threading.Thread(target=scarpy,args=(False,))
                t.setDaemon(True)
                t.start()
            except:
                logger.warning("Main Loop Error!")
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
