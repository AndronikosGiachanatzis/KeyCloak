import streamlit as st
import requests
import sys
from base64 import b64decode
from base64 import urlsafe_b64decode
import jwt
import json
from streamlit_url_fragment import get_fragment


def DecodeTokenOffline(token, token_type='access'):

    parts = token.split(".")

    # decode payload
    decodedBytes=urlsafe_b64decode(parts[1] + '=='*(-len(parts[1])%4))
    decodedString=str(decodedBytes, "utf-8")
    return decodedString
    

def jsonizeFragment(fragment): # prepare and convert fragment to json format
    fragment = str(fragment) 
    fragment = fragment.replace("#", "")
    fragment = "{\"" + fragment + "\"}"
    fragment = fragment.replace("=", "\":\"")
    fragment = fragment.replace("&", "\",\"")

    return json.loads(fragment)



# get fragment
fragment = get_fragment()
if fragment: # if a fragment exists
    st.subheader("Response received from Entra ID", divider='gray')
    fragment = jsonizeFragment(fragment)
    st.write(fragment)
    
    # decode access token
    st.subheader("Decoded Access token", divider='gray')
    st.write(json.loads(DecodeTokenOffline(fragment["access_token"])))
    
    # decode id token
    st.subheader("Decoded ID token", divider='gray')
    st.write(json.loads(DecodeTokenOffline(fragment["id_token"])))

