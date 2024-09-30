A test app that uses the Authorization Code Flow (Standard Flow in Keycloak terms)
It:
  - sets up a simple http server
  - requests a code from the keycloak server
  - exchanges the code for an access token
  - prints the access token
  - decodes the access token

# Before running update the Dockerfile with your configuration
- **PORT**: The port on which your app server will be running/listening to for requests
- **BASE_URL**: The KeyCloak server url (i.e. https://keycloak)
- **CLIENT_ID**: The client id of the client in KeyCloak
- **REALM_NAME**: The name of the KeyCloak realm where the client exists
- **APP_URL**: The URL that is used to access the current app (needed for a redirect URL in the token request). Note that it should be the same as the root URL configured in the KeyCloak client


# How to run:
Build the image (go to the directory where the dockerfile is located):     
```sudo docker build -t IMAGE-NAME . ```

Create and run container:     
```sudo docker run -it --rm -p PORT:PORT --name CONTAINER-NAME IMAGE-NAME ```

- If the KeyCloak server is accessed by a hostname then either configure DNS or simply add the ```--add-host HOSTNAME:IP``` option to add one in the container
- If you want to start the container in the background replace ```-it``` with ```-d```

