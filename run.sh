#!/bin/bash
Quit=0
trap 'Ctrl' INT
function Ctrl(){
	Quit=1
}
echo "Connecting to $1"
python3 cv_video.py &
python3 breathingnews.py -s $1 &
while [ $Quit == 0 ];do
	echo "running"
	sleep 1
done
kill -9 `ps aux |grep breathingnews|grep -v grep|awk -F' ' '{print $2}'`
kill -9 `ps aux |grep cv_video|grep -v grep|awk -F' ' '{print $2}'`
#tar -czvf data_new.tar.gz tmp/
#mv data_new.tar.gz tmp/

