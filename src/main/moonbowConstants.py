import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("/etc/moonbow/backend.ini")


PIXELBUFFER = Config.get('Server', 'bufferfile', '/etc/moonbow/pixelbuffer')
IMGIDFILE = Config.get('Server', 'imgidfile', '/etc/moonbow/img.id')
DEBUG = Config.get('Server', 'debug', False)

PIXELCOUNT = int(Config.get('Graphics','pixelcount'))
FRAMESLEEP = float(Config.get('Graphics','frameduration', 0.5))
