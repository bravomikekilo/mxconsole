# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mxconsole/protobuf/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mxconsole.protobuf import cost_graph_pb2 as mxconsole_dot_protobuf_dot_cost__graph__pb2
from mxconsole.protobuf import graph_pb2 as mxconsole_dot_protobuf_dot_graph__pb2
from mxconsole.protobuf import step_stats_pb2 as mxconsole_dot_protobuf_dot_step__stats__pb2
from mxconsole.protobuf import debug_pb2 as mxconsole_dot_protobuf_dot_debug__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mxconsole/protobuf/config.proto',
  package='mxconsole',
  syntax='proto3',
  serialized_pb=_b('\n\x1fmxconsole/protobuf/config.proto\x12\tmxconsole\x1a#mxconsole/protobuf/cost_graph.proto\x1a\x1emxconsole/protobuf/graph.proto\x1a#mxconsole/protobuf/step_stats.proto\x1a\x1emxconsole/protobuf/debug.proto\"\xeb\x01\n\nGPUOptions\x12\'\n\x1fper_process_gpu_memory_fraction\x18\x01 \x01(\x01\x12\x16\n\x0e\x61llocator_type\x18\x02 \x01(\t\x12\x1f\n\x17\x64\x65\x66\x65rred_deletion_bytes\x18\x03 \x01(\x03\x12\x14\n\x0c\x61llow_growth\x18\x04 \x01(\x08\x12\x1b\n\x13visible_device_list\x18\x05 \x01(\t\x12\"\n\x1apolling_active_delay_usecs\x18\x06 \x01(\x05\x12$\n\x1cpolling_inactive_delay_msecs\x18\x07 \x01(\x05\"\xdd\x02\n\x10OptimizerOptions\x12+\n#do_common_subexpression_elimination\x18\x01 \x01(\x08\x12\x1b\n\x13\x64o_constant_folding\x18\x02 \x01(\x08\x12\x1c\n\x14\x64o_function_inlining\x18\x04 \x01(\x08\x12\x34\n\topt_level\x18\x03 \x01(\x0e\x32!.mxconsole.OptimizerOptions.Level\x12\x44\n\x10global_jit_level\x18\x05 \x01(\x0e\x32*.mxconsole.OptimizerOptions.GlobalJitLevel\" \n\x05Level\x12\x06\n\x02L1\x10\x00\x12\x0f\n\x02L0\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\"C\n\x0eGlobalJitLevel\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x10\n\x03OFF\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x08\n\x04ON_1\x10\x01\x12\x08\n\x04ON_2\x10\x02\"\xb8\x02\n\x0cGraphOptions\x12\x1e\n\x16\x65nable_recv_scheduling\x18\x02 \x01(\x08\x12\x36\n\x11optimizer_options\x18\x03 \x01(\x0b\x32\x1b.mxconsole.OptimizerOptions\x12\x18\n\x10\x62uild_cost_model\x18\x04 \x01(\x03\x12\x1e\n\x16\x62uild_cost_model_after\x18\t \x01(\x03\x12\x14\n\x0cinfer_shapes\x18\x05 \x01(\x08\x12\x1a\n\x12place_pruned_graph\x18\x06 \x01(\x08\x12 \n\x18\x65nable_bfloat16_sendrecv\x18\x07 \x01(\x08\x12\x15\n\rtimeline_step\x18\x08 \x01(\x05J\x04\x08\x01\x10\x02R%skip_common_subexpression_elimination\",\n\x15ThreadPoolOptionProto\x12\x13\n\x0bnum_threads\x18\x01 \x01(\x05\"2\n\nRPCOptions\x12$\n\x1cuse_rpc_for_inprocess_master\x18\x01 \x01(\x08\"\xcc\x04\n\x0b\x43onfigProto\x12=\n\x0c\x64\x65vice_count\x18\x01 \x03(\x0b\x32\'.mxconsole.ConfigProto.DeviceCountEntry\x12$\n\x1cintra_op_parallelism_threads\x18\x02 \x01(\x05\x12$\n\x1cinter_op_parallelism_threads\x18\x05 \x01(\x05\x12\x1f\n\x17use_per_session_threads\x18\t \x01(\x08\x12\x46\n\x1csession_inter_op_thread_pool\x18\x0c \x03(\x0b\x32 .mxconsole.ThreadPoolOptionProto\x12\x18\n\x10placement_period\x18\x03 \x01(\x05\x12\x16\n\x0e\x64\x65vice_filters\x18\x04 \x03(\t\x12*\n\x0bgpu_options\x18\x06 \x01(\x0b\x32\x15.mxconsole.GPUOptions\x12\x1c\n\x14\x61llow_soft_placement\x18\x07 \x01(\x08\x12\x1c\n\x14log_device_placement\x18\x08 \x01(\x08\x12.\n\rgraph_options\x18\n \x01(\x0b\x32\x17.mxconsole.GraphOptions\x12\x1f\n\x17operation_timeout_in_ms\x18\x0b \x01(\x03\x12*\n\x0brpc_options\x18\r \x01(\x0b\x32\x15.mxconsole.RPCOptions\x1a\x32\n\x10\x44\x65viceCountEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\xa3\x02\n\nRunOptions\x12\x35\n\x0btrace_level\x18\x01 \x01(\x0e\x32 .mxconsole.RunOptions.TraceLevel\x12\x15\n\rtimeout_in_ms\x18\x02 \x01(\x03\x12\x1c\n\x14inter_op_thread_pool\x18\x03 \x01(\x05\x12\x1f\n\x17output_partition_graphs\x18\x05 \x01(\x08\x12.\n\rdebug_options\x18\x06 \x01(\x0b\x32\x17.mxconsole.DebugOptions\"R\n\nTraceLevel\x12\x0c\n\x08NO_TRACE\x10\x00\x12\x12\n\x0eSOFTWARE_TRACE\x10\x01\x12\x12\n\x0eHARDWARE_TRACE\x10\x02\x12\x0e\n\nFULL_TRACE\x10\x03J\x04\x08\x04\x10\x05\"\x93\x01\n\x0bRunMetadata\x12(\n\nstep_stats\x18\x01 \x01(\x0b\x32\x14.mxconsole.StepStats\x12+\n\ncost_graph\x18\x02 \x01(\x0b\x32\x17.mxconsole.CostGraphDef\x12-\n\x10partition_graphs\x18\x03 \x03(\x0b\x32\x13.mxconsole.GraphDefB\"\n\rorg.mxconsoleB\x0c\x43onfigProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[mxconsole_dot_protobuf_dot_cost__graph__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_graph__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_step__stats__pb2.DESCRIPTOR,mxconsole_dot_protobuf_dot_debug__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OPTIMIZEROPTIONS_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='mxconsole.OptimizerOptions.Level',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='L1', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L0', index=1, number=-1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=671,
  serialized_end=703,
)
_sym_db.RegisterEnumDescriptor(_OPTIMIZEROPTIONS_LEVEL)

