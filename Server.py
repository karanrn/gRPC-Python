import grpc
from concurrent import futures

from Employee import employee_pb2
from Employee import employee_pb2_grpc
from Response import response_pb2

class EmployeeDB(employee_pb2_grpc.GetEmployeeServicer):

    def Get(self, request, context):
        empResp = employee_pb2.EmployeeResponse()
        empResp.employee.emp_id = 420
        empResp.employee.first_name = "Karan"
        empResp.employee.job_title = "IT"
        empResp.employee.dob = "1994-08-11"

        empResp.response.StatusCode = 200
        empResp.response.ResponseMessage = "Employee details of emp_id = {}".format(request.emp_id)

        return empResp

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    employee_pb2_grpc.add_GetEmployeeServicer_to_server(EmployeeDB(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()