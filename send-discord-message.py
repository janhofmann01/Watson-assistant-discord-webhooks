# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:38:21 2021

@author: Hofmann
"""


import requests


def main(dict):
    
    discordurl = "INSERT_YOUR_URL"
    
    
    try:
        r = requests.post(discordurl, data=dict)
    except Exception as err:
        return {"message": "an error occured while trying to call the discord webhook."}
    
    
    #If the message was sent successfully, the respose's body is empty
    if not r.text:
        return {"message": "Message was sent successfully"}
    
    #else: return errormessage
    return r.text

if __name__ == "__main__": main(dict)