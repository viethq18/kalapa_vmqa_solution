# kalapa_vmqa_solution

## Getting started
```
git clone https://github.com/viethq18/kalapa_vmqa_solution.git
```
### Installing
`pip install -r requirements.txt`

### Download embedding model me5 from Huggingface and convert to onnx
`git clone https://huggingface.co/intfloat/multilingual-e5-small`
`python convert_onnx.py`

### Embed Medical Corpus into Vector Storage
`python embed_corpus.py`

### Run local
`python main.py`
