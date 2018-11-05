import bottle

class Controller:
    def __init__(self, routes):
        for route in routes:
            bottle.route(**route)
