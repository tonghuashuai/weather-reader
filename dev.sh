while true
do
    python /home/tonghs/weather-reader/misc/coffee_const.py
    python /home/tonghs/weather-reader/app.py

    for i in $(seq 5)
    do
        echo $i
        sleep 1
    done

done
