
## running local on unix

in your merely-players folder, have a venv python virtual environment. can create that with

    python -m venv venv

have your bash shell set to use your venv

    source venv/bin/activate

your bash prompt should now begin with (venv) showing it's active. within your venv, have pip installed pexpect and sshkeyboard

    pip install pexpect
    pip install sshkeyboard

you can also automatically get these by installing the python project via

    pip install .

with project utexas 'booted from disk' and running in a terminal, open other terminals and start robots

    python cic/robots/robot.py -n [captain's name]

or start groups of robots using the start-some-robots bash script

    bash cic/start-some-robots.sh &

to watch and shutdown

    tail -f log1
    pkill -2 -f python
    2 SIGINT     ctrlc
    20 SIGTSTP   ctrlz
