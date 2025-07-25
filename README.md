# C-MQCIC

C-MQCIC is an open-source Chinese dataset for medical quality control indicator calculation. We will release all the experiment results in the future.

# Data available

https://huggingface.co/datasets/YuY2001/CMQCIC

# Explanation of files

<img width="1647" height="1079" alt="image" src="https://github.com/user-attachments/assets/b93073f0-a6e6-480d-a370-0f10614f7e4f" />


# The example of the medical quality control indicator calculation

<img src="https://github.com/user-attachments/assets/6ef83434-4c1e-41d1-9d87-1620d00dfe19" alt="task_new_00" width="50%" />

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

## Citation

```
@inproceedings{ye2025imqc,
  title={IMQC: A Large Language Model Platform for Medical Quality Control},
  author={Ye, Qi and Yu, Guangya and Liu, Jingping and Chen, Erzhen and Dong, Chenjie and Lin, Xiaosheng and Liu, Zelei and Yu, Han and Ruan, Tong},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={39},
  number={28},
  pages={28810--28818},
  year={2025}
}
@article{Yu2025CMQCICBenchAC,
  title={CMQCIC-Bench: A Chinese Benchmark for Evaluating Large Language Models in Medical Quality Control Indicator Calculation},
  author={Guangya Yu and Yanhao Li and Zongying Jiang and Yuxiong Jin and Li Dai and Yupian Lin and Ruihui Hou and Weiyan Zhang and Yongqi Fan and Qi Ye and Jingping Liu and Tong Ruan},
  journal={ArXiv},
  year={2025},
  volume={abs/2502.11703},
  url={https://api.semanticscholar.org/CorpusID:276409291}
}
```
