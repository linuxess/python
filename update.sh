#!/bin/sh
now=`date +%F-%X`
git add . && git commit -m "update at $now" && git push origin master
