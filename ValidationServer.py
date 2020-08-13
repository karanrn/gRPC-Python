import grpc
from concurrent import futures
import re

from Validation import validation_pb2
from Validation import validation_pb2_grpc

class ValidationService(validation_pb2_grpc.ValidationService):

    def ValidateName(self, request, context):
        pattern = re.compile('[A-Za-z]{2,25}( [A-Za-z]{2,25})?')
        
        result = validation_pb2.ValidateNameResponse()
        result.valid = bool(pattern.fullmatch(request.name))
        return result
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    validation_pb2_grpc.add_ValidationServiceServicer_to_server(ValidationService(), server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()