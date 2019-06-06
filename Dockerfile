FROM python:3.6.8-slim-stretch
ENV PYTHONUNBUFFERED 1

# Install deps and remove apt lists
RUN apt-get update 
RUN apt-get upgrade -y 
RUN apt-get install --no-install-recommends -y build-essential python3-dev
RUN pip install --upgrade pip 
RUN apt-get autoremove -y
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy source to app dir
RUN mkdir /app
COPY location_tree/ /app

COPY requirements.txt /app
RUN pip install -r app/requirements.txt

WORKDIR /app