# Async Flipper Zero Protobuf Client

## [Test PyPi](https://test.pypi.org/project/async-protopy/0.0.0/)

## Base use example:
```python
import asyncio

from async_protopy.clients.protobuf_client import FlipperProtobufClient
from async_protopy.connectors.serial_connector import SerialConnector

async def main():
    async with FlipperProtobufClient(SerialConnector(url='/dev/tty.usbmodemflip_name', baud_rate=230400)) as proto:
        response = await proto.system.power_info_request()

        print(response)

        while True:
            await asyncio.sleep(1)

            await proto.gui.send_input_event_request(key="DOWN", itype="PRESS")
            await proto.gui.send_input_event_request(key="DOWN", itype="SHORT")
            await proto.gui.send_input_event_request(key="DOWN", itype="RELEASE")

asyncio.run(main())
```

## Create your own methods:
- stream data
```python
from async_protopy.clients.protobuf_client import FlipperProtobufClient
from async_protopy.commands.gui_commands import StartScreenStreamRequestCommand
from async_protopy.connectors.serial_connector import SerialConnector


async def stream_screen():
    async with FlipperProtobufClient(SerialConnector(url='/dev/tty.usbmodemflip_name', baud_rate=230400)) as proto:
        stream_response = await proto.stream(StartScreenStreamRequestCommand())

        last_data = None
        async for data in stream_response:

            if not data.gui_screen_frame.data:
                continue

            if last_data != data:
                print(data)  # display data
                last_data = data
```

- request data

```python
from async_protopy.clients.protobuf_client import FlipperProtobufClient
from async_protopy.commands.gui_commands import StopScreenStreamRequestCommand
from async_protopy.connectors.serial_connector import SerialConnector

async def stop_screen_stream():
    async with FlipperProtobufClient(SerialConnector(url='/dev/tty.usbmodemflip_name', baud_rate=230400)) as proto:
        response = await proto.request(
            StopScreenStreamRequestCommand(),
            wait_for_response=True,
            to_validate=True
        )
```
