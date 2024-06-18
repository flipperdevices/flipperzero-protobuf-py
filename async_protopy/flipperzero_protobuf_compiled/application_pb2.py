"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import descriptor as _descriptor

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11application.proto\x12\x06PB_App"*\n\x0cStartRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04args\x18\x02 \x01(\t"\x13\n\x11LockStatusRequest"$\n\x12LockStatusResponse\x12\x0e\n\x06locked\x18\x01 \x01(\x08"\x10\n\x0eAppExitRequest""\n\x12AppLoadFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t"4\n\x15AppButtonPressRequest\x12\x0c\n\x04args\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05"\x19\n\x17AppButtonReleaseRequest"3\n\x10AppStateResponse\x12\x1f\n\x05state\x18\x01 \x01(\x0e2\x10.PB_App.AppState"\x11\n\x0fGetErrorRequest".\n\x10GetErrorResponse\x12\x0c\n\x04code\x18\x01 \x01(\r\x12\x0c\n\x04text\x18\x02 \x01(\t"#\n\x13DataExchangeRequest\x12\x0c\n\x04data\x18\x01 \x01(\x0c*+\n\x08AppState\x12\x0e\n\nAPP_CLOSED\x10\x00\x12\x0f\n\x0bAPP_STARTED\x10\x01B!\n\x1fcom.flipperdevices.protobuf.appb\x06proto3'
)
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'application_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.flipperdevices.protobuf.app'
    _globals['_APPSTATE']._serialized_start = 424
    _globals['_APPSTATE']._serialized_end = 467
    _globals['_STARTREQUEST']._serialized_start = 29
    _globals['_STARTREQUEST']._serialized_end = 71
    _globals['_LOCKSTATUSREQUEST']._serialized_start = 73
    _globals['_LOCKSTATUSREQUEST']._serialized_end = 92
    _globals['_LOCKSTATUSRESPONSE']._serialized_start = 94
    _globals['_LOCKSTATUSRESPONSE']._serialized_end = 130
    _globals['_APPEXITREQUEST']._serialized_start = 132
    _globals['_APPEXITREQUEST']._serialized_end = 148
    _globals['_APPLOADFILEREQUEST']._serialized_start = 150
    _globals['_APPLOADFILEREQUEST']._serialized_end = 184
    _globals['_APPBUTTONPRESSREQUEST']._serialized_start = 186
    _globals['_APPBUTTONPRESSREQUEST']._serialized_end = 238
    _globals['_APPBUTTONRELEASEREQUEST']._serialized_start = 240
    _globals['_APPBUTTONRELEASEREQUEST']._serialized_end = 265
    _globals['_APPSTATERESPONSE']._serialized_start = 267
    _globals['_APPSTATERESPONSE']._serialized_end = 318
    _globals['_GETERRORREQUEST']._serialized_start = 320
    _globals['_GETERRORREQUEST']._serialized_end = 337
    _globals['_GETERRORRESPONSE']._serialized_start = 339
    _globals['_GETERRORRESPONSE']._serialized_end = 385
    _globals['_DATAEXCHANGEREQUEST']._serialized_start = 387
    _globals['_DATAEXCHANGEREQUEST']._serialized_end = 422
