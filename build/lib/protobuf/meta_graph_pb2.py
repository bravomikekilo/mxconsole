# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mxconsole/protobuf/meta_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from mxconsole.protobuf import graph_pb2 as mxconsole_dot_protobuf_dot_graph__pb2
from mxconsole.protobuf import op_def_pb2 as mxconsole_dot_protobuf_dot_op__def__pb2
from mxconsole.protobuf import tensor_shape_pb2 as mxconsole_dot_protobuf_dot_tensor__shape__pb2
from mxconsole.protobuf import types_pb2 as mxconsole_dot_protobuf_dot_types__pb2
from mxconsole.protobuf import saver_pb2 as mxconsole_dot_protobuf_dot_saver__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mxconsole/protobuf/meta_graph.proto',
  package='mxconsole',
  syntax='proto3',
  serialized_pb=_b('\n#mxconsole/protobuf/meta_graph.proto\x12\tmxconsole\x1a\x19google/protobuf/any.proto\x1a\x1emxconsole/protobuf/graph.proto\x1a\x1fmxconsole/protobuf/op_def.proto\x1a%mxconsole/protobuf/tensor_shape.proto\x1a\x1emxconsole/protobuf/types.proto\x1a\x1emxconsole/protobuf/saver.proto\"\xba\x05\n\x0cMetaGraphDef\x12:\n\rmeta_info_def\x18\x01 \x01(\x0b\x32#.mxconsole.MetaGraphDef.MetaInfoDef\x12&\n\tgraph_def\x18\x02 \x01(\x0b\x32\x13.mxconsole.GraphDef\x12&\n\tsaver_def\x18\x03 \x01(\x0b\x32\x13.mxconsole.SaverDef\x12\x42\n\x0e\x63ollection_def\x18\x04 \x03(\x0b\x32*.mxconsole.MetaGraphDef.CollectionDefEntry\x12@\n\rsignature_def\x18\x05 \x03(\x0b\x32).mxconsole.MetaGraphDef.SignatureDefEntry\x12/\n\x0e\x61sset_file_def\x18\x06 \x03(\x0b\x32\x17.mxconsole.AssetFileDef\x1a\xc8\x01\n\x0bMetaInfoDef\x12\x1a\n\x12meta_graph_version\x18\x01 \x01(\t\x12+\n\x10stripped_op_list\x18\x02 \x01(\x0b\x32\x11.mxconsole.OpList\x12&\n\x08\x61ny_info\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x1a\n\x12tensorflow_version\x18\x05 \x01(\t\x12\x1e\n\x16tensorflow_git_version\x18\x06 \x01(\t\x1aN\n\x12\x43ollectionDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.mxconsole.CollectionDef:\x02\x38\x01\x1aL\n\x11SignatureDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.mxconsole.SignatureDef:\x02\x38\x01\"\xda\x03\n\rCollectionDef\x12\x36\n\tnode_list\x18\x01 \x01(\x0b\x32!.mxconsole.CollectionDef.NodeListH\x00\x12\x38\n\nbytes_list\x18\x02 \x01(\x0b\x32\".mxconsole.CollectionDef.BytesListH\x00\x12\x38\n\nint64_list\x18\x03 \x01(\x0b\x32\".mxconsole.CollectionDef.Int64ListH\x00\x12\x38\n\nfloat_list\x18\x04 \x01(\x0b\x32\".mxconsole.CollectionDef.FloatListH\x00\x12\x34\n\x08\x61ny_list\x18\x05 \x01(\x0b\x32 .mxconsole.CollectionDef.AnyListH\x00\x1a\x19\n\x08NodeList\x12\r\n\x05value\x18\x01 \x03(\t\x1a\x1a\n\tBytesList\x12\r\n\x05value\x18\x01 \x03(\x0c\x1a\x1e\n\tInt64List\x12\x11\n\x05value\x18\x01 \x03(\x03\x42\x02\x10\x01\x1a\x1e\n\tFloatList\x12\x11\n\x05value\x18\x01 \x03(\x02\x42\x02\x10\x01\x1a.\n\x07\x41nyList\x12#\n\x05value\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\x06\n\x04kind\"q\n\nTensorInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x05\x64type\x18\x02 \x01(\x0e\x32\x13.mxconsole.DataType\x12\x31\n\x0ctensor_shape\x18\x03 \x01(\x0b\x32\x1b.mxconsole.TensorShapeProto\"\x9c\x02\n\x0cSignatureDef\x12\x33\n\x06inputs\x18\x01 \x03(\x0b\x32#.mxconsole.SignatureDef.InputsEntry\x12\x35\n\x07outputs\x18\x02 \x03(\x0b\x32$.mxconsole.SignatureDef.OutputsEntry\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x1a\x44\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.mxconsole.TensorInfo:\x02\x38\x01\x1a\x45\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.mxconsole.TensorInfo:\x02\x38\x01\"L\n\x0c\x41ssetFileDef\x12*\n\x0btensor_info\x18\x01 \x01(\x0b\x32\x15.mxconsole.TensorInfo\x12\x10\n\x08\x66ilename\x18\x02 \x01(\tB%\n\rorg.mxconsoleB\x0fMetaGraphProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_graph__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_op__def__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_tensor__shape__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_types__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_saver__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_METAGRAPHDEF_METAINFODEF = _descriptor.Descriptor(
  name='MetaInfoDef',
  full_name='mxconsole.MetaGraphDef.MetaInfoDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_graph_version', full_name='mxconsole.MetaGraphDef.MetaInfoDef.meta_graph_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stripped_op_list', full_name='mxconsole.MetaGraphDef.MetaInfoDef.stripped_op_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any_info', full_name='mxconsole.MetaGraphDef.MetaInfoDef.any_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='mxconsole.MetaGraphDef.MetaInfoDef.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensorflow_version', full_name='mxconsole.MetaGraphDef.MetaInfoDef.tensorflow_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensorflow_git_version', full_name='mxconsole.MetaGraphDef.MetaInfoDef.tensorflow_git_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=786,
)

