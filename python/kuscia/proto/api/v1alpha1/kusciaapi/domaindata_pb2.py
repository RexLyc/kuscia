# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kuscia/proto/api/v1alpha1/kusciaapi/domaindata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kuscia.proto.api.v1alpha1 import common_pb2 as kuscia_dot_proto_dot_api_dot_v1alpha1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4kuscia/proto/api/v1alpha1/kusciaapi/domaindata.proto\x12#kuscia.proto.api.v1alpha1.kusciaapi\x1a&kuscia/proto/api/v1alpha1/common.proto\"\xdc\x03\n\x17\x43reateDomainDataRequest\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.kuscia.proto.api.v1alpha1.RequestHeader\x12\x15\n\rdomaindata_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x14\n\x0crelative_uri\x18\x05 \x01(\t\x12\x11\n\tdomain_id\x18\x06 \x01(\t\x12\x15\n\rdatasource_id\x18\x07 \x01(\t\x12`\n\nattributes\x18\x08 \x03(\x0b\x32L.kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataRequest.AttributesEntry\x12\x37\n\tpartition\x18\t \x01(\x0b\x32$.kuscia.proto.api.v1alpha1.Partition\x12\x36\n\x07\x63olumns\x18\n \x03(\x0b\x32%.kuscia.proto.api.v1alpha1.DataColumn\x12\x0e\n\x06vendor\x18\x0b \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9e\x01\n\x18\x43reateDomainDataResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.kuscia.proto.api.v1alpha1.Status\x12O\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x41.kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataResponseData\"5\n\x1c\x43reateDomainDataResponseData\x12\x15\n\rdomaindata_id\x18\x01 \x01(\t\"\xdc\x03\n\x17UpdateDomainDataRequest\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.kuscia.proto.api.v1alpha1.RequestHeader\x12\x15\n\rdomaindata_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x14\n\x0crelative_uri\x18\x05 \x01(\t\x12\x11\n\tdomain_id\x18\x06 \x01(\t\x12\x15\n\rdatasource_id\x18\x07 \x01(\t\x12`\n\nattributes\x18\x08 \x03(\x0b\x32L.kuscia.proto.api.v1alpha1.kusciaapi.UpdateDomainDataRequest.AttributesEntry\x12\x37\n\tpartition\x18\t \x01(\x0b\x32$.kuscia.proto.api.v1alpha1.Partition\x12\x36\n\x07\x63olumns\x18\n \x03(\x0b\x32%.kuscia.proto.api.v1alpha1.DataColumn\x12\x0e\n\x06vendor\x18\x0b \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"M\n\x18UpdateDomainDataResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.kuscia.proto.api.v1alpha1.Status\"}\n\x17\x44\x65leteDomainDataRequest\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.kuscia.proto.api.v1alpha1.RequestHeader\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x15\n\rdomaindata_id\x18\x03 \x01(\t\"M\n\x18\x44\x65leteDomainDataResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.kuscia.proto.api.v1alpha1.Status\"\xa1\x01\n\x16QueryDomainDataRequest\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.kuscia.proto.api.v1alpha1.RequestHeader\x12M\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32?.kuscia.proto.api.v1alpha1.kusciaapi.QueryDomainDataRequestData\"\x8b\x01\n\x17QueryDomainDataResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.kuscia.proto.api.v1alpha1.Status\x12=\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32/.kuscia.proto.api.v1alpha1.kusciaapi.DomainData\"F\n\x1aQueryDomainDataRequestData\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x15\n\rdomaindata_id\x18\x02 \x01(\t\"\xa6\x01\n\x1b\x42\x61tchQueryDomainDataRequest\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.kuscia.proto.api.v1alpha1.RequestHeader\x12M\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32?.kuscia.proto.api.v1alpha1.kusciaapi.QueryDomainDataRequestData\"\x94\x01\n\x1c\x42\x61tchQueryDomainDataResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.kuscia.proto.api.v1alpha1.Status\x12\x41\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x33.kuscia.proto.api.v1alpha1.kusciaapi.DomainDataList\"\x9f\x01\n\x15ListDomainDataRequest\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.kuscia.proto.api.v1alpha1.RequestHeader\x12L\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32>.kuscia.proto.api.v1alpha1.kusciaapi.ListDomainDataRequestData\"\x8e\x01\n\x16ListDomainDataResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.kuscia.proto.api.v1alpha1.Status\x12\x41\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x33.kuscia.proto.api.v1alpha1.kusciaapi.DomainDataList\"b\n\x19ListDomainDataRequestData\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x17\n\x0f\x64omaindata_type\x18\x02 \x01(\t\x12\x19\n\x11\x64omaindata_vendor\x18\x03 \x01(\t\"Z\n\x0e\x44omainDataList\x12H\n\x0f\x64omaindata_list\x18\x01 \x03(\x0b\x32/.kuscia.proto.api.v1alpha1.kusciaapi.DomainData\"\x98\x03\n\nDomainData\x12\x15\n\rdomaindata_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x14\n\x0crelative_uri\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\x12\x15\n\rdatasource_id\x18\x06 \x01(\t\x12S\n\nattributes\x18\x07 \x03(\x0b\x32?.kuscia.proto.api.v1alpha1.kusciaapi.DomainData.AttributesEntry\x12\x37\n\tpartition\x18\x08 \x01(\x0b\x32$.kuscia.proto.api.v1alpha1.Partition\x12\x36\n\x07\x63olumns\x18\t \x03(\x0b\x32%.kuscia.proto.api.v1alpha1.DataColumn\x12\x0e\n\x06vendor\x18\n \x01(\t\x12\x0e\n\x06status\x18\x0b \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x82\x07\n\x11\x44omainDataService\x12\x8f\x01\n\x10\x43reateDomainData\x12<.kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataRequest\x1a=.kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataResponse\x12\x8f\x01\n\x10UpdateDomainData\x12<.kuscia.proto.api.v1alpha1.kusciaapi.UpdateDomainDataRequest\x1a=.kuscia.proto.api.v1alpha1.kusciaapi.UpdateDomainDataResponse\x12\x8f\x01\n\x10\x44\x65leteDomainData\x12<.kuscia.proto.api.v1alpha1.kusciaapi.DeleteDomainDataRequest\x1a=.kuscia.proto.api.v1alpha1.kusciaapi.DeleteDomainDataResponse\x12\x8c\x01\n\x0fQueryDomainData\x12;.kuscia.proto.api.v1alpha1.kusciaapi.QueryDomainDataRequest\x1a<.kuscia.proto.api.v1alpha1.kusciaapi.QueryDomainDataResponse\x12\x9b\x01\n\x14\x42\x61tchQueryDomainData\x12@.kuscia.proto.api.v1alpha1.kusciaapi.BatchQueryDomainDataRequest\x1a\x41.kuscia.proto.api.v1alpha1.kusciaapi.BatchQueryDomainDataResponse\x12\x89\x01\n\x0eListDomainData\x12:.kuscia.proto.api.v1alpha1.kusciaapi.ListDomainDataRequest\x1a;.kuscia.proto.api.v1alpha1.kusciaapi.ListDomainDataResponseB^\n!org.secretflow.v1alpha1.kusciaapiZ9github.com/secretflow/kuscia/proto/api/v1alpha1/kusciaapib\x06proto3')



