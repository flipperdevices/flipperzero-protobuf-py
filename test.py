# import asyncio
#
# from async_protopy.clients.protobuf_client import FlipperProtobufClient
# from async_protopy.connectors.serial_connector import SerialConnector
#
#
# async def main():
#     async with FlipperProtobufClient(SerialConnector(url='/dev/tty.usbmodemflip_Pichopos1',
#     baud_rate=230400)) as proto:
#         response = await proto.system.power_info_request()
#
#         print(response)
#
#         while True:
#             await asyncio.sleep(1)
#
#             await proto.gui.send_input_event_request(key="DOWN", itype="PRESS")
#             await proto.gui.send_input_event_request(key="DOWN", itype="LONG")
#             await proto.gui.send_input_event_request(key="DOWN", itype="RELEASE")
#
# asyncio.run(main())
import logging
import asyncio

from async_protopy.connectors.serial_connector import SerialConnector
from async_protopy.clients.protobuf_client import FlipperProtobufClient
from async_protopy.commands.gui_commands import StartScreenStreamRequestCommand

# import logging
# import os
# import sys
# import asyncio
# from serial.serialutil import SerialException
#
# current_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(current_dir, 'flipperzero_protobuf_py'))
#
# from async_protopy.clients.protobuf_client import FlipperProtobufClient
# from async_protopy.commands.gui_commands import StartScreenStreamRequestCommand, StopScreenStreamRequestCommand
# from async_protopy.connectors.serial_connector import SerialConnector
#
# logging.basicConfig(level=logging.DEBUG)
#
# async def stream_screen():
#     try:
#         async with FlipperProtobufClient(SerialConnector(url='/dev/tty.usbmodemflip_Pichopos1'
#         , baud_rate=230400)) as proto:
#             stream_response = await proto.stream(StartScreenStreamRequestCommand())
#
#             last_data = None
#             async for data in stream_response:
#                 if not data.gui_screen_frame.data:
#                     logging.debug("Пустой кадр данных получен.")
#                     continue
#
#                 if last_data != data:
#                     logging.debug("Получен новый кадр, вывод данных.")
#                     print(data)  # вывод данных
#                     last_data = data
#
#     except SerialException as e:
#         logging.error(f"SerialException в stream_screen: {e}", exc_info=True)
#     except Exception as e:
#         logging.error(f"Ошибка в stream_screen: {e}", exc_info=True)
#
# # Основной запуск программы
# if __name__ == '__main__':
#     try:
#         asyncio.run(stream_screen())
#     except Exception as e:
#         logging.error(f"Ошибка в основной программе: {e}", exc_info=True)


async def stream_screen():
    async with FlipperProtobufClient(SerialConnector(url='/dev/tty.usbmodemflip_Pichopos1', baud_rate=230400)) as proto:
        stream_response = await proto.stream(StartScreenStreamRequestCommand(), command_id=0)
        await stream_response.__anext__()
        print(await stream_response.__anext__())
        print(await stream_response.__anext__())
        print(await stream_response.__anext__())

        last_data = None
        async for data in stream_response:
            if not data.gui_screen_frame.data:
                continue

            if last_data != data:
                print(data)  # display data
                last_data = data


if __name__ == '__main__':
    try:
        asyncio.run(stream_screen())
    except Exception as e:
        logging.error(f"Ошибка в основной программе: {e}", exc_info=True)
