import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("/etc/moonbow/backend.ini")


PIXELBUFFER = Config.get('Server', 'bufferfile', '/tmp/pixelbuffer')
DEBUG = Config.get('Server', 'debug', False)

PIXELCOUNT = int(Config.get('Graphics','pixelcount'))
FRAMESLEEP = Config.get('Graphics','framesleep', 0.5)
