# pasos Learning Assistant

## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Create a new environment using the following command:
```bash
$ python3 -m venv <env-name>
```
3) Activate the environment:
```bash
$ source <env-name>/bin/activate
```
## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
$ cd docker
$ cp .env.example .env
```

- update `.env` with your credentials



```bash
$ cd docker && sudo docker compose up -d && cd ..
```

## Run the FastAPI server

```bash
$ cd src && uvicorn main:app --reload --host 0.0.0.0 --port 5000 && cd ..
```
