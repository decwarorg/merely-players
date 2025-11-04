FROM python:3.11-slim

ENV PYTHOPATH /docker
WORKDIR $PYTHOPATH
COPY merely_players $PYTHOPATH/merely_players
COPY /pyproject.toml $PYTHOPATH/pyproject.toml

RUN pip install -e .

CMD ["fastapi", "run", "merely_players/api.py", "--port", "2031"]