_OPTIMIZEROPTIONS_GLOBALJITLEVEL = _descriptor.EnumDescriptor(
  name='GlobalJitLevel',
  full_name='mxconsole.OptimizerOptions.GlobalJitLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=1, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_1', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_2', index=3, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=705,
  serialized_end=772,
)
_sym_db.RegisterEnumDescriptor(_OPTIMIZEROPTIONS_GLOBALJITLEVEL)

_RUNOPTIONS_TRACELEVEL = _descriptor.EnumDescriptor(
  name='TraceLevel',
  full_name='mxconsole.RunOptions.TraceLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_TRACE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTWARE_TRACE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HARDWARE_TRACE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_TRACE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1982,
  serialized_end=2064,
)
_sym_db.RegisterEnumDescriptor(_RUNOPTIONS_TRACELEVEL)


_GPUOPTIONS = _descriptor.Descriptor(
  name='GPUOptions',
  full_name='mxconsole.GPUOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='per_process_gpu_memory_fraction', full_name='mxconsole.GPUOptions.per_process_gpu_memory_fraction', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocator_type', full_name='mxconsole.GPUOptions.allocator_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deferred_deletion_bytes', full_name='mxconsole.GPUOptions.deferred_deletion_bytes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_growth', full_name='mxconsole.GPUOptions.allow_growth', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible_device_list', full_name='mxconsole.GPUOptions.visible_device_list', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polling_active_delay_usecs', full_name='mxconsole.GPUOptions.polling_active_delay_usecs', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polling_inactive_delay_msecs', full_name='mxconsole.GPUOptions.polling_inactive_delay_msecs', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=185,
  serialized_end=420,
)


