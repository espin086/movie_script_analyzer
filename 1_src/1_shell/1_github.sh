#!/bin/bash
clear
if [ $1 = "--h" ]
then
	echo ""
    echo "************** HELP FILE **************"
    echo ""
    echo "Author: JJ Espinoza"
    echo "Description: Creates and Manages Github Repository"
    echo ""
    echo "---------------------------------------"
    echo ""
    echo "Commands:                                                 Info:"
    echo "./1_github.sh --h		                          Help Menu"
    echo "./1_github.sh --create [localpath] [github_url]	          Creates Github folder"
    echo "./1_github.sh --pull [localpath]	                  Refreshes local repository"
    echo "./1_github.sh --push [localpath] [commit message]         Updates remote repository"
    echo ""
    echo "Current Directory is: "
    pwd
    echo ""
    echo "---------------------------------------"

fi

#Creates a new Github repository
if [ $1 = "--create" ]
then
    cd $2
    git init
    git status
    git add .
    git status
    git commit -m "first commit"
    git status
    git remote add origin $3
    git remote -v
    git push -u origin master
    git status

fi

#Pulls any remote changes
if [ $1 = "--pull" ]
then
    cd $2
	git fetch origin
    git branch -a
    git merge origin/master
fi

#Pushes any local changes
if [ $1 = "--push" ]
then
    cd $2
    git add .
    git commit -m $3
    git push -u origin master
fi







