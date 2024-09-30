A test app that uses the Authorization Code Flow (Standard Flow in Keycloak terms)
It:
  - sets up a simple http server
  - requests a code from the keycloak server
  - exchanges the code for an access token
  - prints the access token
  - decodes the access token
