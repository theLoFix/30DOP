#!/bin/bash

path=`pwd`
echo "Path:" $path
cd /c/Program\ Files/Git/bin/
exec ssh-agent bash
ssh-add /c/Users/lukas/.ssh/thelofixBB
cd $path
