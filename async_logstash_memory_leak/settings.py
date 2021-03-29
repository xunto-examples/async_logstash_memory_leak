import os
from pathlib import Path

DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = ')pb@@6!hym0r4g!g3cb1ld6oz4_8zr1n=kq9j5j&_lmw7f)!3^'
ROOT_URLCONF = 'async_logstash_memory_leak.urls'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logstash': {
            '()': 'logstash_async.formatter.DjangoLogstashFormatter',
            'message_type': 'auth_log',
            'fqdn': True
        },
    },
    'handlers': {
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash_async.handler.AsynchronousLogstashHandler',
            'transport': 'logstash_async.transport.TcpTransport',
            'host': 'test.example.com',
            'port': 5959,
            'database_path': os.path.join(BASE_DIR, 'queue.db'),
            'formatter': 'logstash',
        }
    },
    'loggers': {
        'async_logstash_memory_leak': {
            'level': 'DEBUG',
            'handlers': ['logstash'],
            'propagate': True,
        }
    },
}
