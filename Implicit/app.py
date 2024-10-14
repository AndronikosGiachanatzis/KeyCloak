import streamlit as st

TENANT = os.environ['TENANT']
CLIENT_ID = os.environ['CLIENT_ID']
BASE_URL = "https://login.microsoftonline.com"
APP_URL = os.environ['APP_URL']
SCOPE = f"openid email profile api://{CLIENT_ID}/user_impersonation"
RESPONSE_TYPE="id_token token"

def buildURL():
    url = f"{BASE_URL}/{TENANT}/oauth2/v2.0/authorize?"
    url += f"scope={SCOPE}&"
    url += f"response_type={RESPONSE_TYPE}&"
    url += f"client_id={CLIENT_ID}&"
    url += f"redirect_uri={APP_URL}/auth_redirect&"
    url += f"response_mode=fragment&"
    url += f"nonce=123456"

    return url


# build Entra ID sign-in url
url = buildURL()

html_button = """
<style>
    .btn {
    background-color:#4169E1;
    color: #fff;
    border:none; 
    border-radius:10px; 
    padding:15px;
    min-height:30px; 
    width: 100%;
  }
</style>
"""
# button to redirect to Entra ID login
html_button += f'<a href="{url}" target="_self"><button class="btn" >Login</button></a>'

st.subheader("Step 1: Initialize the flow (Click the button to login)", divider="grey")
st.markdown(html_button, unsafe_allow_html=True)

st.subheader("Step 2: Redirect to Entra ID (Once you click you will go to the Entra ID login page through this call:)", divider="grey")
st.code(url.replace("&", "&\n"))
print('NEW REQUEST')
