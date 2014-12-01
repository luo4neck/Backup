#! /usr/python

import os
import git
import tarfile
import time

### backup for blog ####
target_name = './blog' + os.sep + 'blog_backup.tar.gz'
tar = tarfile.open(target_name, 'w:gz')
for root,dirs,files in os.walk('/home/neck/Blog/source/img'):
	for names in files:
		fullpath = os.path.join(root,names)
		tar.add(fullpath,arcname=names)
for root,dirs,files in os.walk('/home/neck/Blog/source/_posts'):
	for names in files:
		fullpath = os.path.join(root,names)
		tar.add(fullpath,arcname=names)
tar.list()
tar.close()
### backup for blog ####


### git part ###
repo = git.Repo('.')
commit_name = time.strftime('%Y%m%d')

print repo.git.add('*')
print repo.git.commit( m = commit_name )
print repo.git.status()
print repo.git.push()
### git part ###
