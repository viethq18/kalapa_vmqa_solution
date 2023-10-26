DEFAULT_PROMPT = """<|im_start|>system\nYou are a helpful assistant. From now you are expert in Medical Health Care and helpful answers to questions from humans in Vietnamese.<|im_end|>
<|im_start|>user\n{user_message}<|im_end|>
<|im_start|>assistant\n"""

USER_MESSAGE = """Please answer the following multiple choice questions, each question has 2 to 6 options, of which at least one is correct:

Question: {question}

Multi answer choices:\n{answer_choices}

For each question with multi choices, you need to return a json answer, where the key of the json is the ith choice and the value is is 0 if the ith choice in the question is false and vice versa.
Please output your answer in JSON format,:
{{  "A": "", 
    "B": "", 
    "C": "", 
    "D": "", 
    "E": "", 
    "F": "", }}
"""

USER_MESSAGE_WITH_CONTEXT = """Please answer the following multiple choice questions based on the given context, each question has 2 to 6 options, of which at least one is correct:

Context:\n{context}

Question: {question}

Multi answer choices:\n{answer_choices}

For each question with multi choices, you need to return a json answer, where the value is is 0 if the key choice in the question is false and vice versa.
Please output your answer in JSON format,:
{{  "A": "", 
    "B": "", 
    "C": "", 
    "D": "", 
    "E": "", 
    "F": "", }}
"""
