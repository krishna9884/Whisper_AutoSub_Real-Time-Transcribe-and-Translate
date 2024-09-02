# speech-to-text

Real-time transcription using [faster-whisper](https://github.com/guillaumekln/faster-whisper)

![architecture](docs/architecture.png)

Accepts audio input from a microphone using a [Sounddevice](https://github.com/spatialaudio/python-sounddevice). By using [Silero VAD](https://github.com/snakers4/silero-vad)(Voice Activity Detection), silent parts are detected and recognized as one voice data. This audio data is converted to text using Faster-Whisper.

The HTML-based GUI allows you to check the transcription results and make detailed settings for the faster-whisper.

## Transcription speed

If the sentences are well separated, the transcription takes less than a second.
![TranscriptionSpeed](docs/transcription_speed.png)

Large-v2 model  
Executed with CUDA 11.7 on a NVIDIA GeForce RTX 3060 12GB.

## Installation

1. pip install .

## Usage

1. python -m speech_to_text
1. Select "App Settings" and configure the settings.
1. Select "Model Settings" and configure the settings.
1. Select "Transcribe Settings" and configure the settings.
1. Select "VAD Settings" and configure the settings.
1. Start Transcription

If you use the OpenAI API for text proofreading, set OPENAI_API_KEY as an environment variable.

## Notes

- If you select local_model in "Model size or path", the model with the same name in the local folder will be referenced.

## Demo

![demo](docs/demo.gif)


