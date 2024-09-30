FROM python:3

# set working directory
WORKDIR /app

COPY . /app

# add DNS entry for keycloak
#RUN echo "10.2.7.4 keycloakentra" >> /etc/hosts

# expose port
EXPOSE 5544

# install requirements
RUN pip3 install -r requirements.txt

# set environment variables
ENV PORT=5544
ENV BASE_URL=https://keycloakentra:8443
ENV CLIENT_ID=mycooldockerapp
ENV REALM_NAME=TestRealm
ENV APP_URL=http://10.2.4.5:5544

# start server
CMD ["python3", "-m", "streamlit", "run", "/app/app.py", "--server.port", "5544"]
