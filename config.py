import os

from dotenv import load_dotenv

load_dotenv()

ME5_TOKENIZER_PATH = os.getenv("ME5_TOKENIZER_PATH", "./weight/me5_tokenizer/")
ME5_MODEL_SMALL_PATH = os.getenv("ME5_MODEL_SMALL_PATH", "./weight/me5_model/me5_small.onnx")
VECTORSTORES_LOCAL = os.getenv("VECTORSTORES_LOCAL", "./.tmp_vectorstores")

MODEL_EMBEDDING_SIZE = {
    "me5-small": 384,
}
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "4"))