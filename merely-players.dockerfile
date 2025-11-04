# couldn't get telnet onto python images, but can do with ubuntu
# ubuntu 24.04 brings all kinds of pain around pip
FROM ubuntu:22.04
RUN apt-get update && apt-get install build-essential cmake telnet -y
RUN apt-get install python3 python3-dev python3-pip python3-setuptools -y
RUN pip install pexpect sshkeyboard fastapi[standard]

ADD merely_players /merely_players
ENV PYTHONPATH="${PYTHONPATH}:/merely_players"

CMD ["fastapi", "run", "merely_players/api.py", "--port", "2031"]
