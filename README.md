# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


- Git manages multiple versions of source code and record them into a repository. It is a distributed version control system used in this project

- GitHub is the cloud based platform used in this project. It serves as a location for uploading copies of a Git repository for collaboration

- Bash terminal in the VSCode platform is used to run all the commands for Git and for running the python script. 

- Vim is the source-code editor used to edit and update the python scripts and README file 

## Milestone 1:

Create a repository with the name 'hangman' in GitHub to save everything in one place

## Milestone 2:
\
The below command clones the 'hangman' repository in the GitHub to the bash terminal in the local machine

        git clone https://github.com/TellisAshwini/hangman.git
\
The below command is used to create a file milestone_2.py within 'hangman' repository

        touch milestone_2.py
\
The below commands are frequently used to stage changes and commit them to the 'hangman' repository

        git add milestone_2.py
        git commit milestone_2.py
\
The below command is used to push the commited changes in the  local repository to the GitHub repository

        git push
\
The below command is used to edit or update the python code in milestone_2.py

        vim milestone_2.py

\
In milestone_2.py file, create a python list of 5 fruits. 
- Import the 'random' module
- Using 'choice' method of this module, print a random element from the created list

\
Create a variable that asks for user input to enter a single letter. 
- Check if the length of the letter is 1 and the input is a alphabet (check using 'isalpha' function) 
- If the condition is met, print a message to the user saying he guessed it correctly. If not then print a message saying its a invalid input


