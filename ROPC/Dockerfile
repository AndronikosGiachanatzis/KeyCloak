FROM python:3

# set working directory
WORKDIR /app

# copy files to workdir
COPY . /app

# server and app configuration variables
ARG PORT=<PORT>
ARG BASE_URL=https://login.microsoftonline.com
ARG TENANT=<TENANT>
ARG CLIENT_ID=<CLIENT-ID>
ARG CLIENT_SECRET=<CLIENT-SECRET>

# expose port
EXPOSE ${PORT}

# install requirements
RUN pip3 install -r requirements.txt

# set environment variables
ENV PORT=${PORT}
ENV BASE_URL=${BASE_URL}
ENV TENANT=${TENANT}
ENV CLIENT_ID=${CLIENT_ID}
ENV CLIENT-SECRET=${CLIENT-SECRET}

# start server
#CMD ["python3", "-m", "streamlit", "run", "/app/app.py", "--server.port", "$PORT"]
CMD python3 -m streamlit run /app/app.py --server.port ${PORT}
