"""

Parameter setup
===============
"""
__author__ = 'jiayiliu'

import ConfigParser
from os import system

config = ConfigParser.RawConfigParser()
config.read("./photoz.cfg")

# galaxy catalog position
CAT_PATH = config.get("Galaxy Catalog", "CAT_PATH")

## galaxy file pattern
CAT_PATTERN = config.get("Galaxy Catalog", "CAT_PATTERN")

## galaxy file content order: [ra, dec, bands ...]
CAT_BANDS = eval(config.get("Galaxy Catalog", "CAT_BANDS"))

## database position
DB_FILE = config.get("Database", "DB_FILE")

## detection method
P_method = eval(config.get("Database", "P_method"))

#: Table name for catalog
DB_CAT = config.get("Database", "DB_CAT")

#: Table name for photoz
DB_PZ = config.get("Database", "DB_PZ")

########## Color magnitude information ##########
#: CMR_combination file path
CMR_path = config.get("CMR", "CMR_path")

#: Color band information, specify the column order as [z, g, r, i, z]
CMR_BANDS = eval(config.get("CMR", "CMR_BANDS"))

#: Number of L* for all band, which is the total columns minus 1 (from redshift)
CMR_NL = config.getint("CMR", "CMR_NL")

#: color combinations, each color need to be in CMR_BANDS
CMR_combination = eval(config.get("CMR", "CMR_combination"))

#: color for plotting
CMR_COLOR = eval(config.get("CMR", "CMR_COLOR"))

########## P(z) files ##########
#: Photo-z file path
PHOTOZ_PATH = config.get("Photoz", "PHOTOZ_PATH")

#: P(z) file name pattern
PZ_pattern = config.get("Photoz", "PZ_pattern")

#: sigma clipping
NSIGMA = config.getfloat("Photoz", "NSIGMA")

#: interation in sigma clipping
NITER = config.getint("Photoz", "NITER")

########## Output Path ##########
#: output pattern - path/{0:d}
OUTPUT_CAT_PATTERN = config.get("OUTPUT", "OUTPUT_CAT_PATTERN")

#: figure output pattern - path/{0:d}
OUTPUT_CMR_PATTERN = config.get("OUTPUT", "OUTPUT_CMR_PATTERN")

#: region output files pattern - path/{0:s}
OUTPUT_REGION_PATTERN = config.get("OUTPUT", "OUTPUT_REGION_PATTERN")

########### DS9 ##########
def call_ds9(cid, band):
    """
    call ds9 for plotting

    :param cid: cluster ID
    :param band: color combination
    """
    print "\033[33m ... Openning FITS file ... \033[0m"
    system("ds9new.sh {0:d} {1:s}".format(cid, band))

########## Extra Loading ########
n = config.getint("Extra", "N")
for i in range(n):
    exec(config.get("Extra", "E{0:d}".format(i)))

