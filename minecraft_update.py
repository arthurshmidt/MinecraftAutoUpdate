#!/usr/bin/env python3
import os
import sys

import logging
import requests
# import scrapy
from bs4 import BeautifulSoup

# Globals
URL = "https://www.minecraft.net/en-us/download/server/bedrock"
ALLOW = "/home/minecraft/server/bedrock/latest_release/allowlist.json"
WORLDS = "/home/minecraft/server/bedrock/latest_release/worlds"
PROPERTIES = "/home/minecraft/server/bedrock/latest_release/server.properties"

def backup(version):
    os.system("tar -zcvpf /home/minecraft/server/bedrock/backups/backup-bedrock-"+version+".tar.gz "+ALLOW+" "+WORLDS+" "+PROPERTIES)

def cleanup():
    os.system("rm -rf /home/minecraft/server/bedrock/temp/*")
    os.system("cp -rf /home/minecraft/server/bedrock/latest_release/allowlist.json /home/minecraft/server/bedrock/temp")
    os.system("cp -rf /home/minecraft/server/bedrock/latest_release/server.properties /home/minecraft/server/bedrock/temp")
    os.system("cp -rf /home/minecraft/server/bedrock/latest_release/worlds /home/minecraft/server/bedrock/temp")
    _ = input("Enter to Delete latest_release")
    os.system("rm -rf /home/minecraft/server/bedrock/latest_release/*")

def install(version2):
    os.system("unzip /home/minecraft/server/bedrock/server_releases/bedrock-server-"+version2+".zip -d /home/minecraft/server/bedrock/latest_release/")

if __name__ == "__main__":
    print("Backing up version: "+sys.argv[1]+" to "+sys.argv[2])
#    backup(sys.argv[1])
#    cleanup()
    install(sys.argv[2])
