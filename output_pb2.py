# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: output.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='output.proto',
  package='falco.output',
  syntax='proto3',
  serialized_options=_b('Z1github.com/falcosecurity/client-go/pkg/api/output'),
  serialized_pb=_b('\n\x0coutput.proto\x12\x0c\x66\x61lco.output\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0cschema.proto\"\x1c\n\x07request\x12\x11\n\tkeepalive\x18\x01 \x01(\x08\"\xaa\x02\n\x08response\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x08priority\x18\x02 \x01(\x0e\x32\x16.falco.schema.priority\x12$\n\x06source\x18\x03 \x01(\x0e\x32\x14.falco.schema.source\x12\x0c\n\x04rule\x18\x04 \x01(\t\x12\x0e\n\x06output\x18\x05 \x01(\t\x12?\n\routput_fields\x18\x06 \x03(\x0b\x32(.falco.output.response.OutputFieldsEntry\x12\x10\n\x08hostname\x18\x07 \x01(\t\x1a\x33\n\x11OutputFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32G\n\x07service\x12<\n\tsubscribe\x12\x15.falco.output.request\x1a\x16.falco.output.response0\x01\x42\x33Z1github.com/falcosecurity/client-go/pkg/api/outputb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,schema__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='request',
  full_name='falco.output.request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keepalive', full_name='falco.output.request.keepalive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=77,
  serialized_end=105,
)


_RESPONSE_OUTPUTFIELDSENTRY = _descriptor.Descriptor(
  name='OutputFieldsEntry',
  full_name='falco.output.response.OutputFieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='falco.output.response.OutputFieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='falco.output.response.OutputFieldsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=406,
)

_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='falco.output.response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='falco.output.response.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='falco.output.response.priority', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='falco.output.response.source', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='falco.output.response.rule', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='falco.output.response.output', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_fields', full_name='falco.output.response.output_fields', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='falco.output.response.hostname', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_OUTPUTFIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=406,
)

_RESPONSE_OUTPUTFIELDSENTRY.containing_type = _RESPONSE
_RESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RESPONSE.fields_by_name['priority'].enum_type = schema__pb2._PRIORITY
_RESPONSE.fields_by_name['source'].enum_type = schema__pb2._SOURCE
_RESPONSE.fields_by_name['output_fields'].message_type = _RESPONSE_OUTPUTFIELDSENTRY
DESCRIPTOR.message_types_by_name['request'] = _REQUEST
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

request = _reflection.GeneratedProtocolMessageType('request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'output_pb2'
  # @@protoc_insertion_point(class_scope:falco.output.request)
  })
_sym_db.RegisterMessage(request)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), {

  'OutputFieldsEntry' : _reflection.GeneratedProtocolMessageType('OutputFieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_OUTPUTFIELDSENTRY,
    '__module__' : 'output_pb2'
    # @@protoc_insertion_point(class_scope:falco.output.response.OutputFieldsEntry)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'output_pb2'
  # @@protoc_insertion_point(class_scope:falco.output.response)
  })
_sym_db.RegisterMessage(response)
_sym_db.RegisterMessage(response.OutputFieldsEntry)


DESCRIPTOR._options = None
_RESPONSE_OUTPUTFIELDSENTRY._options = None

_SERVICE = _descriptor.ServiceDescriptor(
  name='service',
  full_name='falco.output.service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=408,
  serialized_end=479,
  methods=[
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='falco.output.service.subscribe',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['service'] = _SERVICE

# @@protoc_insertion_point(module_scope)
