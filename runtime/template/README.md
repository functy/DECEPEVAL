# Prompt Templates

The runtime uses only `judge.txt`. It is the single configurable prompt sent
to the judge model for both packaged subsets. `models/prompt_store.py` maps
the runtime's legacy lookup keys to this same file, so no additional judge
prompt files or judge models are required.
