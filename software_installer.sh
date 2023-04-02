#!/bin/bash

echo "Script to install software"
var=$1

if [ $(uname) == "Linux" ];then 
        echo "This is Linux,Installing $var"
        apt-get install $var
else
        echo "This is Not Linux"
fi