_CREATEDOMAINDATAREQUEST = DESCRIPTOR.message_types_by_name['CreateDomainDataRequest']
_CREATEDOMAINDATAREQUEST_ATTRIBUTESENTRY = _CREATEDOMAINDATAREQUEST.nested_types_by_name['AttributesEntry']
_CREATEDOMAINDATARESPONSE = DESCRIPTOR.message_types_by_name['CreateDomainDataResponse']
_CREATEDOMAINDATARESPONSEDATA = DESCRIPTOR.message_types_by_name['CreateDomainDataResponseData']
_UPDATEDOMAINDATAREQUEST = DESCRIPTOR.message_types_by_name['UpdateDomainDataRequest']
_UPDATEDOMAINDATAREQUEST_ATTRIBUTESENTRY = _UPDATEDOMAINDATAREQUEST.nested_types_by_name['AttributesEntry']
_UPDATEDOMAINDATARESPONSE = DESCRIPTOR.message_types_by_name['UpdateDomainDataResponse']
_DELETEDOMAINDATAREQUEST = DESCRIPTOR.message_types_by_name['DeleteDomainDataRequest']
_DELETEDOMAINDATARESPONSE = DESCRIPTOR.message_types_by_name['DeleteDomainDataResponse']
_QUERYDOMAINDATAREQUEST = DESCRIPTOR.message_types_by_name['QueryDomainDataRequest']
_QUERYDOMAINDATARESPONSE = DESCRIPTOR.message_types_by_name['QueryDomainDataResponse']
_QUERYDOMAINDATAREQUESTDATA = DESCRIPTOR.message_types_by_name['QueryDomainDataRequestData']
_BATCHQUERYDOMAINDATAREQUEST = DESCRIPTOR.message_types_by_name['BatchQueryDomainDataRequest']
_BATCHQUERYDOMAINDATARESPONSE = DESCRIPTOR.message_types_by_name['BatchQueryDomainDataResponse']
_LISTDOMAINDATAREQUEST = DESCRIPTOR.message_types_by_name['ListDomainDataRequest']
_LISTDOMAINDATARESPONSE = DESCRIPTOR.message_types_by_name['ListDomainDataResponse']
_LISTDOMAINDATAREQUESTDATA = DESCRIPTOR.message_types_by_name['ListDomainDataRequestData']
_DOMAINDATALIST = DESCRIPTOR.message_types_by_name['DomainDataList']
_DOMAINDATA = DESCRIPTOR.message_types_by_name['DomainData']
_DOMAINDATA_ATTRIBUTESENTRY = _DOMAINDATA.nested_types_by_name['AttributesEntry']
CreateDomainDataRequest = _reflection.GeneratedProtocolMessageType('CreateDomainDataRequest', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEDOMAINDATAREQUEST_ATTRIBUTESENTRY,
    '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
    # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataRequest.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEDOMAINDATAREQUEST,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataRequest)
  })
