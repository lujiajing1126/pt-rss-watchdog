import logging

def init_logger():
	logger = logging.getLogger("ptfd_rss_service")
	logger.setLevel(logging.DEBUG)
	fh = logging.FileHandler("service.log")
	fh.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
	fh.setFormatter(formatter)
	logger.addHandler(fh)