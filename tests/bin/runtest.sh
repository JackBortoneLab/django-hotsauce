#!/bin/sh
shift;
interpreter=$1
if [ -r "/etc/djangorc" ];
then
 echo 'Loading custom djangorc..'
 echo "PYTHON interpreter = $PYTHON"
 . /etc/djangorc
fi
$PYTHON ./bin/run.py $@
