import requests
import json
from pathlib import Path

url = "https://api.chatkore.com/v1/audio/speech"

payload = json.dumps({
    "model": "tts-1",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy"  # 音色: alloy、echo、fable、onyx、nova和shimmer
})
headers = {
    'Authorization': 'Bearer sk-xxxx',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# 检查请求是否成功
if response.status_code == 200:
    # 设置保存音频文件的路径
    speech_file_path = Path(__file__).parent / "speech.mp3"
    # 以二进制写入模式打开文件
    with open(speech_file_path, 'wb') as f:
        # 写入响应的内容
        f.write(response.content)
    print(f"语音文件已保存到 {speech_file_path}")
else:
    # 如果请求失败，打印状态码和响应文本
    print(f"获取语音失败。状态码: {response.status_code}")
    print(response.text)
