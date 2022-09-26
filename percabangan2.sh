#!/bin/bash

printf "Kemana kamu akan berlibur tahun ini?\n"
printf "Bali?\n"
printf "Malang?\n"
printf "Labuan Bajo?\n"

read berlibur

case "$berlibur" in
  "Bali")
    echo "Di Bali, pantainya bagus"
    ;;
  "Malang")
    echo "Malang, udaranya segerr"
    ;;
  "Labuan Bajo")
    echo "Tempat nya bagus dan instagramable"
    ;;
  *)
    echo "Tempat berlibur mu lumayan bagus"
    ;;
esac
