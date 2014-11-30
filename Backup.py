#! /usr/python

import os
# import git
import tarfile
import time

target_name = './Blog' + os.sep + time.strftime('%Y%m%d') + '.tar.gz'

tar = tarfile.open(target_name, 'w:gz')

for root,dirs,files in os.walk('/home/neck/Blog/source/_posts'):
	for names in files:
		fullpath = os.path.join(root,names)
		tar.add(fullpath,arcname=names)

tar.list()
tar.close()

git_add = ('git add *')
git_commit = ('git commit -m %s') % time.strftime('%Y%m%d')

os.system()
