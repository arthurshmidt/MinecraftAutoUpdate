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
LATEST = "/home/minecraft/server/bedrock/latest_release/"
PROPERTIES = "/home/minecraft/server/bedrock/latest_release/server.properties"

def backup(version):
    print("Backing up latest version")
#    os.system("tar -zcvpf /home/minecraft/server/bedrock/backups/backup-bedrock-"+version+".tar.gz "+ALLOW+" "+WORLDS+" "+PROPERTIES)
    os.system("tar -zcvpf /home/minecraft/server/bedrock/backups/backup-bedrock-"+version+".tar.gz "+LATEST)

def cleanup():
    print("Cleaning up")
    os.system("rm -vrf /home/minecraft/server/bedrock/temp/*")
    os.system("cp -vrf /home/minecraft/server/bedrock/latest_release/allowlist.json /home/minecraft/server/bedrock/temp")
    os.system("cp -vrf /home/minecraft/server/bedrock/latest_release/server.properties /home/minecraft/server/bedrock/temp")
    os.system("cp -vrf /home/minecraft/server/bedrock/latest_release/worlds /home/minecraft/server/bedrock/temp")
    _ = input("Press <Enter> to Delete latest_release")
    os.system("rm -rf /home/minecraft/server/bedrock/latest_release/*")

def install(version2):
    _ = input("Press <Enter> to Install version: "+version2)
    os.system("unzip /home/minecraft/server/bedrock/server_releases/bedrock-server-"+version2+".zip -d /home/minecraft/server/bedrock/latest_release/")
    os.system("cp -vrf /home/minecraft/server/bedrock/temp/* /home/minecraft/server/bedrock/latest_release")

if __name__ == "__main__":
    print("Backing up version: "+sys.argv[1]+" to "+sys.argv[2])
    backup(sys.argv[1])
    cleanup()
    install(sys.argv[2])
    print("Update Complete")
