import streamlit as st
import os
import json
import requests
from base64 import b64decode, urlsafe_b64decode


TENANT = os.environ['TENANT']
CLIENT_ID = os.environ['CLIENT_ID']
GRANT_TYPE = "password"
BASE_URL = os.environ['BASE_URL']

def getToken(usrname, passwd):
    token_url = f"{BASE_URL}/{TENANT}/oauth2/v2.0/token"

    body = {
            "client_id": CLIENT_ID,
            "scope": "openid api://f27e716f-0071-44c2-8016-e32535231986/user_impersonation",
            "grant_type": GRANT_TYPE,
            "username": usrname,
            "password": passwd,
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


# username and password fields to connect to Entra
usrname = st.text_input("Username (email address)", placeholder="myemail@aarealdemo.onmicrosoft.com")
passwd = st.text_input("password")

login_btn = st.button("Login with the above credentials", type="primary")
if login_btn: # when the button is clicked
    if usrname and passwd: # proceed only if the username and password have been properly written
        
        st.write(f"Will login now as {usrname}:{passwd}")
        st.subheader("Token Received from Entra ID", divider='gray')
        resp = getToken(usrname, passwd)
        st.write(resp.json())
    
        st.subheader("Decoded Access Token", divider='gray')
        access_token = resp.json()['access_token']
        st.write(json.loads(DecodeTokenOffline(access_token)))

        st.subheader("Decoded ID Token", divider='gray')
        id_token = resp.json()['id_token']
        st.write(json.loads(DecodeTokenOffline(id_token)))

    else:
        st.write('Cannot Log in make sure to press enter at both username and password fields')


print('NEW REQUEST')
