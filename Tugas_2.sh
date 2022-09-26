#!/bin/bash

echo -n "Berapa tinggi badanmu? ";
read tinggi

if [ $tinggi -ge 120 ]
then
  echo "Kamu bisa memasuki kolam dewasa"
else
  echo "Kamu harus ke kolam anak"
fi
