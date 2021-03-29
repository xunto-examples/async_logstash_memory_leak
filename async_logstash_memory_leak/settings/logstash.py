import os

from async_logstash_memory_leak.settings.no_logstash import *

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
