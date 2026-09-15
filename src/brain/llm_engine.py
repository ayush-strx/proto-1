import os
from dotenv import load_dotenv
from llama_cpp import Llama

load_dotenv()

MODEL_PATH = os.getenv("LLM_MODEL_PATH")

llm = Llama(model_path=MODEL_PATH, verbose=False, n_ctx=512)


def ask_llm(prompt, max_tokens=20):
    response = llm(prompt, max_tokens=max_tokens, stop=["\n"])
    return response["choices"][0]["text"].strip()