export DJANGO_SETTINGS_MODULE="async_logstash_memory_leak.settings.no_logstash"
mprof run --multiprocess python manage.py runserver