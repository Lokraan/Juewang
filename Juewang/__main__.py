
from . import config


logging.getLogger("discord.http").setLevel(logging.WARNING)
logging.getLogger("discord").setLevel(logging.INFO)

logger = logging.getLogger()

level = logging.DEBUG if config.debug else logging.INFO

f_handler = logging.FileHandler(filename="juewang.log", encoding="utf-8", mode="w")
cl_handler = logging.StreamHandler()

dt_fmt = "%Y-%m-%d %H:%M:%S"
out_fmt = "[{asctime}] [{levelname:<6}] {name}: {message}"
logger_fmt = logging.Formatter(out_fmt, dt_fmt, style="{")

cl_handler.setFormatter(logger_fmt)
f_handler.setFormatter(logger_fmt)

logger.addHandler(cl_handler)
logger.addHandler(f_handler)
logger.setLevel(level)

try:
  if not config.token:
    sys.exit("Discord token must be supplied in configuration.")
except:
  sys.exit("Discord token must be supplied in configuration.")

elif sys.version_info < (3, 6):
  sys.exit("Python 3.6 or higher to run. This is version {0}.".format(
    ".".join(sys.version_info[:3])))


from .bot import Juewang
Juewang().run()
