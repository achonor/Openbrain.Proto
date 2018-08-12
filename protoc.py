#!usr/bin/env python
#coding=utf-8

import os
import sys

OUT_PATH_CSHARP = '../Openbrain.Client/Assets/Scripts/Protocol'
OUT_PATH_LUA = '../Openbrain.Client/Assets/Lua/Protocol'
OUT_PATH_PYTHON = '../Openbrain.Server/proto'
BASE_CMD = 'protoc -I=. --csharp_out=%s --python_out=%s'%(OUT_PATH_CSHARP, OUT_PATH_PYTHON)
LUA_BASE_CMD = 'protoc --plugin=protoc-gen-lua="lua_plugin\protoc-gen-lua.bat" --lua_out=%s'%(OUT_PATH_LUA)

def protoc(path):
    fileList = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and os.path.splitext(x)[-1]=='.proto']
    for fileName in fileList:
        cmd  = BASE_CMD + ' ' + os.path.join(path, fileName)
        lua_cmd  = LUA_BASE_CMD + ' ' + os.path.join(path, fileName)
        os.system(cmd)
        os.system(lua_cmd)
        print(cmd)
        print(lua_cmd)

if('__main__' == __name__):
    if (len(sys.argv) < 2 ):
        protoc(".")
    else:
        protoc(sys.argv[1])