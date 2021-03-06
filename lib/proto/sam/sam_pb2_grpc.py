# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
import sys
sys.path.append("../../proto")
from copytrade import copytrade_pb2 as copytrade_dot_copytrade__pb2
from sam import sam_pb2 as sam_dot_sam__pb2
from tradesignal import tradesignal_pb2 as tradesignal_dot_tradesignal__pb2


class SamSignalSrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAssetByAccount = channel.unary_unary(
        '/sam.SamSignalSrv/GetAssetByAccount',
        request_serializer=sam_dot_sam__pb2.AccountRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.Asset.FromString,
        )
    self.GetSymbolListByAccount = channel.unary_unary(
        '/sam.SamSignalSrv/GetSymbolListByAccount',
        request_serializer=sam_dot_sam__pb2.AccountRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.SymbolListReply.FromString,
        )
    self.GetSymbolListByAccountStream = channel.stream_stream(
        '/sam.SamSignalSrv/GetSymbolListByAccountStream',
        request_serializer=sam_dot_sam__pb2.AccountRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.SymbolListReply.FromString,
        )
    self.SubscribeTradeSignal = channel.unary_stream(
        '/sam.SamSignalSrv/SubscribeTradeSignal',
        request_serializer=sam_dot_sam__pb2.Empty.SerializeToString,
        response_deserializer=tradesignal_dot_tradesignal__pb2.TradeSignal.FromString,
        )
    self.GetMT4Clients = channel.unary_unary(
        '/sam.SamSignalSrv/GetMT4Clients',
        request_serializer=sam_dot_sam__pb2.GetMT4ClientsRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.GetMT4ClientsReply.FromString,
        )
    self.SyncTrades = channel.unary_unary(
        '/sam.SamSignalSrv/SyncTrades',
        request_serializer=sam_dot_sam__pb2.SyncTradesRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.SyncTradesReply.FromString,
        )
    self.SyncHistoryTrades = channel.unary_unary(
        '/sam.SamSignalSrv/SyncHistoryTrades',
        request_serializer=sam_dot_sam__pb2.AccountRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.SyncHistoryTradesReply.FromString,
        )
    self.NotifyBindAccount = channel.unary_unary(
        '/sam.SamSignalSrv/NotifyBindAccount',
        request_serializer=sam_dot_sam__pb2.AccountRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.SuccessReply.FromString,
        )
    self.NotifyInvalidAccount = channel.unary_unary(
        '/sam.SamSignalSrv/NotifyInvalidAccount',
        request_serializer=sam_dot_sam__pb2.AccountRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.SuccessReply.FromString,
        )
    self.Position = channel.unary_unary(
        '/sam.SamSignalSrv/Position',
        request_serializer=sam_dot_sam__pb2.PositionRequest.SerializeToString,
        response_deserializer=sam_dot_sam__pb2.PositionReply.FromString,
        )
    self.CopyTrade = channel.unary_unary(
        '/sam.SamSignalSrv/CopyTrade',
        request_serializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.SerializeToString,
        response_deserializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.FromString,
        )
    self.CopyTradeStream = channel.stream_stream(
        '/sam.SamSignalSrv/CopyTradeStream',
        request_serializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.SerializeToString,
        response_deserializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.FromString,
        )
    self.GetTradeSignalList = channel.unary_unary(
        '/sam.SamSignalSrv/GetTradeSignalList',
        request_serializer=tradesignal_dot_tradesignal__pb2.TradeSignalListRequest.SerializeToString,
        response_deserializer=tradesignal_dot_tradesignal__pb2.TradeSignalListReply.FromString,
        )


class SamSignalSrvServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAssetByAccount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSymbolListByAccount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSymbolListByAccountStream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeTradeSignal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMT4Clients(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SyncTrades(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SyncHistoryTrades(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotifyBindAccount(self, request, context):
    """绑定成功通知
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotifyInvalidAccount(self, request, context):
    """密码变更通知
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Position(self, request, context):
    """下单
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CopyTrade(self, request, context):
    """交易 (Fake 😁)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CopyTradeStream(self, request_iterator, context):
    """跟单交易
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTradeSignalList(self, request, context):
    """获取帐户所有订单
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SamSignalSrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAssetByAccount': grpc.unary_unary_rpc_method_handler(
          servicer.GetAssetByAccount,
          request_deserializer=sam_dot_sam__pb2.AccountRequest.FromString,
          response_serializer=sam_dot_sam__pb2.Asset.SerializeToString,
      ),
      'GetSymbolListByAccount': grpc.unary_unary_rpc_method_handler(
          servicer.GetSymbolListByAccount,
          request_deserializer=sam_dot_sam__pb2.AccountRequest.FromString,
          response_serializer=sam_dot_sam__pb2.SymbolListReply.SerializeToString,
      ),
      'GetSymbolListByAccountStream': grpc.stream_stream_rpc_method_handler(
          servicer.GetSymbolListByAccountStream,
          request_deserializer=sam_dot_sam__pb2.AccountRequest.FromString,
          response_serializer=sam_dot_sam__pb2.SymbolListReply.SerializeToString,
      ),
      'SubscribeTradeSignal': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeTradeSignal,
          request_deserializer=sam_dot_sam__pb2.Empty.FromString,
          response_serializer=tradesignal_dot_tradesignal__pb2.TradeSignal.SerializeToString,
      ),
      'GetMT4Clients': grpc.unary_unary_rpc_method_handler(
          servicer.GetMT4Clients,
          request_deserializer=sam_dot_sam__pb2.GetMT4ClientsRequest.FromString,
          response_serializer=sam_dot_sam__pb2.GetMT4ClientsReply.SerializeToString,
      ),
      'SyncTrades': grpc.unary_unary_rpc_method_handler(
          servicer.SyncTrades,
          request_deserializer=sam_dot_sam__pb2.SyncTradesRequest.FromString,
          response_serializer=sam_dot_sam__pb2.SyncTradesReply.SerializeToString,
      ),
      'SyncHistoryTrades': grpc.unary_unary_rpc_method_handler(
          servicer.SyncHistoryTrades,
          request_deserializer=sam_dot_sam__pb2.AccountRequest.FromString,
          response_serializer=sam_dot_sam__pb2.SyncHistoryTradesReply.SerializeToString,
      ),
      'NotifyBindAccount': grpc.unary_unary_rpc_method_handler(
          servicer.NotifyBindAccount,
          request_deserializer=sam_dot_sam__pb2.AccountRequest.FromString,
          response_serializer=sam_dot_sam__pb2.SuccessReply.SerializeToString,
      ),
      'NotifyInvalidAccount': grpc.unary_unary_rpc_method_handler(
          servicer.NotifyInvalidAccount,
          request_deserializer=sam_dot_sam__pb2.AccountRequest.FromString,
          response_serializer=sam_dot_sam__pb2.SuccessReply.SerializeToString,
      ),
      'Position': grpc.unary_unary_rpc_method_handler(
          servicer.Position,
          request_deserializer=sam_dot_sam__pb2.PositionRequest.FromString,
          response_serializer=sam_dot_sam__pb2.PositionReply.SerializeToString,
      ),
      'CopyTrade': grpc.unary_unary_rpc_method_handler(
          servicer.CopyTrade,
          request_deserializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.FromString,
          response_serializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.SerializeToString,
      ),
      'CopyTradeStream': grpc.stream_stream_rpc_method_handler(
          servicer.CopyTradeStream,
          request_deserializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.FromString,
          response_serializer=copytrade_dot_copytrade__pb2.OrderWithQuantity.SerializeToString,
      ),
      'GetTradeSignalList': grpc.unary_unary_rpc_method_handler(
          servicer.GetTradeSignalList,
          request_deserializer=tradesignal_dot_tradesignal__pb2.TradeSignalListRequest.FromString,
          response_serializer=tradesignal_dot_tradesignal__pb2.TradeSignalListReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sam.SamSignalSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