_METAGRAPHDEF_COLLECTIONDEFENTRY = _descriptor.Descriptor(
  name='CollectionDefEntry',
  full_name='mxconsole.MetaGraphDef.CollectionDefEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mxconsole.MetaGraphDef.CollectionDefEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.MetaGraphDef.CollectionDefEntry.value', index=1,
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
  serialized_start=788,
  serialized_end=866,
)

_METAGRAPHDEF_SIGNATUREDEFENTRY = _descriptor.Descriptor(
  name='SignatureDefEntry',
  full_name='mxconsole.MetaGraphDef.SignatureDefEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mxconsole.MetaGraphDef.SignatureDefEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.MetaGraphDef.SignatureDefEntry.value', index=1,
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
  serialized_start=868,
  serialized_end=944,
)

_METAGRAPHDEF = _descriptor.Descriptor(
  name='MetaGraphDef',
  full_name='mxconsole.MetaGraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_info_def', full_name='mxconsole.MetaGraphDef.meta_info_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph_def', full_name='mxconsole.MetaGraphDef.graph_def', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='saver_def', full_name='mxconsole.MetaGraphDef.saver_def', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collection_def', full_name='mxconsole.MetaGraphDef.collection_def', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature_def', full_name='mxconsole.MetaGraphDef.signature_def', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_file_def', full_name='mxconsole.MetaGraphDef.asset_file_def', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_METAGRAPHDEF_METAINFODEF, _METAGRAPHDEF_COLLECTIONDEFENTRY, _METAGRAPHDEF_SIGNATUREDEFENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=944,
)


_COLLECTIONDEF_NODELIST = _descriptor.Descriptor(
  name='NodeList',
  full_name='mxconsole.CollectionDef.NodeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.CollectionDef.NodeList.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1248,
  serialized_end=1273,
)

_COLLECTIONDEF_BYTESLIST = _descriptor.Descriptor(
  name='BytesList',
  full_name='mxconsole.CollectionDef.BytesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.CollectionDef.BytesList.value', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1275,
  serialized_end=1301,
)

