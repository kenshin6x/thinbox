class Wrapper:

    def __init__(self, application):
        self.__application = application

    def __call__(self, environ, start_response):
        if environ.get('HTTP_CONTENT_ENCODING', '') == 'gzip':
            buffer = cStringIO.StringIO()
            input = environ['wsgi.input']
            blksize = 8192
            length = 0

            data = input.read(blksize)
            buffer.write(data)
            length += len(data)

            while data:
                data = input.read(blksize)
                buffer.write(data)
                length += len(data)

            buffer = cStringIO.StringIO(buffer.getvalue())

            environ['wsgi.input'] = buffer
            environ['CONTENT_LENGTH'] = length

        return self.__application(environ, start_response)


import sys
import site
import os

prev_sys_path = list(sys.path)

site.addsitedir('/usr/local/thinbox/lib/python2.7/site-packages')
sys.path.append('/usr/local/thinbox/thinbox_web')

new_sys_path = [p for p in sys.path if p not in prev_sys_path]

for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'thinbox.settings'

application = Wrapper(WSGIHandler())