_OPTIMIZEROPTIONS = _descriptor.Descriptor(
  name='OptimizerOptions',
  full_name='mxconsole.OptimizerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='do_common_subexpression_elimination', full_name='mxconsole.OptimizerOptions.do_common_subexpression_elimination', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='do_constant_folding', full_name='mxconsole.OptimizerOptions.do_constant_folding', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='do_function_inlining', full_name='mxconsole.OptimizerOptions.do_function_inlining', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opt_level', full_name='mxconsole.OptimizerOptions.opt_level', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='global_jit_level', full_name='mxconsole.OptimizerOptions.global_jit_level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPTIMIZEROPTIONS_LEVEL,
    _OPTIMIZEROPTIONS_GLOBALJITLEVEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=772,
)


_GRAPHOPTIONS = _descriptor.Descriptor(
  name='GraphOptions',
  full_name='mxconsole.GraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_recv_scheduling', full_name='mxconsole.GraphOptions.enable_recv_scheduling', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optimizer_options', full_name='mxconsole.GraphOptions.optimizer_options', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_cost_model', full_name='mxconsole.GraphOptions.build_cost_model', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_cost_model_after', full_name='mxconsole.GraphOptions.build_cost_model_after', index=3,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='infer_shapes', full_name='mxconsole.GraphOptions.infer_shapes', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='place_pruned_graph', full_name='mxconsole.GraphOptions.place_pruned_graph', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable_bfloat16_sendrecv', full_name='mxconsole.GraphOptions.enable_bfloat16_sendrecv', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeline_step', full_name='mxconsole.GraphOptions.timeline_step', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=775,
  serialized_end=1087,
)


_THREADPOOLOPTIONPROTO = _descriptor.Descriptor(
  name='ThreadPoolOptionProto',
  full_name='mxconsole.ThreadPoolOptionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_threads', full_name='mxconsole.ThreadPoolOptionProto.num_threads', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1089,
  serialized_end=1133,
)


_RPCOPTIONS = _descriptor.Descriptor(
  name='RPCOptions',
  full_name='mxconsole.RPCOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_rpc_for_inprocess_master', full_name='mxconsole.RPCOptions.use_rpc_for_inprocess_master', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1135,
  serialized_end=1185,
)


_CONFIGPROTO_DEVICECOUNTENTRY = _descriptor.Descriptor(
  name='DeviceCountEntry',
  full_name='mxconsole.ConfigProto.DeviceCountEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mxconsole.ConfigProto.DeviceCountEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mxconsole.ConfigProto.DeviceCountEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1726,
  serialized_end=1776,
)

