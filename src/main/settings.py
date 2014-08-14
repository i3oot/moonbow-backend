import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("/etc/moonbow/backend.ini")


PIXELBUFFER = Config.get('Server', 'bufferfile', '/etc/moonbow/pixelbuffer')
IMGIDFILE = Config.get('Server', 'imgidfile', '/etc/moonbow/img.id')
DEBUG = Config.get('Server', 'debug', False)
PIXELCOUNT = int(Config.get('Graphics','pixelcount'))



def framesleep():
	return Config.get('Graphics','frameduration', 0.5)

def framesleep(sleep):
	Config.set('Graphics','frameduration', sleep)
	with open("/etc/moonbow/backend.ini", 'wb') as configfile:
		Config.write(configfile)
	return framesleep()
