# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import version_pb2 as version__pb2


class serviceStub(object):
    """This service defines a RPC call
    to request the Falco version.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.version = channel.unary_unary(
                '/falco.version.service/version',
                request_serializer=version__pb2.request.SerializeToString,
                response_deserializer=version__pb2.response.FromString,
                )


class serviceServicer(object):
    """This service defines a RPC call
    to request the Falco version.
    """

    def version(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'version': grpc.unary_unary_rpc_method_handler(
                    servicer.version,
                    request_deserializer=version__pb2.request.FromString,
                    response_serializer=version__pb2.response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'falco.version.service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class service(object):
    """This service defines a RPC call
    to request the Falco version.
    """

    @staticmethod
    def version(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/falco.version.service/version',
            version__pb2.request.SerializeToString,
            version__pb2.response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)