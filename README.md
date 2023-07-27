# chatkore
chatkore本意即为开发者提供优质稳定的OpenAI相关的API调用接口，方便国内用户使用各类开源ChatGPT项目或者AI领域的库的使用。有任何问题请加QQ群联系客服：群号[742077418](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=tUZP9cQ-wRDjYNMwZjvs7maNyixcIYB5&authKey=dzF1K7fXUdg%2BMf8zLoPp9L%2F9bvhkoVpyWQoZoEFW0WLeinAmx2OOHBGZfqAjrikl&noverify=0&group_code=742077418)  
官网：[https://www.chatkore.com](https://www.chatkore.com)  
免部署版网页端现已上线：[https://www.chatkore.com/chat](https://www.chatkore.com/chat)，现已支持GPT3.5和GPT4的切换，GPT4没有每3小时25条消息的限制。无需翻墙，国内网络即可体验，注册即送100积分。

### 相比OpenAI的主要优势
- 不限制国内使用，可以用支付宝付款，没有封号风险。
- 无需代理即可访问，没有墙的阻拦。
- 支持GPT4，并且没有每3小时25条消息的限制。
- 无需代理即可访问，没有墙的阻拦。
- 无需代理即可访问，没有墙的阻拦。
- 兼容OpenAI接口格式，可以做到平替。支持vscode插件，支持autoGPT，agentGPT。API用法也可参考[官方文档](https://platform.openai.com/docs/api-reference/introduction)
- 无最低消费金额与最低充值金额，可以作为本地测试开发的完美替代品。
- 新增对Embeddings支持，可以用接口运行AutoGPT等应用。

### 变更日志
2023-06-15: 支持gpt-4-0613，gpt-3.5-turbo-0613，gpt-3.5-turbo-16k，gpt-3.5-turbo-16k-0613新模型，支持函数调用功能。  

### 使用[chatgpt-web](https://github.com/Chanzhaoyu/chatgpt-web)项目配置
##### 修改service/.env文件
- 设置OPENAI_API_KEY环境变量为chatkore后台获取的Key
- 设置OPENAI_API_BASE_URL环境变量为：https://api.chatkore.com/v1
- 由于网络延迟，建议把TIMEOUT_MS设置为180000或者更高

### chatkore-API接入文档
##### API介绍
API通过HTTP请求调用。每次请求，需要在HTTP头中携带用户的Token，用于认证。当认证成功，系统会检查用户账户余额，如果余额不足，则返回错误。

##### HTTP请求认证
所有HTTP请求使用API Token进行认证。用户注册后，可以在首页找到自己的Token。在每一次API请求时，将Token带在Header中进行认证。请保护好你的Token！不要将自己的Token共享给他人或直接保存在客户端的代码中。
所有API请求都应该包括API Token在Authorization HTTP Header中，比如：
> Authorization: Bearer YOUR_API_TOKEN

##### 请求示例
以下是一个API请求的示例。记住将$API_TOKEN替换为你自己的API Key。
curl：
```
curl https://api.chatkore.com/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization:  Bearer $API_TOKEN" \
    -d '{
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.7
    }'
```
      
Python：
```
import requests
URL = 'https://api.chatkore.com/v1/chat/completions'
resp = requests.post(URL, json={
    'model': 'gpt-3.5-turbo',
    'messages': [{'role': 'user', 'content': '回复这是一个测试'}],
    'temperature': 0,
}, headers={
    'Authorization': " Bearer $API_TOKEN"
})
print(resp.json())
```
      
这个请求将调用gpt-3.5-turbo模型，完成对话。你将会得到类似如下的返回结果：
```
{
  "id":"chatcmpl-abc123",
  "object":"chat.completion",
  "created":1677858242,
  "model":"gpt-3.5-turbo-0301",
  "usage":{
      "prompt_tokens":13,
      "completion_tokens":7,
      "total_tokens":20
  },
  "choices":[
      {
        "message":{
            "role":"assistant",
            "content":"\n\nThis is a test!"
        },
        "finish_reason":"stop",
        "index":0
      }
  ]
}
```
      
### 主要接口介绍-聊天
##### 聊天对话
给定一个聊天对话，模型将返回一个聊天回答响应。
创建聊天对话
> POST https://api.chatkore.com/v1/chat/completions

##### 请求参数
**model** 类型: string必填  
要使用的模型ID。您可以使用"列出所有模型"API查看所有可用的模型，或查看我们的Model overview了解它们的描述。  
**messages** 类型: array必填  
生成聊天的提示消息，格式为JSON对象，包含以下字段：  
role：角色，可以是system, assitant，或者是user  
content：信息的内容  
**temperature** 类型: float可选 默认: 1  
要使用的采样温度，介于0和2之间。较高的值（例如0.8）会使输出更随机，而较低的值（例如0.2）会使其更加集中和确定性。  
**top_p** 类型: float可选 默认: 1  
与温度一起采样的替代方法，称为核心采样，其中模型考虑具有top_p概率质量的令牌的结果。因此，0.1表示仅考虑组成前10％概率质量的令牌。  
**n** 类型: int可选 默认: 1  
要为每个提示生成的答案数。  
**max_tokens** 类型: int可选 默认: inf  
对话最多可以生成的令牌数。  
**presence_penalty** 类型: float可选 默认: 0  
介于-2.0和2.0之间的数字。正值会根据新令牌是否出现在迄今为止的文本中对其进行惩罚，增加模型谈论新主题的可能性。  
**frequency_penalty** 类型: float可选 默认: 0  
介于-2.0和2.0之间的数字。正值会根据迄今为止的文本中的现有频率惩罚新令牌，降低模型重复同一行的可能性。  

### 主要接口介绍-模型
##### 列出所有模型
列出所有可以使用的模型，以及模型的基本信息。想了解模型可以做什么，模型间有什么不同，请参考OpenAI文档。
> GET https://api.chatkore.com/v1/models

### 主要接口介绍-文本转向量
##### 文本转向量 Embeddings
计费说明：text-embedding-ada-002 模型的 Token 价格是 gpt-3.5-turbo 的六分之一，我们已动态折算为积分，请以积分为准。每次请求最低消费 4积分。
> POST https://api.chatkore.com/v1/embeddings
Node.js示例
```
const fetch = require("node-fetch");
fetch("https://api.chatkore.com/v1/embeddings", {
  method: "POST",
  headers: {
    Authorization: "Bearer 你的api_key",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    input: "哈哈哈哈哈",
    model: "text-embedding-ada-002",
  }),
});
```
##### 请求参数
**model** 类型: string必填  
固定为 text-embedding-ada-002 专用于文本转向量  
**input** 类型: string 或者 array
输入要嵌入的文本，编码为字符串或令牌数组。要在单个请求中嵌入多个输入，请传递字符串数组或令牌数组。每个输入不得超过模型的最大输入标记（text-embedding-ada-002为8191个标记）。  
返回示例
```
{
    "object": "list",
    "data": [
    {
        "object": "embedding",
        "embedding": [
            0.0023064255,
            -0.009327292,
            .... (1536 floats total for ada-002)
            -0.0028842222,
        ],
        "index": 0
    }
    ],
    "model": "text-embedding-ada-002",
    "usage": {
        "prompt_tokens": 8,
        "total_tokens": 8
    }
}
```

### 主要接口介绍-会话补充
##### 会话补完
会话补完是指根据用户的输入，自动补全对话。这个功能可以用于聊天机器人、自动问答等场景。
创建补完对话
> POST https://api.chatkore.com/v1/completions

##### 请求参数
**model** 类型: string必填  
要使用的模型ID。您可以使用"列出所有模型"API查看所有可用的模型，或查看我们的Model overview了解它们的描述。  
**prompt** 类型: string或者array可选  
要生成对话的提示，编码为字符串、字符串数组、令牌数组或令牌数组的数组。  
**suffix** 类型: string可选  
插入文本完成后的后缀。  
**max_tokens** 类型: int可选 默认: 16  
对话最多可以生成的令牌数。  
**temperature** 类型: float可选 默认: 1  
要使用的采样温度，介于0和2之间。较高的值（例如0.8）会使输出更随机，而较低的值（例如0.2）会使其更加集中和确定性。  
**top_p** 类型: float可选 默认: 1  
与温度一起采样的替代方法，称为核心采样，其中模型考虑具有top_p概率质量的令牌的结果。因此，0.1表示仅考虑组成前10％概率质量的令牌。  
**n** 类型: int可选 默认: 1  
要为每个提示生成的答案数。
