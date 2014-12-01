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



git_add = ('git add *')
git_commit = ('git commit -m %s') % time.strftime('%Y%m%d')
git_push = ('git push')

repo = git.Repo('.')
print repo.git.add('*')
print repo.git.commit(m='test')
print repo.git.push()
# print repo.git.commit(m='%s') % time.strftime('%Y%m%d')

# git_commit = ('git commit -m %s') % time.strftime('%Y%m%d')

# if os.system( git_add ) != 0:
#print 'git add was wrong'

# if os.system( git_commit ) != 0:
# print 'git commit was wrong'

# if os.system( git_push ) != 0:
# print 'git push was wrong'
