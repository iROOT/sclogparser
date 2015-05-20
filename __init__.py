import parselog
import utils
import logging
logging.basicConfig(format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)

if __name__ == "__main__":
    log = parselog.ParseLog(utils.get_last_directory())
    log.print_log_merged()
