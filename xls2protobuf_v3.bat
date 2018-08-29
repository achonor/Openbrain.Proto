python xls2protobuf_v3.py xls
python2 xls2protobuf_v2.py xls
python copyfile.py xls2bin ../Openbrain.Client/Assets/StreamingAssets/Android/DataConfig
python copyfile.py xls2bin ../Openbrain.Client/Assets/StreamingAssets/iOS/DataConfig
python copyfile.py xls2bin ../Openbrain.Server/DataConfig
python protoc.py xls2proto/
pause