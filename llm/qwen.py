from prompts import *

from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.generation import GenerationConfig


class QwenInfer:
    def __init__(self, model_path):
        self.model, self.tokenizer = self.load_models_tokenizer(model_path)
        pass

    def load_models_tokenizer(self, model_path):
        tokenizer = AutoTokenizer.from_pretrained(
            model_path, trust_remote_code=True
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            trust_remote_code=True,
        ).eval()
        model.generation_config = GenerationConfig.from_pretrained(
            model_path, trust_remote_code=True
        )
        model.generation_config.do_sample = True  # use greedy decoding
        model.generation_config.repetition_penalty = 1.5  # disable repetition penalty
        model.generation_config.top_k = 40
        model.generation_config.top_p = 0.99
        model.generation_config.temperature = 0
        return model, tokenizer

    def preprocess_prompt(self, question, choices, context=None):
        user_message_ = USER_MESSAGE.format(question=question, answer_choices=choices)
        if context is not None:
            user_message_ = USER_MESSAGE_WITH_CONTEXT_VER_2.format(context=context, question=question,
                                                                   answer_choices=choices)
        prompt = DEFAULT_PROMPT.format(user_message=user_message_)
        return prompt

    def call_api(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to("cuda") for k, v in inputs.items()}
        output = self.model.generate(**inputs, max_new_tokens=100)
        response_text = self.tokenizer.batch_decode(output, skip_special_tokens=True)
        return response_text

    def generate(self, question, choices, context=None):
        prompt = self.preprocess_prompt(question, choices, context)
        response_text = self.call_api(prompt)
        output = str(response_text[0].split("assistant")[-1]).strip()
        return output, prompt
