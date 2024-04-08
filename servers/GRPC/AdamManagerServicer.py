# adam_manager_server.py
import os

import grpc
from concurrent import futures
import adam_manager_pb2
import adam_manager_pb2_grpc

from adam_sdk import AdamManager
from adam_sdk import MotorCommand
from adam_sdk import SerializableCommands


class AdamManagerServicer(adam_manager_pb2_grpc.AdamManagerServiceServicer):
    def __init__(self, adam_manager_instance):
        self.adam_manager_instance = adam_manager_instance

    def HandleCommand(self, request, context):
        try:
            serializable_commands = SerializableCommands(
                motors=[MotorCommand(
                    name=cmd.name,
                    goal_position=cmd.goal_position,
                    speed=cmd.speed
                ) for cmd in request.motors]
            )
            type(serializable_commands)
            print(serializable_commands)
            self.adam_manager_instance.handle_command(serializable_commands)
            return adam_manager_pb2.EmptyResponse()
        except Exception as e:
            return adam_manager_pb2.EmptyResponse()

    def ReturnToStartPosition(self, request, context):
        return adam_manager_pb2.EmptyResponse()

    def Move(self, request, context):
        print(request.linear_velocity, request.angular_velocity)
        self.adam_manager_instance.move(request.linear_velocity, request.angular_velocity)
        return adam_manager_pb2.EmptyResponse()


def serve():
    adam_manager_instance = AdamManager()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    adam_manager_pb2_grpc.add_AdamManagerServiceServicer_to_server(AdamManagerServicer(adam_manager_instance), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
