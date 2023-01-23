#!/usr/bin/env python3
import os
import sys

import logging
import requests
# import scrapy
from bs4 import BeautifulSoup

# Globals
URL = "https://www.minecraft.net/en-us/download/server/bedrock"
ALLOW = "/home/minecraft/server/bedrock/allowlist.json"
WORLDS = "/home/minecraft/server/bedrock/worlds"
PROPERTIES = "/home/minecraft/server/bedrock/server.properties"
PROG = "/home/minecraft/server/bedrock/server_releases/bedrock-server-"

def backup(version):
    os.system("tar -zcvpf /home/minecraft/server/bedrock/backups/backup-bedrock-"+version+".tar.gz "+ALLOW+" "+WORLDS+" "+PROPERTIES+" "+PROG+version+".zip")

def cleanup():
    os.system("rm -rf /home/minecraft/server/bedrock/temp/*")
    os.system("cp -rf /home/minecraft/server/bedrock/latest_release/allowlist /home/minecraft/server/bedrock/temp")

if __name__ == "__main__":
    print("Backing up version: "+sys.argv[1]+" to "sys.argv[2])
#    backup(sys.argv[1])
    cleanup()
#    os.system("tar -zcvpf backup-"+sys.argv[1]+".tar.bz2 README.md") 