_COLLECTIONDEF_INT64LIST = _descriptor.Descriptor(
  name='Int64List',
  full_name='mxconsole.CollectionDef.Int64List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.CollectionDef.Int64List.value', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1303,
  serialized_end=1333,
)

_COLLECTIONDEF_FLOATLIST = _descriptor.Descriptor(
  name='FloatList',
  full_name='mxconsole.CollectionDef.FloatList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.CollectionDef.FloatList.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1335,
  serialized_end=1365,
)

_COLLECTIONDEF_ANYLIST = _descriptor.Descriptor(
  name='AnyList',
  full_name='mxconsole.CollectionDef.AnyList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.CollectionDef.AnyList.value', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1367,
  serialized_end=1413,
)

_COLLECTIONDEF = _descriptor.Descriptor(
  name='CollectionDef',
  full_name='mxconsole.CollectionDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_list', full_name='mxconsole.CollectionDef.node_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_list', full_name='mxconsole.CollectionDef.bytes_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_list', full_name='mxconsole.CollectionDef.int64_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_list', full_name='mxconsole.CollectionDef.float_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any_list', full_name='mxconsole.CollectionDef.any_list', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTIONDEF_NODELIST, _COLLECTIONDEF_BYTESLIST, _COLLECTIONDEF_INT64LIST, _COLLECTIONDEF_FLOATLIST, _COLLECTIONDEF_ANYLIST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='mxconsole.CollectionDef.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=947,
  serialized_end=1421,
)


_TENSORINFO = _descriptor.Descriptor(
  name='TensorInfo',
  full_name='mxconsole.TensorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mxconsole.TensorInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='mxconsole.TensorInfo.dtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='mxconsole.TensorInfo.tensor_shape', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1423,
  serialized_end=1536,
)


_SIGNATUREDEF_INPUTSENTRY = _descriptor.Descriptor(
  name='InputsEntry',
  full_name='mxconsole.SignatureDef.InputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mxconsole.SignatureDef.InputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.SignatureDef.InputsEntry.value', index=1,
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
  serialized_start=1684,
  serialized_end=1752,
)

_SIGNATUREDEF_OUTPUTSENTRY = _descriptor.Descriptor(
  name='OutputsEntry',
  full_name='mxconsole.SignatureDef.OutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mxconsole.SignatureDef.OutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.SignatureDef.OutputsEntry.value', index=1,
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
  serialized_start=1754,
  serialized_end=1823,
)

_SIGNATUREDEF = _descriptor.Descriptor(
  name='SignatureDef',
  full_name='mxconsole.SignatureDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='mxconsole.SignatureDef.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='mxconsole.SignatureDef.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='mxconsole.SignatureDef.method_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREDEF_INPUTSENTRY, _SIGNATUREDEF_OUTPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1539,
  serialized_end=1823,
)


_ASSETFILEDEF = _descriptor.Descriptor(
  name='AssetFileDef',
  full_name='mxconsole.AssetFileDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_info', full_name='mxconsole.AssetFileDef.tensor_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='mxconsole.AssetFileDef.filename', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1825,
  serialized_end=1901,
)

