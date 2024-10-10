import streamlit as st
import os
import json
import requests
from base64 import b64decode, urlsafe_b64decode


TENANT = os.environ['TENANT']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
GRANT_TYPE = "client_credentials"
BASE_URL = os.environ['BASE_URL']


def getToken():
    token_url = f"{BASE_URL}/{TENANT}/oauth2/v2.0/token"

    body = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "scope": "https://graph.microsoft.com/.default",
            "grant_type": GRANT_TYPE,
        }
    st.write(body)
    
    # make request to get token
    resp = requests.post(
        token_url,
        data=body,
        verify=False
    )

    return resp



def DecodeTokenOffline(token):
    # decode payload
    parts = token.split(".")
    decodedBytes=urlsafe_b64decode(parts[1] + '=='*(-len(parts[1])%4))
    
    decodedString=str(decodedBytes, "utf-8")
    
    return decodedString


login_btn = st.button("Login with with the client secret", type="primary")
if login_btn: # when the button is clicked

     st.subheader("Token Received from Entra ID", divider='gray')
     resp = getToken()
     st.write(resp.json())
    
     st.subheader("Decoded Access Token", divider='gray')
     access_token = resp.json()['access_token']
     st.write(json.loads(DecodeTokenOffline(access_token)))




print('NEW REQUEST')
