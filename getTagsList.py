#!/usr/bin/python
# -*- coding: UTF-8 -*-

# todo: if not selectedDbUUID，显示所有 tags
# 多个 tag 匹配

import os
import json
import ast
import shlex
import subprocess

selectedDbUUID = os.getenv('selectedDbUUID', "")

if selectedDbUUID:
    cmdScript = "osascript -e 'tell application \"DEVONthink\" to get name of tag group of (get database with uuid \"{}\")' -s s".format(selectedDbUUID)
else:
    cmdScript = "osascript -e 'tell application \"DEVONthink\" to get name of every tag group' -s s"

proc = subprocess.Popen(cmdScript, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
cmdResult = proc.stdout.read()
tagList = ast.literal_eval(
    "[" + cmdResult[1:-2].decode("UTF8") + "]")

result = {"items": []}
for tag in tagList:
    result["items"].append({
        "title": tag,
        "subtitle": "Press Enter to list all files with this tag",
        # "arg": tag,
        "variables": {"selectedTag": tag, "selectedDbUUID": selectedDbUUID}
    })

if result['items']:
    print(json.dumps(result))
else:
    # when result list is empty
    print('{"items": [{"title": "None Tag","subtitle": "(*´･д･)?"}]}')
