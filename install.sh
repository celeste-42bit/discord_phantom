#!/bin/bash
echo "This is the install script for discord_phantom"
echo
echo "Make sure python 3.11 and python-venv are installed, otherwise this script will error-out!"
sleep 5
echo "Setting up the environment for python 3.11 ..."

cd .
ls -la | grep "env" # setup check for existing .env (ls | grep?!)
#setup check for existing venv installation (opt version number, check for output)
python3 -m venv env
source ./env/bin/activate
python3 -m pip install discord.py

echo "Environment setup installed discord.py && discord.ext"