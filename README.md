# C-MQCIC

C-MQCIC is an open-source Chinese dataset for medical quality control indicator calculation. We will release all the experiment results in the future.

## Requirements

The released code utilizes GPT calls. If you intend to use `vllm` or `transformers`, please refer to the relevant documentation.

### Dependencies
- `openai >= 1.43.0`
- `tqdm`

## Quick Start

Run the following command:

```bash
bash main.sh

def send_chat_completion_request(model_name, message_content, temperature=0.01):
    key = "Bearer {key}"  # Set your API key here

```
---

## Acknowledgments and References
Thanks to the following open-source projects for their support:
- **Transformers**: [GitHub - huggingface/transformers](https://github.com/huggingface/transformers)  
- **vLLM**: [GitHub - vllm-project/vllm](https://github.com/vllm-project/vllm)  
- **llama-factory** [Github - llama-factory](https://github.com/hiyouga/LLaMA-Factory)
---
