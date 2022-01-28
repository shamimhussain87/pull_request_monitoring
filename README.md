# github-pull-request-monitoring
>Github pull request monitoring using PyGithub library
>>PyGithub is a python library by which we can access Github Rest Api and perform different operations depends upon our requiremnets .In this section we focused more on repositories access and Pull requests related data .

# Depenedencies to setup before working :
1) Install PyGithub using command line : pip install PyGithub
2) Tested on python3.6 or above
3) Import Datetime library for time claculation purpose of pull requests
4) Generate token from console of Github to access or read data related to that particular account

# Steps to follow after setting up dependencies

1) Create user and personal access tokens in source and target GitHub. 
2) User should have read privileges to source and target account.

# Required inputs to the algorithm

1) It requires username of github user for which you want to check pull request creation time
2) It also requires no of pull requests for which you want to get information about there completion.
3) You can provide the custom account creation date or the algo use the default account creation date

# Output provided by an algorithm

1) Output will be the total time taken by user to make pull requests on different repositories of an owner account.
2) Or an exception scenario in which user does not make an pull request or user does not exists.
# Actions performed

 1) Clone description, pull requests ,creation dates and users info from required repos.
 2) Get list of all repos from the github account.
 3) List all open pull requets for the given user.
 4) Neglect pull requests for the blacklist repositories .
 5) Count duration of pull request from account creation till the last pull request.
 6) Get pull requests data of user based on the pull requests done on main/master branch
 
# Source: 
Simple example of the usage of the PyGithub python module

https://pygithub.readthedocs.io/en/latest/introduction.html

