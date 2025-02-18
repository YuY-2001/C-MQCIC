# C-MQCIC

C-MQCIC is an open-source Chinese dataset for medical quality control indicator calculation. We will release all the experiment results in the future.

# The example of the medical quality control indicator calculation

![task_new_00](https://github.com/user-attachments/assets/6ef83434-4c1e-41d1-9d87-1620d00dfe19){:width="30px" height="auto"}


# The overview of CF-IR
![framework_00](https://github.com/user-attachments/assets/80ed6737-880e-4146-bd0f-735b31516e47)


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

