# pip install modelscope
from modelscope import snapshot_download

snapshot_download('iic/CosyVoice-300M', local_dir='models/TTS/CosyVoice-300M')

snapshot_download('qwen/Qwen1.5-0.5B-Chat', local_dir='models/LLM/Qwen1.5-0.5B-Chat')

snapshot_download('AI-ModelScope/XTTS-v2', local_dir='models/TTS/XTTS-v2')
# snapshot_download('keepitsimple/faster-whisper-large-v3', local_dir='models/ASR/whisper')