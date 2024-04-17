from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

server = SimpleXMLRPCServer(("localhost", 8000), logRequests=True)
server.register_function(factorial, "factorial_rpc")

try:
    print("Starting and listening on port 8000...")
    print("Press Ctrl + C to exit.")
    server.serve_forever()
except KeyboardInterrupt:
    print("Exit.")
