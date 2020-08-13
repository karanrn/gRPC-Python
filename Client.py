import grpc

from Employee import employee_pb2
from Employee import employee_pb2_grpc

def get_employee():
    emp_id = int(input("Enter employee Id to be searched :"))
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

def add_employee():
    emp = employee_pb2.Employee()
    emp.emp_id = int(input("Enter employee Id:"))
    emp.first_name = input("Enter employee first_name:")
    emp.last_name = input("Enter employee last_name:")
    emp.job_title = input("Enter employee job_title:")
    emp.dob = input("Enter employee date of birth (yyyy-mm-dd):")

    with grpc.insecure_channel('localhost:5000') as channel:
        stub = employee_pb2_grpc.EmployeeServiceStub(channel)
        response = stub.AddEmployee(emp)
    
    print(response)


if __name__ == "__main__":
    get_employee()
    print("------------------------------------------------")
    print("Get all employees:")
    get_employees()
    print("------------------------------------------------")
    add_employee()