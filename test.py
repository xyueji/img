#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

os.popen('rm -rf web && git add . && git commit -m "feat(newImg): add new image of the article" && git push -u origin master')
