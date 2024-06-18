"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import descriptor as _descriptor

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ngpio.proto\x12\x07PB_Gpio"O\n\nSetPinMode\x12\x1d\n\x03pin\x18\x01 \x01(\x0e2\x10.PB_Gpio.GpioPin\x12"\n\x04mode\x18\x02 \x01(\x0e2\x14.PB_Gpio.GpioPinMode"X\n\x0cSetInputPull\x12\x1d\n\x03pin\x18\x01 \x01(\x0e2\x10.PB_Gpio.GpioPin\x12)\n\tpull_mode\x18\x02 \x01(\x0e2\x16.PB_Gpio.GpioInputPull"+\n\nGetPinMode\x12\x1d\n\x03pin\x18\x01 \x01(\x0e2\x10.PB_Gpio.GpioPin"8\n\x12GetPinModeResponse\x12"\n\x04mode\x18\x01 \x01(\x0e2\x14.PB_Gpio.GpioPinMode"(\n\x07ReadPin\x12\x1d\n\x03pin\x18\x01 \x01(\x0e2\x10.PB_Gpio.GpioPin" \n\x0fReadPinResponse\x12\r\n\x05value\x18\x02 \x01(\r"8\n\x08WritePin\x12\x1d\n\x03pin\x18\x01 \x01(\x0e2\x10.PB_Gpio.GpioPin\x12\r\n\x05value\x18\x02 \x01(\r*Q\n\x07GpioPin\x12\x07\n\x03PC0\x10\x00\x12\x07\n\x03PC1\x10\x01\x12\x07\n\x03PC3\x10\x02\x12\x07\n\x03PB2\x10\x03\x12\x07\n\x03PB3\x10\x04\x12\x07\n\x03PA4\x10\x05\x12\x07\n\x03PA6\x10\x06\x12\x07\n\x03PA7\x10\x07*$\n\x0bGpioPinMode\x12\n\n\x06OUTPUT\x10\x00\x12\t\n\x05INPUT\x10\x01*)\n\rGpioInputPull\x12\x06\n\x02NO\x10\x00\x12\x06\n\x02UP\x10\x01\x12\x08\n\x04DOWN\x10\x02B"\n com.flipperdevices.protobuf.gpiob\x06proto3'
)
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gpio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.flipperdevices.protobuf.gpio'
    _globals['_GPIOPIN']._serialized_start = 431
    _globals['_GPIOPIN']._serialized_end = 512
    _globals['_GPIOPINMODE']._serialized_start = 514
    _globals['_GPIOPINMODE']._serialized_end = 550
    _globals['_GPIOINPUTPULL']._serialized_start = 552
    _globals['_GPIOINPUTPULL']._serialized_end = 593
    _globals['_SETPINMODE']._serialized_start = 23
    _globals['_SETPINMODE']._serialized_end = 102
    _globals['_SETINPUTPULL']._serialized_start = 104
    _globals['_SETINPUTPULL']._serialized_end = 192
    _globals['_GETPINMODE']._serialized_start = 194
    _globals['_GETPINMODE']._serialized_end = 237
    _globals['_GETPINMODERESPONSE']._serialized_start = 239
    _globals['_GETPINMODERESPONSE']._serialized_end = 295
    _globals['_READPIN']._serialized_start = 297
    _globals['_READPIN']._serialized_end = 337
    _globals['_READPINRESPONSE']._serialized_start = 339
    _globals['_READPINRESPONSE']._serialized_end = 371
    _globals['_WRITEPIN']._serialized_start = 373
    _globals['_WRITEPIN']._serialized_end = 429
