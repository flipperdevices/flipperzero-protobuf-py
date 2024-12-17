"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdesktop.proto\x12\nPB_Desktop"\x11\n\x0fIsLockedRequest"\x0f\n\rUnlockRequest"\x18\n\x16StatusSubscribeRequest"\x1a\n\x18StatusUnsubscribeRequest"\x18\n\x06Status\x12\x0e\n\x06locked\x18\x01 \x01(\x08B%\n#com.flipperdevices.protobuf.desktopb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'desktop_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.flipperdevices.protobuf.desktop'
    _globals['_ISLOCKEDREQUEST']._serialized_start = 29
    _globals['_ISLOCKEDREQUEST']._serialized_end = 46
    _globals['_UNLOCKREQUEST']._serialized_start = 48
    _globals['_UNLOCKREQUEST']._serialized_end = 63
    _globals['_STATUSSUBSCRIBEREQUEST']._serialized_start = 65
    _globals['_STATUSSUBSCRIBEREQUEST']._serialized_end = 89
    _globals['_STATUSUNSUBSCRIBEREQUEST']._serialized_start = 91
    _globals['_STATUSUNSUBSCRIBEREQUEST']._serialized_end = 117
    _globals['_STATUS']._serialized_start = 119
    _globals['_STATUS']._serialized_end = 143