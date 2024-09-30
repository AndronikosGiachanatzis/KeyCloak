FROM python:3

# set working directory
WORKDIR /app

# copy files to workdir
COPY . /app

# server and app configuration variables
ARG PORT=5544
ARG BASE_URL=https://keycloakentra:8443
ARG CLIENT_ID=mycooldockerapp
ARG REALM_NAME=TestRealm
ARG APP_URL=http://10.2.4.5:${PORT}

# expose port
EXPOSE ${PORT}

# install requirements
RUN pip3 install -r requirements.txt

# set environment variables
ENV PORT=${PORT}
ENV BASE_URL=${BASE_URL}
ENV CLIENT_ID=${CLIENT_ID}
ENV REALM_NAME=${REALM_NAME}
ENV APP_URL=${APP_URL}

# start server
#CMD ["python3", "-m", "streamlit", "run", "/app/app.py", "--server.port", "$PORT"]
CMD python3 -m streamlit run /app/app.py --server.port ${PORT}
