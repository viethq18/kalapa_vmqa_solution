DEFAULT_PROMPT = """<|im_start|>system\n你是一个有用的助手。你是由 VillaLabs 开发的，目的是理解越南语，用越南语为人类提出的问题提供详细、礼貌和有用的答案。<|im_end|>
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

USER_MESSAGE_WITH_CONTEXT_VER_2 = """根据越南语中有关与医疗问题相关的疾病的背景，通过选择相关字母来确定合适的答案。每个问题都会向您提供 2 到 6 个选项，标记为 A、B、C、D、E、F。

语境：\n{context}

问题： {question}

多答案选择：\n{answer_choices}

从给定的上下文中提取答案，即使问题包含误导性或无关的细节。请注意，有些问题可能有多个准确答案，而其他问题可能只有一个。为了清楚起见，仅输出选择的标签，您的答案可以采用以下格式：
例子：
如果 A 是正确答案，则必须回答：A
如果 A 和 B 都是正确答案，则必须回答：A、B
如果 B、D、E 都是正确答案，则必须回答：B、D、E
...

不要使用我给你的这些例子，你必须自己回答这个问题。
"""