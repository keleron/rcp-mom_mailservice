FROM python:slim
COPY helloworld.proto helloworld.proto 
COPY client.py client.py
RUN pip3 install grpcio
RUN pip3 install grpcio-tools
RUN python3 -m grpc_tools.protoc helloworld.proto --proto_path=. --python_out=. --grpc_python_out=.