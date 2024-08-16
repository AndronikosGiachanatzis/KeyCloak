import streamlit as st
import requests
import sys

sys.path.append('../')
from app.py import BASE_URL
from app.py import CLIENT_ID
from app.py import REALM
from app.py import APP_URL



st.subheader("Step 4: Redirect to the app with query params", divider="grey")
st.write(st.query_params)

st.subheader("Step 5: Exchanging the code for the token id", divider="grey")
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
        data=body
    )

st.subheader("Code flow result", divider="grey")
st.write(resp.json())