_CONFIGPROTO = _descriptor.Descriptor(
  name='ConfigProto',
  full_name='mxconsole.ConfigProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_count', full_name='mxconsole.ConfigProto.device_count', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intra_op_parallelism_threads', full_name='mxconsole.ConfigProto.intra_op_parallelism_threads', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inter_op_parallelism_threads', full_name='mxconsole.ConfigProto.inter_op_parallelism_threads', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_per_session_threads', full_name='mxconsole.ConfigProto.use_per_session_threads', index=3,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_inter_op_thread_pool', full_name='mxconsole.ConfigProto.session_inter_op_thread_pool', index=4,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='placement_period', full_name='mxconsole.ConfigProto.placement_period', index=5,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_filters', full_name='mxconsole.ConfigProto.device_filters', index=6,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu_options', full_name='mxconsole.ConfigProto.gpu_options', index=7,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_soft_placement', full_name='mxconsole.ConfigProto.allow_soft_placement', index=8,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_device_placement', full_name='mxconsole.ConfigProto.log_device_placement', index=9,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph_options', full_name='mxconsole.ConfigProto.graph_options', index=10,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation_timeout_in_ms', full_name='mxconsole.ConfigProto.operation_timeout_in_ms', index=11,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpc_options', full_name='mxconsole.ConfigProto.rpc_options', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGPROTO_DEVICECOUNTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1188,
  serialized_end=1776,
)


_RUNOPTIONS = _descriptor.Descriptor(
  name='RunOptions',
  full_name='mxconsole.RunOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_level', full_name='mxconsole.RunOptions.trace_level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout_in_ms', full_name='mxconsole.RunOptions.timeout_in_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inter_op_thread_pool', full_name='mxconsole.RunOptions.inter_op_thread_pool', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_partition_graphs', full_name='mxconsole.RunOptions.output_partition_graphs', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug_options', full_name='mxconsole.RunOptions.debug_options', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RUNOPTIONS_TRACELEVEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1779,
  serialized_end=2070,
)


_RUNMETADATA = _descriptor.Descriptor(
  name='RunMetadata',
  full_name='mxconsole.RunMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_stats', full_name='mxconsole.RunMetadata.step_stats', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost_graph', full_name='mxconsole.RunMetadata.cost_graph', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partition_graphs', full_name='mxconsole.RunMetadata.partition_graphs', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=2073,
  serialized_end=2220,
)

_OPTIMIZEROPTIONS.fields_by_name['opt_level'].enum_type = _OPTIMIZEROPTIONS_LEVEL
_OPTIMIZEROPTIONS.fields_by_name['global_jit_level'].enum_type = _OPTIMIZEROPTIONS_GLOBALJITLEVEL
_OPTIMIZEROPTIONS_LEVEL.containing_type = _OPTIMIZEROPTIONS
_OPTIMIZEROPTIONS_GLOBALJITLEVEL.containing_type = _OPTIMIZEROPTIONS
_GRAPHOPTIONS.fields_by_name['optimizer_options'].message_type = _OPTIMIZEROPTIONS
_CONFIGPROTO_DEVICECOUNTENTRY.containing_type = _CONFIGPROTO
_CONFIGPROTO.fields_by_name['device_count'].message_type = _CONFIGPROTO_DEVICECOUNTENTRY
_CONFIGPROTO.fields_by_name['session_inter_op_thread_pool'].message_type = _THREADPOOLOPTIONPROTO
_CONFIGPROTO.fields_by_name['gpu_options'].message_type = _GPUOPTIONS
_CONFIGPROTO.fields_by_name['graph_options'].message_type = _GRAPHOPTIONS
_CONFIGPROTO.fields_by_name['rpc_options'].message_type = _RPCOPTIONS
_RUNOPTIONS.fields_by_name['trace_level'].enum_type = _RUNOPTIONS_TRACELEVEL
_RUNOPTIONS.fields_by_name['debug_options'].message_type = mxconsole_dot_protobuf_dot_debug__pb2._DEBUGOPTIONS
_RUNOPTIONS_TRACELEVEL.containing_type = _RUNOPTIONS
_RUNMETADATA.fields_by_name['step_stats'].message_type = mxconsole_dot_protobuf_dot_step__stats__pb2._STEPSTATS
_RUNMETADATA.fields_by_name['cost_graph'].message_type = mxconsole_dot_protobuf_dot_cost__graph__pb2._COSTGRAPHDEF
_RUNMETADATA.fields_by_name['partition_graphs'].message_type = mxconsole_dot_protobuf_dot_graph__pb2._GRAPHDEF
DESCRIPTOR.message_types_by_name['GPUOptions'] = _GPUOPTIONS
DESCRIPTOR.message_types_by_name['OptimizerOptions'] = _OPTIMIZEROPTIONS
DESCRIPTOR.message_types_by_name['GraphOptions'] = _GRAPHOPTIONS
DESCRIPTOR.message_types_by_name['ThreadPoolOptionProto'] = _THREADPOOLOPTIONPROTO
DESCRIPTOR.message_types_by_name['RPCOptions'] = _RPCOPTIONS
DESCRIPTOR.message_types_by_name['ConfigProto'] = _CONFIGPROTO
DESCRIPTOR.message_types_by_name['RunOptions'] = _RUNOPTIONS
DESCRIPTOR.message_types_by_name['RunMetadata'] = _RUNMETADATA

