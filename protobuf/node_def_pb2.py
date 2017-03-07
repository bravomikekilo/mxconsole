# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mxconsole/protobuf/node_def.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mxconsole.protobuf import attr_value_pb2 as mxconsole_dot_protobuf_dot_attr__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mxconsole/protobuf/node_def.proto',
  package='mxconsole',
  syntax='proto3',
  serialized_pb=_b('\n!mxconsole/protobuf/node_def.proto\x12\tmxconsole\x1a#mxconsole/protobuf/attr_value.proto\"\xb1\x01\n\x07NodeDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12\r\n\x05input\x18\x03 \x03(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12*\n\x04\x61ttr\x18\x05 \x03(\x0b\x32\x1c.mxconsole.NodeDef.AttrEntry\x1a\x41\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.mxconsole.AttrValue:\x02\x38\x01\x42\x1f\n\rorg.mxconsoleB\tNodeProtoP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[mxconsole_dot_protobuf_dot_attr__value__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NODEDEF_ATTRENTRY = _descriptor.Descriptor(
  name='AttrEntry',
  full_name='mxconsole.NodeDef.AttrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mxconsole.NodeDef.AttrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.NodeDef.AttrEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=263,
)

_NODEDEF = _descriptor.Descriptor(
  name='NodeDef',
  full_name='mxconsole.NodeDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mxconsole.NodeDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op', full_name='mxconsole.NodeDef.op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input', full_name='mxconsole.NodeDef.input', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='mxconsole.NodeDef.device', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr', full_name='mxconsole.NodeDef.attr', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NODEDEF_ATTRENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=263,
)

_NODEDEF_ATTRENTRY.fields_by_name['value'].message_type = mxconsole_dot_protobuf_dot_attr__value__pb2._ATTRVALUE
_NODEDEF_ATTRENTRY.containing_type = _NODEDEF
_NODEDEF.fields_by_name['attr'].message_type = _NODEDEF_ATTRENTRY
DESCRIPTOR.message_types_by_name['NodeDef'] = _NODEDEF

NodeDef = _reflection.GeneratedProtocolMessageType('NodeDef', (_message.Message,), dict(

  AttrEntry = _reflection.GeneratedProtocolMessageType('AttrEntry', (_message.Message,), dict(
    DESCRIPTOR = _NODEDEF_ATTRENTRY,
    __module__ = 'mxconsole.protobuf.node_def_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.NodeDef.AttrEntry)
    ))
  ,
  DESCRIPTOR = _NODEDEF,
  __module__ = 'mxconsole.protobuf.node_def_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.NodeDef)
  ))
_sym_db.RegisterMessage(NodeDef)
_sym_db.RegisterMessage(NodeDef.AttrEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\rorg.mxconsoleB\tNodeProtoP\001\370\001\001'))
_NODEDEF_ATTRENTRY.has_options = True
_NODEDEF_ATTRENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
