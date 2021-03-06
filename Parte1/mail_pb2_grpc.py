# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import mail_pb2 as mail__pb2


class GreeterStub(object):
  """option java_multiple_files = true;
  option java_package = "io.grpc.examples.helloworld";
  option java_outer_classname = "HelloWorldProto";
  option objc_class_prefix = "HLW";

  package mail;

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Log = channel.unary_unary(
        '/Greeter/Log',
        request_serializer=mail__pb2.Request.SerializeToString,
        response_deserializer=mail__pb2.Request.FromString,
        )
    self.SendText = channel.unary_unary(
        '/Greeter/SendText',
        request_serializer=mail__pb2.Text.SerializeToString,
        response_deserializer=mail__pb2.Text.FromString,
        )
    self.ShowBandeja = channel.unary_unary(
        '/Greeter/ShowBandeja',
        request_serializer=mail__pb2.Request.SerializeToString,
        response_deserializer=mail__pb2.Request.FromString,
        )
    self.ListAllUsers = channel.unary_unary(
        '/Greeter/ListAllUsers',
        request_serializer=mail__pb2.Request.SerializeToString,
        response_deserializer=mail__pb2.Request.FromString,
        )
    self.ShowEnviados = channel.unary_unary(
        '/Greeter/ShowEnviados',
        request_serializer=mail__pb2.Request.SerializeToString,
        response_deserializer=mail__pb2.Request.FromString,
        )


class GreeterServicer(object):
  """option java_multiple_files = true;
  option java_package = "io.grpc.examples.helloworld";
  option java_outer_classname = "HelloWorldProto";
  option objc_class_prefix = "HLW";

  package mail;

  """

  def Log(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendText(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowBandeja(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAllUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowEnviados(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Log': grpc.unary_unary_rpc_method_handler(
          servicer.Log,
          request_deserializer=mail__pb2.Request.FromString,
          response_serializer=mail__pb2.Request.SerializeToString,
      ),
      'SendText': grpc.unary_unary_rpc_method_handler(
          servicer.SendText,
          request_deserializer=mail__pb2.Text.FromString,
          response_serializer=mail__pb2.Text.SerializeToString,
      ),
      'ShowBandeja': grpc.unary_unary_rpc_method_handler(
          servicer.ShowBandeja,
          request_deserializer=mail__pb2.Request.FromString,
          response_serializer=mail__pb2.Request.SerializeToString,
      ),
      'ListAllUsers': grpc.unary_unary_rpc_method_handler(
          servicer.ListAllUsers,
          request_deserializer=mail__pb2.Request.FromString,
          response_serializer=mail__pb2.Request.SerializeToString,
      ),
      'ShowEnviados': grpc.unary_unary_rpc_method_handler(
          servicer.ShowEnviados,
          request_deserializer=mail__pb2.Request.FromString,
          response_serializer=mail__pb2.Request.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
