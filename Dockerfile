# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY library_pb2.py library_pb2.py
COPY library_pb2_grpc.py library_pb2_grpc.py
COPY server.py server.py
COPY client.py client.py

# Install necessary packages
RUN pip install grpcio grpcio-tools prometheus_client

# Expose the gRPC and Prometheus ports
EXPOSE 50051
EXPOSE 8000

# Command to run the gRPC server
CMD ["python", "server.py"]