_METAGRAPHDEF_METAINFODEF.fields_by_name['stripped_op_list'].message_type = mxconsole_dot_protobuf_dot_op__def__pb2._OPLIST
_METAGRAPHDEF_METAINFODEF.fields_by_name['any_info'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_METAGRAPHDEF_METAINFODEF.containing_type = _METAGRAPHDEF
_METAGRAPHDEF_COLLECTIONDEFENTRY.fields_by_name['value'].message_type = _COLLECTIONDEF
_METAGRAPHDEF_COLLECTIONDEFENTRY.containing_type = _METAGRAPHDEF
_METAGRAPHDEF_SIGNATUREDEFENTRY.fields_by_name['value'].message_type = _SIGNATUREDEF
_METAGRAPHDEF_SIGNATUREDEFENTRY.containing_type = _METAGRAPHDEF
_METAGRAPHDEF.fields_by_name['meta_info_def'].message_type = _METAGRAPHDEF_METAINFODEF
_METAGRAPHDEF.fields_by_name['graph_def'].message_type = mxconsole_dot_protobuf_dot_graph__pb2._GRAPHDEF
_METAGRAPHDEF.fields_by_name['saver_def'].message_type = mxconsole_dot_protobuf_dot_saver__pb2._SAVERDEF
_METAGRAPHDEF.fields_by_name['collection_def'].message_type = _METAGRAPHDEF_COLLECTIONDEFENTRY
_METAGRAPHDEF.fields_by_name['signature_def'].message_type = _METAGRAPHDEF_SIGNATUREDEFENTRY
_METAGRAPHDEF.fields_by_name['asset_file_def'].message_type = _ASSETFILEDEF
_COLLECTIONDEF_NODELIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_BYTESLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_INT64LIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_FLOATLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_ANYLIST.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_COLLECTIONDEF_ANYLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF.fields_by_name['node_list'].message_type = _COLLECTIONDEF_NODELIST
_COLLECTIONDEF.fields_by_name['bytes_list'].message_type = _COLLECTIONDEF_BYTESLIST
_COLLECTIONDEF.fields_by_name['int64_list'].message_type = _COLLECTIONDEF_INT64LIST
_COLLECTIONDEF.fields_by_name['float_list'].message_type = _COLLECTIONDEF_FLOATLIST
_COLLECTIONDEF.fields_by_name['any_list'].message_type = _COLLECTIONDEF_ANYLIST
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['node_list'])
_COLLECTIONDEF.fields_by_name['node_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['bytes_list'])
_COLLECTIONDEF.fields_by_name['bytes_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['int64_list'])
_COLLECTIONDEF.fields_by_name['int64_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['float_list'])
_COLLECTIONDEF.fields_by_name['float_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['any_list'])
_COLLECTIONDEF.fields_by_name['any_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_TENSORINFO.fields_by_name['dtype'].enum_type = mxconsole_dot_protobuf_dot_types__pb2._DATATYPE
_TENSORINFO.fields_by_name['tensor_shape'].message_type = mxconsole_dot_protobuf_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_SIGNATUREDEF_INPUTSENTRY.fields_by_name['value'].message_type = _TENSORINFO
_SIGNATUREDEF_INPUTSENTRY.containing_type = _SIGNATUREDEF
_SIGNATUREDEF_OUTPUTSENTRY.fields_by_name['value'].message_type = _TENSORINFO
_SIGNATUREDEF_OUTPUTSENTRY.containing_type = _SIGNATUREDEF
_SIGNATUREDEF.fields_by_name['inputs'].message_type = _SIGNATUREDEF_INPUTSENTRY
_SIGNATUREDEF.fields_by_name['outputs'].message_type = _SIGNATUREDEF_OUTPUTSENTRY
_ASSETFILEDEF.fields_by_name['tensor_info'].message_type = _TENSORINFO
DESCRIPTOR.message_types_by_name['MetaGraphDef'] = _METAGRAPHDEF
DESCRIPTOR.message_types_by_name['CollectionDef'] = _COLLECTIONDEF
DESCRIPTOR.message_types_by_name['TensorInfo'] = _TENSORINFO
DESCRIPTOR.message_types_by_name['SignatureDef'] = _SIGNATUREDEF
DESCRIPTOR.message_types_by_name['AssetFileDef'] = _ASSETFILEDEF

MetaGraphDef = _reflection.GeneratedProtocolMessageType('MetaGraphDef', (_message.Message,), dict(

  MetaInfoDef = _reflection.GeneratedProtocolMessageType('MetaInfoDef', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_METAINFODEF,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.MetaGraphDef.MetaInfoDef)
    ))
  ,

  CollectionDefEntry = _reflection.GeneratedProtocolMessageType('CollectionDefEntry', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_COLLECTIONDEFENTRY,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.MetaGraphDef.CollectionDefEntry)
    ))
  ,

  SignatureDefEntry = _reflection.GeneratedProtocolMessageType('SignatureDefEntry', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_SIGNATUREDEFENTRY,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.MetaGraphDef.SignatureDefEntry)
    ))
  ,
  DESCRIPTOR = _METAGRAPHDEF,
  __module__ = 'mxconsole.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.MetaGraphDef)
  ))