GPUOptions = _reflection.GeneratedProtocolMessageType('GPUOptions', (_message.Message,), dict(
  DESCRIPTOR = _GPUOPTIONS,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.GPUOptions)
  ))
_sym_db.RegisterMessage(GPUOptions)

OptimizerOptions = _reflection.GeneratedProtocolMessageType('OptimizerOptions', (_message.Message,), dict(
  DESCRIPTOR = _OPTIMIZEROPTIONS,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.OptimizerOptions)
  ))
_sym_db.RegisterMessage(OptimizerOptions)

GraphOptions = _reflection.GeneratedProtocolMessageType('GraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHOPTIONS,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.GraphOptions)
  ))
_sym_db.RegisterMessage(GraphOptions)

ThreadPoolOptionProto = _reflection.GeneratedProtocolMessageType('ThreadPoolOptionProto', (_message.Message,), dict(
  DESCRIPTOR = _THREADPOOLOPTIONPROTO,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.ThreadPoolOptionProto)
  ))
_sym_db.RegisterMessage(ThreadPoolOptionProto)

RPCOptions = _reflection.GeneratedProtocolMessageType('RPCOptions', (_message.Message,), dict(
  DESCRIPTOR = _RPCOPTIONS,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.RPCOptions)
  ))
_sym_db.RegisterMessage(RPCOptions)

ConfigProto = _reflection.GeneratedProtocolMessageType('ConfigProto', (_message.Message,), dict(

  DeviceCountEntry = _reflection.GeneratedProtocolMessageType('DeviceCountEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGPROTO_DEVICECOUNTENTRY,
    __module__ = 'mxconsole.protobuf.config_pb2'
    # @@protoc_insertion_point(class_scope:mxconsole.ConfigProto.DeviceCountEntry)
    ))
  ,
  DESCRIPTOR = _CONFIGPROTO,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.ConfigProto)
  ))
_sym_db.RegisterMessage(ConfigProto)
_sym_db.RegisterMessage(ConfigProto.DeviceCountEntry)

RunOptions = _reflection.GeneratedProtocolMessageType('RunOptions', (_message.Message,), dict(
  DESCRIPTOR = _RUNOPTIONS,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.RunOptions)
  ))
_sym_db.RegisterMessage(RunOptions)

RunMetadata = _reflection.GeneratedProtocolMessageType('RunMetadata', (_message.Message,), dict(
  DESCRIPTOR = _RUNMETADATA,
  __module__ = 'mxconsole.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:mxconsole.RunMetadata)
  ))
_sym_db.RegisterMessage(RunMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\rorg.mxconsoleB\014ConfigProtosP\001\370\001\001'))
_CONFIGPROTO_DEVICECOUNTENTRY.has_options = True
_CONFIGPROTO_DEVICECOUNTENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
