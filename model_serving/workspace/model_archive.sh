torch-model-archiver --model-name lyric_align --version 1.0 --model-file my_model/pytorch_model.bin --handler handler.py --extra-files "my_model/config.json, my_tokenizer/added_tokens.json, my_tokenizer/preprocessor_config.json, my_tokenizer/special_tokens_map.json, my_tokenizer/tokenizer_config.json, my_tokenizer/vocab.json, demus.py, forced_alignment.py, get_lyric_song.py, lyric_align.py, result_to_json.py, util.py" --export-path model_store
