import grpc

from Employee import employee_pb2
from Employee import employee_pb2_grpc

def get_employee(emp_id):
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = employee_pb2_grpc.GetEmployeeStub(channel)
        response = stub.Get(employee_pb2.EmployeeRequest(emp_id=emp_id))
    
    #print("Response Code: {}".format(response.response.StatusCode))
    print(response)

if __name__ == "__main__":
    empId = int(input("Enter employee Id to be searched :"))
    get_employee(empId)