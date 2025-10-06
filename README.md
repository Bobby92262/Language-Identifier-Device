# Language-Identifier-Device

 ## Project Overview
The project aims to build an IoT device that identifies spoken language from individuals and/or groups. Initial audio input will be via a USB microphone, with plans to replace it with an electret microphone circuit for cost efficiency. Audio processing by a Raspberry Pi 4 using Whisper, an open-source automatic speech recognition (ASR) model.

### Tech Stack
1.Python
2.Whisper by OpenAI
3.Raspberry Pi 4 - RaspPi OS Lite
4.Electret Microphone Circuit

*Some additional parts of the project that would be nice to incorporate / research implementation.*
5. Containerisation - Docker ? Podman ?
6. Pytorch
7. NVIDIA container toolkit (CUDA Toolkit)

### Development Plan
- [x] Research Iteration 1 Implementation
- [x] RaspberryPi set up.
- [ ] Virtual Enviroment set up with Whisper installed. (Desktop Version) Test WhisperAI.
- [ ] Implement on the Pi after testing above is done.
- [ ] Review if processing on the edge ?
- [ ] Circuit construct for electret microphone.
- [ ] Container to be set up once chosen entity (Docker/**Podman**).
- [ ] Implement circuit with the Pi and test capabilities.
- [ ] Review Pytorch implementation and GPU accelartion.

### Iteration Checklist
- [ ] First Iteration - Desktop with USB Microphone and WhisperAI
- [ ] Second Iteration - RaspPi with USB Microphone.
- [ ] Thrid Iteration - Circuit constructed and implemented with Pi.
- [ ] Container with image created.
- [ ] Pytorch with GPu accelrated.

### Project Methodology 
- An Agile methodology and the Kipling methodology will be used for this project.
- 2 week sprints for work with diary to be updated every sprint.

### Side notes
- OpenAI need 'FFmpeg' in the backgrpund to convert audio file types.
