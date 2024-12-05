import json
def write_jsonl(file_path, data):
    with open(file_path, 'w',encoding='utf-8') as file:
        for json_obj in data:
            json_line = json.dumps(json_obj,ensure_ascii=False)
            file.write(json_line + '\n')
def write_json(file_path, data):
    with open(file_path, 'w',encoding='utf-8') as file:
         json.dump(data,file,indent = 4, ensure_ascii=False)
         
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            json_obj = json.loads(line.strip())
            data.append(json_obj)
    return data
def read_json(file_path):
    with open(file_path, 'r',encoding = 'utf-8') as file:
        data = json.load(file)
    return data

import requests
def send_chat_completion_request(model_name, message_content,temperature=0.01):
    url = "https://openkey.cloud/v1/chat/completions" 
    key = "Bearer sk-mZp0p3SXEhftBKa17eB64c5957F54d8886DaFf9e88655262"
    headers = {"Content-Type": "application/json","Authorization":key} 
    data = { 
        "model": model_name, 
        "messages": [{"role":"system","content":'你是一个专业的医学质控专家，你具备丰富的医学知识和质控知识。请你遵循指令完成任务。\n###'}
                     ,{"role": "user", "content": message_content}],
                     "temperature": temperature,
                     }  
      
    # 将Python字典转换为JSON格式的字符串  
    json_data = json.dumps(data)  
    try:  
        # 发送POST请求  
        response = requests.post(url, headers=headers, data=json_data)  
        
        # 检查响应状态码，如果成功则返回响应内容，否则抛出异常  
        if response.status_code == 200:  
            return response.json()["choices"][0]["message"]["content"]  
        else:  
            raise Exception(f"Request failed with status {response.status_code}: {response.text}")  
    except Exception as e:
        return f"An error occurred: {type(e).__name__} - {e}"
    
def chat_method(model, content):   
    return send_chat_completion_request(model,content)

import re

def extract_last_yes_or_no_or_not_sure(text):
    if not isinstance(text, (str, bytes)):
        text = str(text) if text is not None else ""
    # 匹配最后一个 "Yes"、"No" 或 "Not Sure" 及其对应含义
    matches = re.findall(r'(是|正确|符合|Yes|True|不是|不|错误|不符合|No|False|无法判断|无法确定|Not Sure)', text, re.IGNORECASE)
    if matches:
        last_match = matches[-1]  # 获取最后一个匹配的值
        # 根据最后的匹配内容返回标准化结果
        if re.match(r'(是|正确|符合|Yes|True)', last_match, re.IGNORECASE):
            return "Yes"
        elif re.match(r'(不是|不|错误|不符合|No|False)', last_match, re.IGNORECASE):
            return "No"
        elif re.match(r'(无法判断|无法确定|Not Sure)', last_match, re.IGNORECASE):
            return "No"
    return "No Answer"  # 如果没有匹配到任何值



from tqdm import tqdm
def process(data,type,indicators):
    if type == "standard":
        instruction = "\n###Instrcution: 这是一个指标计算任务，你需要根据给定的指标要求来对电子病历进行判断，你需要给出病历当中相关的信息作为解释。接下来，我将给你电子病历、指标要求、补充说明。\n###最后输出：Yes/No/Not Sure.\n###输入："
        input_form = "#指标要求:{}\n#补充说明:{}"
    elif type == "cot":
        instruction = "\n###Instrcution: 这是一个指标计算任务，你需要根据给定的指标要求来对电子病历进行判断，你需要给出病历当中相关的信息作为解释。接下来，我将给你电子病历、指标要求、补充说明。请你一步步思考，给出具体的依据和推理过程。\n###最后输出：Yes/No/Not Sure\n###输入："
        input_form = "#指标要求:{}\n#补充说明:{}"
    elif type == "generate":
        instruction = "\n###Instrcution: 这是一个指标计算任务，你需要根据给定的指标要求来对电子病历进行判断。 \n###Step1 知识补充：请你根据指标要求和补充说明生成相关的医学知识。\n###Step2 规则拆分：请你根据指标要求、补充说明和医学知识拆分为子Rules， \n###Step3 从子rules中抽取需要判断的facts。\n###Step4 逻辑表达生成：我希望你生成Logical Rules（逻辑表达式），来对Rules和facts之间进行整合。其中，Rules是对指标要求的进一步细化；Facts则是每一个Rules当中需要去判断的内容，其值可以为True/False的判断，也可以是具体的数值或阴性/阳性等；Logical Rules则是基于Facts的结果进行逻辑运算，并得到最后的判断结果，每个Logical Rules包含自然语言表述和一个对应的符号语言表述。\n###Step5 事实判断：请你根据电子病历判断Facts的值，需要给出具体的fact在原文中的体现,如果没有，认为无法判断。\n###Step6 逻辑推理：基于每个Logical Rules推理得到最终结果。\n###最后输出：Yes/No/Not Sure.\n###输入："
        input_form = "#指标要求:{}\n#补充说明:{}"
    else:
        instruction = "\n###Instrcution: 这是一个指标计算任务，你需要根据给定的指标要求来对电子病历进行判断。\n###Step1 事实判断：请你根据电子病历判断Facts的值，不要做任何假设，需要给出具体的fact在原文中的体现，如果没有，认为无法判断。\n###Step2 逻辑推理：基于每个Logical Rules推理得到最终结果。其中，Rules是对指标要求的进一步细化；Facts则是每一个Rules当中需要去判断的内容，其值可以为True/False的判断，也可以是具体的数值或阴性/阳性等；Logical Rules则是基于Facts的结果进行逻辑运算，并得到最后的判断结果，每个Logical Rules包含自然语言表述和一个对应的符号语言表述。\n###Step3 最后输出：Yes/No/Not Sure.\n###输入："
        input_form = "#Facts:{}\n#Logical Rules:{}"
    count = 0 
    for i in tqdm(range(len(data))):
        instance = data[i]
        indicator = indicators[instance["unique_id"]]
        if type == "CF-IR":
            input = input_form.format(
                indicator['facts'],
                indicator['logical_rules']
                )
        else:
            input = input_form.format(
                indicator['question_rule'],
                indicator['other']
                )
        content = instruction + input + "\n###病历："+ instance['patient note']
        try:
            output = chat_method(model,content)
        except:
            output = 'no answer'
        label = extract_last_yes_or_no_or_not_sure(output)
        data[i]['output'] = output 
        data[i]['predict_label'] = label
        if label == instance['label']:
            count += 1
    acc = count / len(data) 
    acc = count / len(data) 
    print(f'type:{type} acc:{acc}') 
          
    return data
# import sys
# model = sys.argv[1] 
model = 'gpt-4o-2024-08-06'
types = ["standard","cot","CF-IR"]

indicators = read_json('./dataset/indicator.json')
dataset_path = './dataset/data.jsonl'
for type in types: 
    print(f'{type}_{model},starting')
    dataset = read_jsonl(dataset_path)
    new_data = process(dataset[:2],type,indicators)
    save_path = f'./result/{model}_{type}_zero-shot.jsonl'
    write_jsonl(save_path,new_data)
    print(f'{type}_{model},end')