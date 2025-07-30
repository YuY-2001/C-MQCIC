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
@inproceedings{yu-etal-2025-cmqcic,
    title = "{CMQCIC}-Bench: A {C}hinese Benchmark for Evaluating Large Language Models in Medical Quality Control Indicator Calculation",
    author = "Yu, Guangya  and
      Li, Yanhao  and
      Jiang, Zongying  and
      Jin, Yuxiong  and
      Dai, Li  and
      Lin, Yupian  and
      Hou, Ruihui  and
      Zhang, Weiyan  and
      Fan, Yongqi  and
      Ye, Qi  and
      Liu, Jingping  and
      Ruan, Tong",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-acl.34/",
    pages = "609--626",
    ISBN = "979-8-89176-256-5",
    abstract = "Medical quality control indicators are essential to assess the qualifications of healthcare institutions for medical services. With the impressive performance of large language models (LLMs) like GPT-4 in the medical field, leveraging these technologies for the Medical Quality Control Indicator Calculation (MQCIC) presents a promising approach. In this work, (1) we introduce a real-world task MQCIC and propose an open-source Chinese electronic medical records (EMRs)-based dataset (CMQCIC-Bench) comprising 785 instances and 76 indicators. (2) We propose a semi-automatic method to enhance the rule representation. Then we propose the Clinical Facts-based Inferential Rule (CF-IR) method that disentangles the clinical fact verification and inferential rule reasoning actions. (3) We conduct comprehensive experiments on 20 representative LLMs, covering general and medical models. Our findings reveal that CF-IR outperforms Chain-of-Thought methods in MQCIC tasks. (4) We conduct an error analysis and investigate the capabilities of clinical fact verification and inferential rule reasoning, providing insights to improve performance in the MQCIC further. The dataset and code is available in this repository https://github.com/YuY-2001/C-MQCIC."
}
```
