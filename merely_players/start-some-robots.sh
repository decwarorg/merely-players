# ------ help / usages infos -------------------------------------
# bash merely_players/start-some-robots.sh &
# tail -f log1
# pkill -[signal # or name] -f python
# 2  SIGINT  ctrlc   
# 20 SIGTSTP ctrlz
# -----------------------------------------------------------------

rm log/log*
python3 -u merely_players/robot.py > log/log1 &
sleep 2
python3 -u merely_players/robot.py -n robot2 > log/log2 &
sleep 5
python3 -u merely_players/robot.py -n robot3 > log/log3 &
sleep 5
python3 -u merely_players/robot.py -n robot4 > log/log4 &
sleep 5
python3 -u merely_players/robot.py -n robot5 > log/log5 &
sleep 5
python3 -u merely_players/robot.py -n robot6 > log/log6 &
sleep 5
python3 -u merely_players/robot.py -n robot7 > log/log7 &
sleep 5
python3 -u merely_players/robot.py -n robot8 > log/log8 &
sleep 5
python3 -u merely_players/robot.py -n robot9 > log/log9 &
sleep 5
python3 -u merely_players/robot.py -n robot10 > log/log10 &
sleep 5
