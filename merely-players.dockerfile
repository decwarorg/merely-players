# couldn't get telnet onto python image, but can do with ubuntu
# ubuntu 24.04 brings all kinds of pain around pip
FROM ubuntu:22.04
RUN apt-get update && apt-get install build-essential cmake telnet -y
RUN apt-get install python3==3.10.12 python3-dev==3.10.12 python3-pip==3.10.12 python3-setuptools==3.10.12 -y
RUN pip install pexpect==4.9.0 sshkeyboard==2.3.1 fastapi[standard]==0.121.0

ADD merely_players /merely_players
ENV PYTHONPATH="${PYTHONPATH}:/merely_players"

CMD ["fastapi", "run", "merely_players/api.py", "--port", "2031"]
