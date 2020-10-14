#!/usr/bin/python2.7

# Depends on PIL (Python Image Library)

import os, sys
from bin import logo_gen as lg

LOGOFILE = "pics/logo.png"
DLFILE = "pics/download_mode.png"
if not os.path.exists("output"):
    os.mkdir("output")

if not os.path.exists(LOGOFILE):
    print("No logo.png file found in pics folder")
    sys.exit(1)
if not os.path.exists(DLFILE):
    print("No download_mode.png file found in pics folder")
    sys.exit(1)

lg.MakeLogoImage(LOGOFILE, "splash.img")
lg.MakeLogoImage(DLFILE, "dl.img")

with open("splash.img", "ab") as myfile, open("dl.img", "rb") as myfile2:
    myfile.write(myfile2.read())

os.remove("dl.img")
