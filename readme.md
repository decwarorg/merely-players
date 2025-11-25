# project merely players

- [basics](#basics)
- [overview](#overview)
  - [robot](#robot)
  - [brain](#brain)
  - [app](#app)
- [guide](#guide)
  - [python](#python)
  - [docker compose](#docker-compose)
- [versions](#versions)

# basics

cd into the merely-players folder. the first command below removes the three docker images so they will be fully rebuilt by the second command. in practice, often only one of the images is changing and needs to be removed. the third command then starts the complete system.

    docker image rm utexas cic galaxy
    python3 prep.py
    docker compose up

once the utexas container has reached 'GAM assigned', the dec10 is ready.
open a web browser to 'localhost:2031/cic' for control over the robots. hit the start robots button.
open a web browser to 'localhost:2032' for galaxy display. 
open terminal and do 'telnet localhost 2030' to personally enter the game

# overview

there are two very different aspects to the decwar 'merely players'. the ability to play decwar and the skill level at that, so the 'brains'. and the character and personality, so the 'humanity'. right now the second of those seems much more fun and important. the focus has shifted away from adding brains and towards growing the humanity. that's probably why decwar is still alive after fifty years. not so much the gameplay or tech. it's the excitement, drama, and mystery. the robots are the answer for bringing those back to life. the game is what it is, and in the project utexas context is purposely regressing and going backwards to its roots. it's simply the darkened and empty theater stage. the robots are the actors coming on stage to perform and bring the play to life.

right now the path forward is to bring back the 'sounds' of playing. especially the sounds of a friday afternoon in the southwest texas state university computation center, san marcos texas, summer 1983. a rowdy decwar battle before everyone heads out for swimming and tubing on the san marcos river. the idea is to capture the laughter and background chatter along with the clatter of keyboards and hammering of teletypes. and connect those with solid personalities. here are some names. grady early. randy. the deacon.

to get an idea of the 'spirit of things', it's not impossible to imagine decwar in a gunship video right alongside the breakfast club, blade runner, and miami vice. and war games and real genius, of course. the thing about gunship is that there's a special mix of fun, humour, nostalgia, and a peculiar seriousness and 'poetry'. something to keep in mind.

boring 'infrastructure' stuff is corralled into main. fun 'decwar specific' stuff begins with the brain. the brain kicks in and takes over once the decwar game command prompt is available, and only knows about giving decwar commands and reacting to decwar output.

## robot

the 'secret' here is that there's a child thread with a robot instance spinning slowly and handling telnet, tops10, and pregame topics. the main thread is meanwhile listening to the keyboard. the idea is that the main thread always has to ask and wait for the child thread to take any actions, hopefully in a calm, reasonable, clean way. for shutdown, the child should quit decwar, logout of tops10, and close the telnet connection, at which point finally both threads can exit.

## brain

a brain object is effectively a 'ship in the game'. it knows how to give commands and handle the resulting output. on top of that, it adds basic concepts of 'what to do'. this is where things get interesting. without getting too complex and going beyond minimalist approaches, the tougher, longer surviving, and harder to beat the robots can become, the better. 

## app

this is the 'cic' rest api that is started up as a background service. it's purpose is to output information to clients such a the glaxy display, and to act as centralized control for the robots and for the game.

# guide

this is a python and docker project, and both are assumed to be installed. the details of getting to that point are fairly os dependent and beyond the scope here. basically, anyone interested enough to get to this point right here probably knows how to have python and docker ready for action.

## python

this is a python project and it's used wherever possible. the project should work as smoothly as possible on linux, windows, and mac. python virtual environments should only be needed for running and working on the code locally. for docker containers virtual environments shouldn't be an issue since containers are themselves 'virtual environments'. this guide will bypass local non container 'dev mode' runs and focus on high level dockerized ops. dev mode can be addressed in dedicated docs.

## docker compose

the objective here is a simple push button 'turn key and go' way to run the primordial utexas decwar and have as much fun as possible. that means a pdp10-kl simulator running all of the original sofware from tape images, and able to build decwar on the fly at every boot with modifications to the original fortran and mac10 flowing in smoothly. to really have fun there have to be other players. the more the better. robots have to be telnetting in and playing. that's done with python. and then, even more fun, is a graphical display of the whole galaxy. ideally with sounds as well. that's done via webbrowser using p5js javascript. here's where things are at the moment.

    https://gitlab.com/decwar/utexas - pure stone age
    https://gitlab.com/decwar/merely-players - pure python robots and 'cic' api
    https://gitlab.com/decwar/galaxy - pure p5js display calling 'cic' api

how to unify these three forces? doco. [docker compose](https://docs.docker.com/compose/)

the project push button concept is that doco is the unifier, controller, automator, and interface for casual play. everything should be reduced as much as possible to a matter of doco usage. of course in reality there will always be more frictions and bumps to smooth out. this is not a simple system, and on top of the three forces shown above, doco is effectively a fourth force. why all the complexity.

for one thing, the system should transparently move across intel, amd, arm, cloud, not to mention future hardware. and the usual software permutations of linux, windows, mac. in particular, at the moment the system is being used on a raspi and a macbook. the only thing the two have in common is the three gitlab repos. doco is available on both and used to run the game. it's now standard to have two simultaneous decwar games going on with ten robot players in each. one on the raspi, the other on the macbook.

for another thing, keeping all the forces separate is better for advancing and maintaining the code. stone age, python, and p5js are completely different planets, if not even different galaxies. there's effectively zero overlap between the three, and zero need to know about the details within the other two in order to work on one. someone interested in the original fortran and assembly language can put all their effort into the utexas repo. another person interested in visual displays can put all their effort into the galaxy repo.

and there's actually some simplification. in the 2000s getting new software meant download installer, install, run. now it can be as simple as download container, run. that's the ideal to work towards.

# versions

- v1.0 20251109
