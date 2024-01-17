# 显示操作日志
from loguru import logger
logger.add("log/debug/log_debug_{time}.log",
    level='DEBUG',
    format='{time:YYYY-MM-DD HH:mm:ss} - {level} - {file} - {line}\n{message}\n',
    # rotation="500MB",
    # compression="zip",
    # retention="10 days",
    # enqueue=True,
    encoding="utf-8")
logger.add("log/info/log_info_{time}.log",
    level='INFO',
    format='{time:YYYY-MM-DD HH:mm:ss} - {level} - {file} - {line}\n{message}\n',
    # rotation="500MB",
    # compression="zip",
    # retention="10 days",
    # enqueue=True,
    encoding="utf-8")
logger.add("log/warning/log_warning_{time}.log",
    level='WARNING',
    format='{time:YYYY-MM-DD HH:mm:ss} - {level} - {file} - {line}\n{message}\n',
    # rotation="500MB",
    # compression="zip",
    # retention="10 days",
    # enqueue=True,
    encoding="utf-8")
# logger.debug(f"")
# logger.info(f"")
# logger.warning(f"")
# logger.error(f"")
# logger.critical(f"")
# @logger.catch

