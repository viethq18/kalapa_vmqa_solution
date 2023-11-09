from prompts import *
import requests


class QwenInfer:
    def __init__(self):
        pass

    def preprocess_prompt(self, question, choices, context=None):
        user_message_ = USER_MESSAGE.format(question=question, answer_choices=choices)
        if context is not None:
            user_message_ = USER_MESSAGE_WITH_CONTEXT_VER_2.format(context=context, question=question,
                                                             answer_choices=choices)
        prompt = DEFAULT_PROMPT.format(user_message=user_message_)
        return prompt

    def call_api(self, prompt):
        url = "http://localhost:8000/generate"
        headers = {'Content-Type': 'application/json'}
        pload = {
            "prompt": prompt,
            "n": 1,
            "best_of": 1,
            "use_beam_search": False,
            "temperature": 0,
            "presence_penalty": 1.5,
            "frequency_penalty": 0,
            "top_p": 1,
            "top_k": -1,
            "max_tokens": 100,
            "ignore_eos": True,
            "stop": ["<|endoftext|>"],
            "stream": False,
            # "logprobs": 0
        }
        response = requests.post(url, headers=headers, json=pload)
        response_text = response.json()["text"]
        return response_text

    def generate(self, question, choices, context=None):
        prompt = self.preprocess_prompt(question, choices, context)
        response_text = self.call_api(prompt)
        output = str(response_text[0].split("assistant")[-1]).strip()
        return output, prompt
