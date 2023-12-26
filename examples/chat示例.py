from openai import OpenAI

client = OpenAI(
    # 输入转发API Key
    api_key="sk-xxxxxxx",
    base_url="https://api.chatkore.com/v1/chat/completions"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    stream=True  # 是否开启流式输出
)

# 非流式输出获取结果
# print(completion.choices[0].message)
# 流式输出获取结果
for chunk in completion:
    print(chunk.choices[0].delta)
