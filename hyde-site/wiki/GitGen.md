##Git Generalities

###Download: 

[http://git-scm.com/](http://git-scm.com/)

###How we set this up
####End Users

    git clone git://uv-cdat.llnl.gov/uv-cdat.git

####CDAT and UV-CDAT

CDAT and UV-CDAT involve many users on many different section, in order to avoid people to step onto each other, "sub-repo" have been created for developpers to be able to work on their area w/o impedding on other areas of development. PCMDI takes responsability to merge all project back into the main (end-users) repo.

####Procedure

1. clone the "main" repo

        git clone git:///bla

2. Add the "Sub-repos" you are interested in

        git repo add Your-Chosen-Name-For-This-Repo git@bla

3. Repeat 2. for each repo you would like
4. fetch all the data

        git fetch --all

5. Create local tracked branches to work on (or just to look at)

        git checkout -b Your-Local-Branch-Name Your Chosen Name For This Repo/master

  * master can be replaced with the name of a specific branch on the remote repo

6. To Navigate between your local branches

        git checkout Your-Local-Branch-Name
        git pull

####Tips

* Showing your remote repos

        git remote show

* Showing details on a specific remote repo

        git remote show Your-Chosen-Name-For-This-Repo

* Navigating between your local branches

        git checkout Your-Local-Branch-Name
        git pull 

* Creating A New Branch On A Repo

        git push Your-Chosen-Name-For-This-Repo HEAD:NewBranchName


