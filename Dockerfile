FROM python:3.9.4-buster
WORKDIR /server
RUN pip install pipenv  
COPY . .
RUN pipenv install --system --deploy --ignore-pipfile
CMD [ "pipenv", "run", "start"]