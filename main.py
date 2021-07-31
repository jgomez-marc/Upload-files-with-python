from github import Github
import time
import colorama # print-color
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

##########################################

g = Github('username', 'password')

# or

g = Github('acces-token')

##########################################

repos = g.get_user().get_repos()

while True:
    try:
        for repo in repos:
            if repo.name == "repository-name":
              
                # Update a file
                    
                contents = repo.get_contents('fielname.xxx') # Write the filename of the file you are going to update
                repo.update_file(contents.path, f'commits', 'Here comes what going to be changed', contents.sha, branch='main')
               
                print(f'{Fore.GREEN}Backup | createt!')
                time.sleep(3600) 
    except:
        print(f'{Fore.RED} Backup | error!')  
        break           
