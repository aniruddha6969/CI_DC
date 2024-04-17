import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

try:
    print("Factorial of 3 is:", proxy.factorial_rpc(3))
    print("Factorial of 5 is:", proxy.factorial_rpc(5))
except Exception as e:
    print("Error:", e)
