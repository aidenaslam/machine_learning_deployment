FROM python:3.9.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/sports-classifier-api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./04_CircleCI_Docker/sports-classifier-api /opt/sports-classifier-api/
RUN pip install --upgrade pip
RUN pip install -r /opt/sports-classifier-api/requirements.txt

RUN chmod +x /opt/sports-classifier-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
