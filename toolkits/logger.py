# -*- coding: utf-8 -*-
# Time   : 2019/11/20 3:00 下午
# Author : Eylaine
# File   : logger.py

import logging
import logging.config
from functools import wraps

from logs import LOG_PATH


def log_config():

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"handlers": ["common", "console"], "level": "INFO", "propagate": False},
        "formatters": {
            "common": {
                "format": "[%(levelname)s] %(filename)s: %(lineno)d - %(message)s"
            },
            "complex": {
                "format": "[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)d - %(message)s"
            },
            "standard": {
                "format": "%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(module)s:%(funcName)s:%(lineno)d ]"
                          "[%(levelname)s]- %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "level": "INFO"
            },
            "common": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "complex",
                "level": "INFO",
                "filename": f"{LOG_PATH}/common.log",
                "mode": "w+",
                "encoding": "utf8"
            }
        },
        "loggers": {
            "common": {
                "handlers": ["common", "console"],
                "level": "INFO",
                "propagate": False
            }
        }
    }

    logging.config.dictConfig(config)


def get_logger(name="common"):
    log_config()
    return logging.getLogger(name)


logger = get_logger()


def record_log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(func.__doc__)
        return func(*args, **kwargs)

    return wrapper