_sym_db.RegisterMessage(CreateDomainDataRequest)
_sym_db.RegisterMessage(CreateDomainDataRequest.AttributesEntry)

CreateDomainDataResponse = _reflection.GeneratedProtocolMessageType('CreateDomainDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOMAINDATARESPONSE,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataResponse)
  })
_sym_db.RegisterMessage(CreateDomainDataResponse)

CreateDomainDataResponseData = _reflection.GeneratedProtocolMessageType('CreateDomainDataResponseData', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOMAINDATARESPONSEDATA,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.CreateDomainDataResponseData)
  })
_sym_db.RegisterMessage(CreateDomainDataResponseData)

UpdateDomainDataRequest = _reflection.GeneratedProtocolMessageType('UpdateDomainDataRequest', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEDOMAINDATAREQUEST_ATTRIBUTESENTRY,
    '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
    # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.UpdateDomainDataRequest.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEDOMAINDATAREQUEST,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.UpdateDomainDataRequest)
  })
_sym_db.RegisterMessage(UpdateDomainDataRequest)
_sym_db.RegisterMessage(UpdateDomainDataRequest.AttributesEntry)

UpdateDomainDataResponse = _reflection.GeneratedProtocolMessageType('UpdateDomainDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDOMAINDATARESPONSE,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.UpdateDomainDataResponse)
  })
_sym_db.RegisterMessage(UpdateDomainDataResponse)

DeleteDomainDataRequest = _reflection.GeneratedProtocolMessageType('DeleteDomainDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOMAINDATAREQUEST,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.DeleteDomainDataRequest)
  })
_sym_db.RegisterMessage(DeleteDomainDataRequest)

DeleteDomainDataResponse = _reflection.GeneratedProtocolMessageType('DeleteDomainDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOMAINDATARESPONSE,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.DeleteDomainDataResponse)
  })
_sym_db.RegisterMessage(DeleteDomainDataResponse)

QueryDomainDataRequest = _reflection.GeneratedProtocolMessageType('QueryDomainDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDOMAINDATAREQUEST,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.QueryDomainDataRequest)
  })
_sym_db.RegisterMessage(QueryDomainDataRequest)

QueryDomainDataResponse = _reflection.GeneratedProtocolMessageType('QueryDomainDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDOMAINDATARESPONSE,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.QueryDomainDataResponse)
  })
_sym_db.RegisterMessage(QueryDomainDataResponse)

QueryDomainDataRequestData = _reflection.GeneratedProtocolMessageType('QueryDomainDataRequestData', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDOMAINDATAREQUESTDATA,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.QueryDomainDataRequestData)
  })
_sym_db.RegisterMessage(QueryDomainDataRequestData)

BatchQueryDomainDataRequest = _reflection.GeneratedProtocolMessageType('BatchQueryDomainDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHQUERYDOMAINDATAREQUEST,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.BatchQueryDomainDataRequest)
  })
_sym_db.RegisterMessage(BatchQueryDomainDataRequest)

BatchQueryDomainDataResponse = _reflection.GeneratedProtocolMessageType('BatchQueryDomainDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHQUERYDOMAINDATARESPONSE,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.BatchQueryDomainDataResponse)
  })
_sym_db.RegisterMessage(BatchQueryDomainDataResponse)

ListDomainDataRequest = _reflection.GeneratedProtocolMessageType('ListDomainDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOMAINDATAREQUEST,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.ListDomainDataRequest)
  })
_sym_db.RegisterMessage(ListDomainDataRequest)

