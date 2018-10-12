# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0emessages.proto\"\xdb\x01\n\x0cUpdateSignal\x12\r\n\x05\x42SSID\x18\x01 \x01(\x06\x12+\n\nstaresults\x18\x02 \x03(\x0b\x32\x17.UpdateSignal.StaResult\x1a\x8e\x01\n\tStaResult\x12\x0e\n\x06StaMAC\x18\x01 \x01(\x06\x12\x41\n\x10linkmeasurements\x18\x02 \x03(\x0b\x32\'.UpdateSignal.StaResult.LinkMeasurement\x1a.\n\x0fLinkMeasurement\x12\r\n\x05\x42SSID\x18\x01 \x01(\x06\x12\x0c\n\x04rssi\x18\x02 \x01(\x11\x62\x06proto3')
)




_UPDATESIGNAL_STARESULT_LINKMEASUREMENT = _descriptor.Descriptor(
  name='LinkMeasurement',
  full_name='UpdateSignal.StaResult.LinkMeasurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='BSSID', full_name='UpdateSignal.StaResult.LinkMeasurement.BSSID', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='UpdateSignal.StaResult.LinkMeasurement.rssi', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=238,
)

_UPDATESIGNAL_STARESULT = _descriptor.Descriptor(
  name='StaResult',
  full_name='UpdateSignal.StaResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StaMAC', full_name='UpdateSignal.StaResult.StaMAC', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkmeasurements', full_name='UpdateSignal.StaResult.linkmeasurements', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATESIGNAL_STARESULT_LINKMEASUREMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=238,
)

_UPDATESIGNAL = _descriptor.Descriptor(
  name='UpdateSignal',
  full_name='UpdateSignal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='BSSID', full_name='UpdateSignal.BSSID', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staresults', full_name='UpdateSignal.staresults', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATESIGNAL_STARESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=238,
)

_UPDATESIGNAL_STARESULT_LINKMEASUREMENT.containing_type = _UPDATESIGNAL_STARESULT
_UPDATESIGNAL_STARESULT.fields_by_name['linkmeasurements'].message_type = _UPDATESIGNAL_STARESULT_LINKMEASUREMENT
_UPDATESIGNAL_STARESULT.containing_type = _UPDATESIGNAL
_UPDATESIGNAL.fields_by_name['staresults'].message_type = _UPDATESIGNAL_STARESULT
DESCRIPTOR.message_types_by_name['UpdateSignal'] = _UPDATESIGNAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateSignal = _reflection.GeneratedProtocolMessageType('UpdateSignal', (_message.Message,), dict(

  StaResult = _reflection.GeneratedProtocolMessageType('StaResult', (_message.Message,), dict(

    LinkMeasurement = _reflection.GeneratedProtocolMessageType('LinkMeasurement', (_message.Message,), dict(
      DESCRIPTOR = _UPDATESIGNAL_STARESULT_LINKMEASUREMENT,
      __module__ = 'messages_pb2'
      # @@protoc_insertion_point(class_scope:UpdateSignal.StaResult.LinkMeasurement)
      ))
    ,
    DESCRIPTOR = _UPDATESIGNAL_STARESULT,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:UpdateSignal.StaResult)
    ))
  ,
  DESCRIPTOR = _UPDATESIGNAL,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:UpdateSignal)
  ))
_sym_db.RegisterMessage(UpdateSignal)
_sym_db.RegisterMessage(UpdateSignal.StaResult)
_sym_db.RegisterMessage(UpdateSignal.StaResult.LinkMeasurement)


# @@protoc_insertion_point(module_scope)