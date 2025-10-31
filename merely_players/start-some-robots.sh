# ------ help / usages infos -------------------------------------
# bash merely_players/start-some-robots.sh &
# tail -f log1
# pkill -[signal # or name] -f python
# 2  SIGINT  ctrlc   
# 20 SIGTSTP ctrlz
# -----------------------------------------------------------------

rm log*
python -u merely_players/main.py > log1 &
sleep 2
python -u merely_players/main.py -n robot2 > log2 &
sleep 5
python -u merely_players/main.py -n robot3 > log3 &
sleep 5
python -u merely_players/main.py -n robot4 > log4 &
sleep 5
python -u merely_players/main.py -n robot5 > log5 &
sleep 5
python -u merely_players/main.py -n robot6 > log6 &
sleep 5
python -u merely_players/main.py -n robot7 > log7 &
sleep 5
python -u merely_players/main.py -n robot8 > log8 &
sleep 5
python -u merely_players/main.py -n robot9 > log9 &
sleep 5
python -u merely_players/main.py -n robot10 > log10 &
sleep 5
