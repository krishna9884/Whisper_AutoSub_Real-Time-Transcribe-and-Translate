import os
import asyncio
import websockets

async def send_audio_file(audio_file, server_url):
    try:
        async with websockets.connect(server_url) as websocket:
            if os.path.exists(audio_file):
                with open(audio_file, "rb") as f:
                    audio_data = f.read()

                # Send the audio data to the server
                await websocket.send(audio_data)

                print(f"Audio file '{audio_file}' sent to the server for transcription.")

                # Receive and print the transcription results from the server
                transcription_results = await websocket.recv()
                print("Transcription Results:", transcription_results)
            else:
                print(f"Audio file '{audio_file}' not found.")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    server_url = "tcp://8.tcp.ngrok.io:17762"  # Replace with your server's address and port
    audio_file_path = "sample-2.mp3"  # Replace with the path to your audio file

    asyncio.get_event_loop().run_until_complete(send_audio_file(audio_file_path, server_url))
