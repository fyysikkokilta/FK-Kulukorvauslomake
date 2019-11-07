import os
import bottle
import kuluserver

kuluserver.setup_application()

if __name__ == '__main__':
    print('Starting server...')
    debug = os.environ['DEBUG'] == 'on'
    bottle.run(
               app=kuluserver.application,
               debug=debug,
               reloader=debug,
               host='0.0.0.0',
               port=8000,
               server='twisted')
