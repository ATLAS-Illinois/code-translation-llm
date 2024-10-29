from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class HFModelLoader:
    def __init__(self, model_name="Qwen/CodeQwen-7B-Chat", device="cuda" if torch.cuda.is_available() else "cpu"):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).to(self.device)

    def generate_code(self, prompt, max_length=150):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(inputs["input_ids"], max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
