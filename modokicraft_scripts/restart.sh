#sh quit.sh &&
screen -X -S minecraft quit &&
screen -X -S minecraft2 quit &&
screen -X -S minecraft3 quit &&
screen -X -S minecraft4 quit &&
wait
cd ~/KUMOSAN/modokicraft_scripts/ && sh start_minecraft.sh
