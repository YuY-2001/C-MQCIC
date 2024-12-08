# C-MQCIC
The dataset for C-MQCIC, an chinese open-source dataset for medical quality control indicator calculation

Requirement

We release the code with GPT call. If use the vllm or transformers, please read the related reference.

must
openai >= 1.43.0

tqdm 

# Quick start
bash main.sh

set your openai key in funtion

def send_chat_completion_request(model_name, message_content,temperature=0.01):

    key = "Bearer {key}" #set your keys

