import logging
import logging.handlers

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

class JsonFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super(JsonFormatter, self).formatException(exc_info)
        json_result = {
        "timestamp": f"{datetime.now()}",
        "level": "ERROR",
        "logger": "app",
        "message": f"{result}"
        }
        return json.dumps(json_result)

json_handler = logging.handlers.TimedRotatingFileHandler(
    filename=f"server/knesis.log",
    interval=12,
    when="H",
    backupCount=1,
)

json_formatter = JsonFormatter(
'{"timestamp":"%(asctime)s", "level":"%(levelname)s", "logger":"%(module)s", "message":"%(message)s"}'
)

json_handler.setFormatter(json_formatter)
logger.addHandler(json_handler)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter(
"[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

logger.error('테스트용 error 메세지 입니다')

json_handler.close()
