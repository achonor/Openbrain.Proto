python xls2protobuf_v3.py xls
python copyfile.py xls2bin ../Openbrain.Client/Assets/StreamingAssets/DataConfig
python copyfile.py xls2bin ../Openbrain.Server/DataConfig
python protoc.py xls2proto/
pause