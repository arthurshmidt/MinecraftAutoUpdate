#!/usr/bin/env python3
import os
import sys

import logging
import requests
# import scrapy
from bs4 import BeautifulSoup

# Globals
URL = "https://www.minecraft.net/en-us/download/server/bedrock"
ALLOW = "/home/minecraft/server/bedrock-edition/allowlist.json"
WORLDS = "/home/minecraft/server/bedrock-edition/worlds"
PROPERTIES = "/home/minecraft/server/bedrock-edition/server.properties"
PROG = "/home/minecraft/server/bedrock-edition/bedrock-"

if __name__ == "__main__":
    print("Backing up version: "+sys.argv[1])
    os.system("tar -zcvpf /home/minecraft/server/bedrock-edition/backups/backup-"+sys.argv[1]+".tar.gz "+ALLOW+" "+WORLDS+" "+PROPERTIES+" "+PROG+sys.argv[1])
#    os.system("tar -zcvpf backup-"+sys.argv[1]+".tar.bz2 README.md") 
