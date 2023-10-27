import json
import re

import pandas as pd
from langchain.vectorstores.chroma import Chroma

import config
from embedding.embedding import mE5Embedding
from llm.qwen import QwenInfer
from utils import litm_reordering

medical_corpus_db = Chroma(collection_name="kalapa_medical_corpus_clean",
                           embedding_function=mE5Embedding(),
                           persist_directory=config.VECTORSTORES_LOCAL,
                           collection_metadata={"hnsw:space": "cosine"})

qwen_model = QwenInfer()
embedding_model = mE5Embedding()


def write_log(question, choices, context, prompt, output, output_json):
    with open("./logs.txt", "a+") as f:
        f.write(f"Context:\n{context}\n")
        f.write(f"Question: {question}\n")
        f.write(f"Choices:\n{choices}\n")
        f.write(f"Prompt:\n{prompt}\n")
        f.write(f"Output: {output}\n")
        f.write(f"Output JSON: {output_json}\n")
        f.write("------------------------------------------------------------------------------\n")


def process_single_row(row):
    question = row["question"].strip()
    list_answer = [str(row["option_1"]), str(row["option_2"]), str(row["option_3"]), str(row["option_4"]),
                   str(row["option_5"]), str(row["option_6"])]
    tmp_ans = []
    for c, a in zip(["A.", "B.", "C.", "D.", "E.", "F."], list_answer):
        if a in ["nan", ""]:
            continue
        if a.startswith(c):
            tmp_ans.append(a)
            continue
        tmp_ans.append(f"{c} {a}")
    answer_choices = "\n".join(tmp_ans)
    return question, answer_choices, len(tmp_ans)


def get_context(question, top_k, use_litm=True, use_mmr=False):
    embedding_vector = embedding_model.embed_documents([f"query: {question}"])
    if use_mmr:
        docs = medical_corpus_db.max_marginal_relevance_search_by_vector(embedding_vector[0], k=top_k)
    else:
        docs = medical_corpus_db.similarity_search_by_vector(embedding_vector[0], k=top_k)
    context = [doc.page_content for doc in docs]
    if use_litm:
        context = litm_reordering(context)
    return "\n".join([c.replace("passage: ", "") for c in context])


def process_output(output, num_ans):
    """Hard code, will remove later"""
    res = ""
    MAP_ANS = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f"}
    output = re.split(r"[.,、]", output)
    output = [c.lower() for c in output if len(c)]
    print("OUTPUT: ", output)
    for i in range(num_ans):
        if MAP_ANS[i] in output:
            res += "1"
        else:
            res += "0"
    print(res)
    return res


def main():
    df = pd.read_csv("./KALAPA_ByteBattles_2023_MEDICAL_Set1/MEDICAL/public_test.csv")
    result = {"id": [], "answer": []}
    for index, row in df.iterrows():
        result["id"].append(row["id"].strip())
        question, choices, num_choices = process_single_row(row)
        context = get_context(question, top_k=5)
        output, prompt = qwen_model.generate(question, choices, context)
        print(output)
        output_json = process_output(output, num_choices)
        result["answer"].append(output_json)

        write_log(question, choices, context, prompt, output, output_json)

    newdf = pd.DataFrame(result, dtype=str)
    newdf.to_csv("./sample_submission.csv", index=False)


if __name__ == "__main__":
    main()
