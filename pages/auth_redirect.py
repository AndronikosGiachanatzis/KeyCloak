import streamlit as st
import requests
import sys
from base64 import b64decode
import jwt
import json

sys.path.append('pages/')
from app import BASE_URL
from app import CLIENT_ID
from app import REALM
from app import APP_URL

def DecodeToken(token, token_type='access'):
    jclient = jwt.PyJWKClient(CERT_URL)
    sign_key = jclient.get_signing_key_from_jwt(access_token)
    if token_type is 'access':
        payload = jwt.decode(token, sign_key.key, algorithms=["RS256"], audience="account")
    else:
        payload = jwt.decode(token, sign_key.key, algorithms=["RS256"], audience=CLIENT_ID)
    return payload

# endpoint to fetch the public key
CERT_URL = f"{BASE_URL}/realms/{REALM}/protocol/openid-connect/certs"
print(CERT_URL)
st.subheader("Step 4: Redirect to the app with query params (What Keycloak returned)", divider="grey")
st.write(st.query_params)

st.subheader("Step 5: Exchanging the code for the token id (Request to exchange to code with token)", divider="grey")
with st.echo():
    token_url = f"{BASE_URL}/realms/{REALM}/protocol/openid-connect/token"

    body = {
            "client_id": {CLIENT_ID},
            "redirect_uri": F"{APP_URL}/auth_redirect",
            "grant_type": "authorization_code",
            "code": st.query_params["code"],
        }

    resp = requests.post(
        token_url,
        data=body,
        verify=False
    )

st.subheader("Code flow result (After exchange of code with token these are the tokens returned from KeyCloak", divider="grey")
st.write(resp.json())

try:
    access_token = resp.json()['access_token']
    print(access_token)
except:
    pass

payload = DecodeToken(access_token)
print(json.dumps(payload, indent=4))


st.subheader("Decoded Access Token", divider='gray')
st.write(payload)

st.subheader("Decoded ID Token", divider='gray')
id_token = resp.json()['id_token']
payload = DecodeToken(id_token, token_type='id')
st.write(payload)
