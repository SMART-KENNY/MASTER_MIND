
### BASIC COMMANDS FOR GIT

#### SETTING UP GIT
- git config --global user.name "Your Name"
- git config --global user.email "your.email@example.com"

#### CHECK CONFIGURATION
- git config user.name
- git config user.email

#### CLONE
- git clone <url>

#### IF YOU MADE CHANGES AND YOU WANT TO ADD THEM
- git add <file> = this will add only a specific files that you have chosen
- git add . = this will add all files that you have made any changes

#### CHECK STATUS
- git status

#### GIT COMMIT
- git commit -m "Commit message"

#### VIEW GIT LOGS
- git log

---

### BRANCHING AND MERGING
- git checkout -b new-branch
- git checkout branch-name
- git merge branch-name

### BRANCHING AND PUSHING AND PULLING
- git push origin branch-name
- git pull

---

### ADDITIONAL COMMANDS 
- git branch -d branch-name = Delete a Branch:
- git checkout -- <file> = Revert Changes:
- git diff = Show Differences:
- git stash = Stash Changes: = Temporarily stores changes in the working directory.


---


### IF YOUR LOCAL DIRECTORY IS NOT INITIALIZE AS A REPROSITORIES OR YOU SEE THIS ERROR
- fatal: not a git repository (or any of the parent directories): .git

#### Then do this step by step
- git init = Initialize Git in Your Directory:
- git add <file> = Add Your File to the Staging Area:
- git commit -m "Initial commit"
- git remote add origin https://github.com/username/repository.git
- git push -u origin master

-- summary commands 
- cd your-directory
- git init
- git checkout -b new-branch
- git add your-file.txt
- git commit -m "Add your-file.txt"
- git remote add origin https://github.com/your-username/your-repository.git
- git push -u origin master  OR git push -u origin new-branch