_sym_db.RegisterMessage(MetaGraphDef)
_sym_db.RegisterMessage(MetaGraphDef.MetaInfoDef)
_sym_db.RegisterMessage(MetaGraphDef.CollectionDefEntry)
_sym_db.RegisterMessage(MetaGraphDef.SignatureDefEntry)

CollectionDef = _reflection.GeneratedProtocolMessageType('CollectionDef', (_message.Message,), dict(

  NodeList = _reflection.GeneratedProtocolMessageType('NodeList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_NODELIST,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.CollectionDef.NodeList)
    ))
  ,

  BytesList = _reflection.GeneratedProtocolMessageType('BytesList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_BYTESLIST,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.CollectionDef.BytesList)
    ))
  ,

  Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_INT64LIST,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.CollectionDef.Int64List)
    ))
  ,

  FloatList = _reflection.GeneratedProtocolMessageType('FloatList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_FLOATLIST,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.CollectionDef.FloatList)
    ))
  ,

  AnyList = _reflection.GeneratedProtocolMessageType('AnyList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_ANYLIST,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.CollectionDef.AnyList)
    ))
  ,
  DESCRIPTOR = _COLLECTIONDEF,
  __module__ = 'mxconsole.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.CollectionDef)
  ))
_sym_db.RegisterMessage(CollectionDef)
_sym_db.RegisterMessage(CollectionDef.NodeList)
_sym_db.RegisterMessage(CollectionDef.BytesList)
_sym_db.RegisterMessage(CollectionDef.Int64List)
_sym_db.RegisterMessage(CollectionDef.FloatList)
_sym_db.RegisterMessage(CollectionDef.AnyList)

TensorInfo = _reflection.GeneratedProtocolMessageType('TensorInfo', (_message.Message,), dict(
  DESCRIPTOR = _TENSORINFO,
  __module__ = 'mxconsole.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.TensorInfo)
  ))
_sym_db.RegisterMessage(TensorInfo)

SignatureDef = _reflection.GeneratedProtocolMessageType('SignatureDef', (_message.Message,), dict(

  InputsEntry = _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREDEF_INPUTSENTRY,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.SignatureDef.InputsEntry)
    ))
  ,

  OutputsEntry = _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREDEF_OUTPUTSENTRY,
    __module__ = 'mxconsole.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.SignatureDef.OutputsEntry)
    ))
  ,
  DESCRIPTOR = _SIGNATUREDEF,
  __module__ = 'mxconsole.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.SignatureDef)
  ))
_sym_db.RegisterMessage(SignatureDef)
_sym_db.RegisterMessage(SignatureDef.InputsEntry)
_sym_db.RegisterMessage(SignatureDef.OutputsEntry)

AssetFileDef = _reflection.GeneratedProtocolMessageType('AssetFileDef', (_message.Message,), dict(
  DESCRIPTOR = _ASSETFILEDEF,
  __module__ = 'mxconsole.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.AssetFileDef)
  ))
_sym_db.RegisterMessage(AssetFileDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\rorg.mxconsoleB\017MetaGraphProtosP\001\370\001\001'))
_METAGRAPHDEF_COLLECTIONDEFENTRY.has_options = True
_METAGRAPHDEF_COLLECTIONDEFENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_METAGRAPHDEF_SIGNATUREDEFENTRY.has_options = True
_METAGRAPHDEF_SIGNATUREDEFENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_COLLECTIONDEF_INT64LIST.fields_by_name['value'].has_options = True
_COLLECTIONDEF_INT64LIST.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_COLLECTIONDEF_FLOATLIST.fields_by_name['value'].has_options = True
_COLLECTIONDEF_FLOATLIST.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SIGNATUREDEF_INPUTSENTRY.has_options = True
_SIGNATUREDEF_INPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SIGNATUREDEF_OUTPUTSENTRY.has_options = True
_SIGNATUREDEF_OUTPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)