ListDomainDataResponse = _reflection.GeneratedProtocolMessageType('ListDomainDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOMAINDATARESPONSE,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.ListDomainDataResponse)
  })
_sym_db.RegisterMessage(ListDomainDataResponse)

ListDomainDataRequestData = _reflection.GeneratedProtocolMessageType('ListDomainDataRequestData', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOMAINDATAREQUESTDATA,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.ListDomainDataRequestData)
  })
_sym_db.RegisterMessage(ListDomainDataRequestData)

DomainDataList = _reflection.GeneratedProtocolMessageType('DomainDataList', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINDATALIST,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.DomainDataList)
  })
_sym_db.RegisterMessage(DomainDataList)

DomainData = _reflection.GeneratedProtocolMessageType('DomainData', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOMAINDATA_ATTRIBUTESENTRY,
    '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
    # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.DomainData.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _DOMAINDATA,
  '__module__' : 'kuscia.proto.api.v1alpha1.kusciaapi.domaindata_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.kusciaapi.DomainData)
  })
_sym_db.RegisterMessage(DomainData)
_sym_db.RegisterMessage(DomainData.AttributesEntry)

_DOMAINDATASERVICE = DESCRIPTOR.services_by_name['DomainDataService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!org.secretflow.v1alpha1.kusciaapiZ9github.com/secretflow/kuscia/proto/api/v1alpha1/kusciaapi'
  _CREATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._options = None
  _CREATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _UPDATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._options = None
  _UPDATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _DOMAINDATA_ATTRIBUTESENTRY._options = None
  _DOMAINDATA_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _CREATEDOMAINDATAREQUEST._serialized_start=134
  _CREATEDOMAINDATAREQUEST._serialized_end=610
  _CREATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._serialized_start=561
  _CREATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._serialized_end=610
  _CREATEDOMAINDATARESPONSE._serialized_start=613
  _CREATEDOMAINDATARESPONSE._serialized_end=771
  _CREATEDOMAINDATARESPONSEDATA._serialized_start=773
  _CREATEDOMAINDATARESPONSEDATA._serialized_end=826
  _UPDATEDOMAINDATAREQUEST._serialized_start=829
  _UPDATEDOMAINDATAREQUEST._serialized_end=1305
  _UPDATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._serialized_start=561
  _UPDATEDOMAINDATAREQUEST_ATTRIBUTESENTRY._serialized_end=610
  _UPDATEDOMAINDATARESPONSE._serialized_start=1307
  _UPDATEDOMAINDATARESPONSE._serialized_end=1384
  _DELETEDOMAINDATAREQUEST._serialized_start=1386
  _DELETEDOMAINDATAREQUEST._serialized_end=1511
  _DELETEDOMAINDATARESPONSE._serialized_start=1513
  _DELETEDOMAINDATARESPONSE._serialized_end=1590
  _QUERYDOMAINDATAREQUEST._serialized_start=1593
  _QUERYDOMAINDATAREQUEST._serialized_end=1754
  _QUERYDOMAINDATARESPONSE._serialized_start=1757
  _QUERYDOMAINDATARESPONSE._serialized_end=1896
  _QUERYDOMAINDATAREQUESTDATA._serialized_start=1898
  _QUERYDOMAINDATAREQUESTDATA._serialized_end=1968
  _BATCHQUERYDOMAINDATAREQUEST._serialized_start=1971
  _BATCHQUERYDOMAINDATAREQUEST._serialized_end=2137
  _BATCHQUERYDOMAINDATARESPONSE._serialized_start=2140
  _BATCHQUERYDOMAINDATARESPONSE._serialized_end=2288
  _LISTDOMAINDATAREQUEST._serialized_start=2291
  _LISTDOMAINDATAREQUEST._serialized_end=2450
  _LISTDOMAINDATARESPONSE._serialized_start=2453
  _LISTDOMAINDATARESPONSE._serialized_end=2595
  _LISTDOMAINDATAREQUESTDATA._serialized_start=2597
  _LISTDOMAINDATAREQUESTDATA._serialized_end=2695
  _DOMAINDATALIST._serialized_start=2697
  _DOMAINDATALIST._serialized_end=2787
  _DOMAINDATA._serialized_start=2790
  _DOMAINDATA._serialized_end=3198
  _DOMAINDATA_ATTRIBUTESENTRY._serialized_start=561
  _DOMAINDATA_ATTRIBUTESENTRY._serialized_end=610
  _DOMAINDATASERVICE._serialized_start=3201
  _DOMAINDATASERVICE._serialized_end=4099
# @@protoc_insertion_point(module_scope)