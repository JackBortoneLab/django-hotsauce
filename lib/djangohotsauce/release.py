MAJOR_VERSION = '1.3'
MINOR_REVISION = 9
if MINOR_REVISION > 0:
 VERSION = MAJOR_VERSION + '.' + "%s" % MINOR_REVISION
else:
 VERSION = MAJOR_VERSION

BASE_REVISION = VERSION 
RELEASE_NAME = "20210613"
