FROM python:alpine3.10
LABEL maintainer="Tonny-Bright"

# Install required packages
RUN apk --no-cache add \
    bash \
    curl \
    python3 \
    py3-pip

# Install the Google Cloud SDK
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-356.0.0-linux-x86_64.tar.gz \
    && tar zxvf google-cloud-sdk-356.0.0-linux-x86_64.tar.gz \
    && rm google-cloud-sdk-356.0.0-linux-x86_64.tar.gz \
    && ./google-cloud-sdk/install.sh --quiet

# Add the Google Cloud SDK binaries to the PATH
ENV PATH="/google-cloud-sdk/bin:${PATH}"

# Set the working directory
WORKDIR /app

# Copy your Python script and other necessary files to the container
COPY app /app
COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base musl-dev gcc linux-headers \
    libffi-dev python-dev

# Install any additional Python dependencies
RUN pip install -r /tmp/requirements.txt

# Set the entry point for your script
ENTRYPOINT ["python", "main.py"]


