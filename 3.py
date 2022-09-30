#!/usr/bin/env python3
import os
repository = str(input("Enter repository:"))
if repository.find("https") != -1:
    bash_command = ["git checkout" + repository, "git status"]
else:
    bash_command = ["cd" + repository, "git status"]

result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print({repository}/prepare_result)
