"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\nPB_Storage"\x88\x01\n\x04File\x12\'\n\x04type\x18\x01 \x01(\x0e2\x19.PB_Storage.File.FileType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\r\x12\x0c\n\x04data\x18\x04 \x01(\x0c\x12\x0e\n\x06md5sum\x18\x05 \x01(\t"\x1d\n\x08FileType\x12\x08\n\x04FILE\x10\x00\x12\x07\n\x03DIR\x10\x01"\x1b\n\x0bInfoRequest\x12\x0c\n\x04path\x18\x01 \x01(\t"7\n\x0cInfoResponse\x12\x13\n\x0btotal_space\x18\x01 \x01(\x04\x12\x12\n\nfree_space\x18\x02 \x01(\x04" \n\x10TimestampRequest\x12\x0c\n\x04path\x18\x01 \x01(\t"&\n\x11TimestampResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\r"\x1b\n\x0bStatRequest\x12\x0c\n\x04path\x18\x01 \x01(\t".\n\x0cStatResponse\x12\x1e\n\x04file\x18\x01 \x01(\x0b2\x10.PB_Storage.File"I\n\x0bListRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x13\n\x0binclude_md5\x18\x02 \x01(\x08\x12\x17\n\x0ffilter_max_size\x18\x03 \x01(\r".\n\x0cListResponse\x12\x1e\n\x04file\x18\x01 \x03(\x0b2\x10.PB_Storage.File"\x1b\n\x0bReadRequest\x12\x0c\n\x04path\x18\x01 \x01(\t".\n\x0cReadResponse\x12\x1e\n\x04file\x18\x01 \x01(\x0b2\x10.PB_Storage.File"<\n\x0cWriteRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x1e\n\x04file\x18\x02 \x01(\x0b2\x10.PB_Storage.File"0\n\rDeleteRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x11\n\trecursive\x18\x02 \x01(\x08"\x1c\n\x0cMkdirRequest\x12\x0c\n\x04path\x18\x01 \x01(\t"\x1d\n\rMd5sumRequest\x12\x0c\n\x04path\x18\x01 \x01(\t" \n\x0eMd5sumResponse\x12\x0e\n\x06md5sum\x18\x01 \x01(\t"3\n\rRenameRequest\x12\x10\n\x08old_path\x18\x01 \x01(\t\x12\x10\n\x08new_path\x18\x02 \x01(\t"+\n\x13BackupCreateRequest\x12\x14\n\x0carchive_path\x18\x01 \x01(\t",\n\x14BackupRestoreRequest\x12\x14\n\x0carchive_path\x18\x01 \x01(\t"7\n\x11TarExtractRequest\x12\x10\n\x08tar_path\x18\x01 \x01(\t\x12\x10\n\x08out_path\x18\x02 \x01(\tB%\n#com.flipperdevices.protobuf.storageb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.flipperdevices.protobuf.storage'
    _globals['_FILE']._serialized_start = 30
    _globals['_FILE']._serialized_end = 166
    _globals['_FILE_FILETYPE']._serialized_start = 137
    _globals['_FILE_FILETYPE']._serialized_end = 166
    _globals['_INFOREQUEST']._serialized_start = 168
    _globals['_INFOREQUEST']._serialized_end = 195
    _globals['_INFORESPONSE']._serialized_start = 197
    _globals['_INFORESPONSE']._serialized_end = 252
    _globals['_TIMESTAMPREQUEST']._serialized_start = 254
    _globals['_TIMESTAMPREQUEST']._serialized_end = 286
    _globals['_TIMESTAMPRESPONSE']._serialized_start = 288
    _globals['_TIMESTAMPRESPONSE']._serialized_end = 326
    _globals['_STATREQUEST']._serialized_start = 328
    _globals['_STATREQUEST']._serialized_end = 355
    _globals['_STATRESPONSE']._serialized_start = 357
    _globals['_STATRESPONSE']._serialized_end = 403
    _globals['_LISTREQUEST']._serialized_start = 405
    _globals['_LISTREQUEST']._serialized_end = 478
    _globals['_LISTRESPONSE']._serialized_start = 480
    _globals['_LISTRESPONSE']._serialized_end = 526
    _globals['_READREQUEST']._serialized_start = 528
    _globals['_READREQUEST']._serialized_end = 555
    _globals['_READRESPONSE']._serialized_start = 557
    _globals['_READRESPONSE']._serialized_end = 603
    _globals['_WRITEREQUEST']._serialized_start = 605
    _globals['_WRITEREQUEST']._serialized_end = 665
    _globals['_DELETEREQUEST']._serialized_start = 667
    _globals['_DELETEREQUEST']._serialized_end = 715
    _globals['_MKDIRREQUEST']._serialized_start = 717
    _globals['_MKDIRREQUEST']._serialized_end = 745
    _globals['_MD5SUMREQUEST']._serialized_start = 747
    _globals['_MD5SUMREQUEST']._serialized_end = 776
    _globals['_MD5SUMRESPONSE']._serialized_start = 778
    _globals['_MD5SUMRESPONSE']._serialized_end = 810
    _globals['_RENAMEREQUEST']._serialized_start = 812
    _globals['_RENAMEREQUEST']._serialized_end = 863
    _globals['_BACKUPCREATEREQUEST']._serialized_start = 865
    _globals['_BACKUPCREATEREQUEST']._serialized_end = 908
    _globals['_BACKUPRESTOREREQUEST']._serialized_start = 910
    _globals['_BACKUPRESTOREREQUEST']._serialized_end = 954
    _globals['_TAREXTRACTREQUEST']._serialized_start = 956
    _globals['_TAREXTRACTREQUEST']._serialized_end = 1011