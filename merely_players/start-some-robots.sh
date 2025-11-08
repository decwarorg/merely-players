# ------ help / usages infos -------------------------------------
# bash merely_players/start-some-robots.sh &
# tail -f log1
# pkill -[signal # or name] -f python
# 2  SIGINT  ctrlc   
# 20 SIGTSTP ctrlz
# -----------------------------------------------------------------

rm data/log*
python3 -u merely_players/robot.py > data/log1 &
sleep 2
python3 -u merely_players/robot.py -n robot2 > data/log2 &
sleep 5
python3 -u merely_players/robot.py -n robot3 > data/log3 &
sleep 5
python3 -u merely_players/robot.py -n robot4 > data/log4 &
sleep 5
python3 -u merely_players/robot.py -n robot5 > data/log5 &
sleep 5
python3 -u merely_players/robot.py -n robot6 > data/log6 &
sleep 5
python3 -u merely_players/robot.py -n robot7 > data/log7 &
sleep 5
python3 -u merely_players/robot.py -n robot8 > data/log8 &
sleep 5
python3 -u merely_players/robot.py -n robot9 > data/log9 &
sleep 5
python3 -u merely_players/robot.py -n robot10 > data/log10 &
sleep 5
