import streamlit as st

CLIENT_ID = 'mycoolapp'
REALM = 'TestRealm'
BASE_URL = 'https://keycloakentra:8443'
APP_URL = 'http://10.2.4.5:3333'

url = f"{BASE_URL}/realms/{REALM}/protocol/openid-connect/auth?"
url += "scope=openid&"
url += "response_type=code&"
url += f"client_id={CLIENT_ID}&"
url += f"redirect_uri={APP_URL}/auth_redirect"

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
html_button += f'<a href="{url}" target="_self"><button class="btn" >Login</button></a>'

st.subheader("Step 1: Initialize the flow (Click the button to login)", divider="grey")
st.markdown(html_button, unsafe_allow_html=True)

st.subheader("Step 2: Redirect to keycloak (Once you click you will go to the KeyCloak login page through this call)", divider="grey")
st.code(url.replace("&", "&\n"))
print('NEW REQUEST')
