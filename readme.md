# project merely players

- [overview](#overview)
  - [main](#main)
  - [brain](#brain)
- [guide](#guide)
  - [setup](#setup)
  - [usage](#usage)

there are two very different aspects to the decwar 'merely players'. the ability to play decwar and the skill level at that, so the 'brains'. and the character and personality, so the 'humanity'. right now the second of those seems much more fun and important. the focus has shifted away from adding brains and towards growing the humanity. that's probably why decwar is still alive after fifty years. not so much the gameplay or tech. it's the excitement, drama, and mystery. the robots are the answer for bringing those back to life. the game is what it is, and in the project utexas context is purposely regressing and going backwards to its roots. it's simply the darkened and empty theater stage. the robots are the actors coming on stage to perform and bring the play to life.

right now the path forward is to bring back the 'sounds' of playing. especially the sounds of a friday afternoon in the southwest texas state university computation center, san marcos texas, summer 1983. a rowdy decwar battle before everyone heads out for swimming and tubing on the san marcos river. the idea is to capture the laughter and background chatter along with the clatter of keyboards and hammering of teletypes. and connect those with solid personalities. here are some names. grady early. randy. the deacon.

to get an idea of the 'spirit of things', it's not impossible to imagine decwar in a gunship video right alongside the breakfast club, blade runner, and miami vice. and war games and real genius, of course. the thing about gunship is that there's a special mix of fun, humour, nostalgia, and a peculiar seriousness and 'poetry'. something to keep in mind.

# overview

boring 'infrastructure' stuff is corralled into main. fun 'decwar specific' stuff begins with the brain. the brain kicks in and takes over once the decwar game command prompt is available, and only knows about giving decwar commands and reacting to decwar output.

## main

the 'secret' here is that there's a child thread with a robot instance spinning slowly and handling telnet, tops10, and pregame topics. the main thread is meanwhile listening to the keyboard. the idea is that the main thread always has to ask and wait for the child thread to take any actions, hopefully in a calm, reasonable, clean way. for shutdown, the child should quit decwar, logout of tops10, and close the telnet connection, at which point finally both threads can exit.

## brain

a brain object is effectively a 'ship in the game'. it knows how to give commands and handle the resulting output. on top of that, it adds basic concepts of 'what to do'. this is where things get interesting. without getting too complex and going beyond minimalist approaches, the tougher, longer surviving, and harder to beat the robots can become, the better. 

# guide

## setup

in your utexas folder, have a venv python virtual environment. can create that with

    python -m venv venv

have your bash shell set to use your venv

    source venv/bin/activate

your bash prompt should now begin with (venv) showing it's active. within your venv, have pip installed pexpect and sshkeyboard

    pip install pexpect
    pip install sshkeyboard

## usage

with project utexas 'booted from disk' and running in a terminal, open other terminals and use the commands

    python robots/main.py [captain's name]
    bash robots/start-some-robots.sh &

to watch and shutdown

    tail -f log1
    pkill -2 -f python
    2 SIGINT     ctrlc
    20 SIGTSTP   ctrlz
