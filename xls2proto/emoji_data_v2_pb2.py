# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls2proto/emoji_data_v2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls2proto/emoji_data_v2.proto',
  package='',
  serialized_pb=_b('\n\x1dxls2proto/emoji_data_v2.proto\"&\n\nemoji_data\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04icon\x18\x02 \x01(\t\".\n\x10\x65moji_data_ARRAY\x12\x1a\n\x05items\x18\x01 \x03(\x0b\x32\x0b.emoji_data')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EMOJI_DATA = _descriptor.Descriptor(
  name='emoji_data',
  full_name='emoji_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='emoji_data.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon', full_name='emoji_data.icon', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=71,
)


_EMOJI_DATA_ARRAY = _descriptor.Descriptor(
  name='emoji_data_ARRAY',
  full_name='emoji_data_ARRAY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='emoji_data_ARRAY.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=119,
)

_EMOJI_DATA_ARRAY.fields_by_name['items'].message_type = _EMOJI_DATA
DESCRIPTOR.message_types_by_name['emoji_data'] = _EMOJI_DATA
DESCRIPTOR.message_types_by_name['emoji_data_ARRAY'] = _EMOJI_DATA_ARRAY

emoji_data = _reflection.GeneratedProtocolMessageType('emoji_data', (_message.Message,), dict(
  DESCRIPTOR = _EMOJI_DATA,
  __module__ = 'xls2proto.emoji_data_v2_pb2'
  # @@protoc_insertion_point(class_scope:emoji_data)
  ))
_sym_db.RegisterMessage(emoji_data)

emoji_data_ARRAY = _reflection.GeneratedProtocolMessageType('emoji_data_ARRAY', (_message.Message,), dict(
  DESCRIPTOR = _EMOJI_DATA_ARRAY,
  __module__ = 'xls2proto.emoji_data_v2_pb2'
  # @@protoc_insertion_point(class_scope:emoji_data_ARRAY)
  ))
_sym_db.RegisterMessage(emoji_data_ARRAY)


# @@protoc_insertion_point(module_scope)
