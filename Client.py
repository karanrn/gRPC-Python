import grpc

from Employee import employee_pb2
from Employee import employee_pb2_grpc

def get_employee(emp_id):
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = employee_pb2_grpc.EmployeeServiceStub(channel)
        # Unary response
        response = stub.GetEmployee(employee_pb2.EmployeeRequest(emp_id=emp_id))

    print(response)

def get_employees():
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = employee_pb2_grpc.EmployeeServiceStub(channel)
        # Stream Response
        for resp in stub.GetEmployees(employee_pb2.Empty()):
            print(resp)

if __name__ == "__main__":
    empId = int(input("Enter employee Id to be searched :"))
    get_employee(empId)
    print("Get all employees:")
    get_employees()