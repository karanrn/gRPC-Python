import grpc
from concurrent import futures

from Employee import employee_pb2
from Employee import employee_pb2_grpc
from Response import response_pb2
from Validation import validation_pb2
from Validation import validation_pb2_grpc

class EmployeeService(employee_pb2_grpc.EmployeeService):

    def GetEmployee(self, request, context):
        empResp = employee_pb2.EmployeeResponse()
        emp = employee_pb2.Employee(emp_id=1, 
                first_name='Karan',
                last_name='Nadagoudar',
                job_title='IT',
                dob='1994-08-11')
        empResp.employee.CopyFrom(emp)

        empResp.response.StatusCode = 200
        empResp.response.ResponseMessage = "Employee details of emp_id = {}".format(request.emp_id)

        return empResp
    
    def GetEmployees(self, request, context):
        for i in range(1, 11):
            emp = employee_pb2.Employee(emp_id=i, 
                first_name='Karan',
                last_name='Nadagoudar',
                job_title='IT',
                dob='1994-08-11')
            yield emp
    
    def AddEmployee(self, request, context):
        with grpc.insecure_channel('localhost:5001') as channel:
            stub = validation_pb2_grpc.ValidationServiceStub(channel)
            # Validate first_name
            validation_response = stub.ValidateName(validation_pb2.ValidateNameRequest(
                name=request.first_name
            ))

        empResp = employee_pb2.EmployeeResponse()
        empResp.employee.CopyFrom(request)

        if validation_response.valid:
            empResp.response.StatusCode = 200
            empResp.response.ResponseMessage = "Employee details of emp_id = {} \
is added.".format(request.emp_id)
        else:
            empResp.response.StatusCode = 400
            empResp.response.ResponseMessage = "Employee first_name is not valid, \
it should only contain alphabets."

        return empResp

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    employee_pb2_grpc.add_EmployeeServiceServicer_to_server(EmployeeService(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()