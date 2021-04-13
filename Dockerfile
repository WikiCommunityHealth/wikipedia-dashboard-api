FROM python:3.9.4-buster
WORKDIR /server
RUN pip install pipenv  
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile
COPY . .
CMD [ "pipenv", "run", "start"]