from typing import AsyncGenerator

from async_protopy.flipperzero_protobuf_compiled import flipper_pb2
from async_protopy.exceptions.base_exceptions import FlipperValidateException
from async_protopy.commands.base_command import BaseCommand
from async_protopy.executor import FlipperProtoExecutor


class FlipperBaseProtoClient:
    """The base flipper protobuf client.

    Implements methods to work with flipper via the protobuf protocol.

    Attributes:
        executor: FlipperProtoExecutor
    """

    def __init__(self, executor: FlipperProtoExecutor):
        self.executor = executor

    async def stream(self, command: BaseCommand, command_id: int = None) -> AsyncGenerator:
        """Streams data from the flipper.

        Sends the given command to the flipper and returns an async generator object.

        Args:
            command: BaseCommand

        Returns:
            An async generator of response data from the flipper
        """
        return await self.executor.execute_command(command=command, command_id=command_id)

    async def request(
        self, command: BaseCommand, command_id: int = None, wait_for_response: bool = True, to_validate: bool = True
    ) -> flipper_pb2.Main:
        """Request data from the flipper.

        Sends the given command to the flipper and returns the first received data from the stream

        Args:
            command: BaseCommand
            command_id: int
                A command id of the executed command, increasing at a command execution if it's not passed.
            wait_for_response: bool
                A flag used to wait for the response data or return after the command is sent (default is True)
            to_validate: bool
                A flag used to validate the response data or not (default is True)

        Returns:
            A response data from the flipper

        Raises:
            FlipperValidateException: And error occurred validating the response command status
        """
        response = await self.executor.execute_command(command=command, command_id=command_id)

        if not wait_for_response:
            return

        async for data in response:
            if to_validate and data.command_status != 0:
                raise FlipperValidateException(
                    f'Command status is not equal to 0, given command type: {type(command)}; '
                    f'method name: {command.method_name}; proto class: {command.proto_class} '
                    f'status: {data.command_status}; command id: {command_id}'
                )

            return data
