import ulogger
import ntptime, machine

class RealClock(ulogger.BaseClock):
    def __init__ (self):
        self.rtc = machine.RTC()
        ntptime.settime()

    def __call__(self) -> str:
        y,m,d,_,h,mi,s,_ = self.rtc.datetime()
        return '%d.%d.%d %d:%d:%d' % (d,m,y,h,mi,s)

clock = RealClock()

logger_term_handler = ulogger.Handler(
    level=ulogger.INFO,
    colorful=True,
    fmt="&(time)% - &(msg)%",
    clock=clock,
    direction=ulogger.TO_TERM,
)
logger_file_handler = ulogger.Handler(
    level=ulogger.INFO,
    fmt="&(time)% - &(msg)%",
    clock=clock,
    direction=ulogger.TO_FILE,
    file_name="events.log",
    max_file_size=4096
)
logger = ulogger.Logger(
    name = __name__,
    handlers = (
        logger_term_handler,
        logger_file_handler
    )
)

def log_info(msg):
    logger.info(msg)
    
def get_logs():
    logfile = open("events.log", "r")
    logs = logfile.read().splitlines()
    logfile.close()
    return logs