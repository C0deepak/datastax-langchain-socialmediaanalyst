from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-vqiZz": {
    "background_color": "",
    "chat_icon": "",
    "files": "",
    "input_value": "what type of post should I post to get more engagement?",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "ParseData-EtrR9": {
    "sep": "\n",
    "template": "{text}"
  },
  "Prompt-W1BaD": {
    "context": "",
    "question": "",
    "template": "{context}\n\n---\nYou are a social media analytics assistant trained to analyze and compare post performance across various types of content. You are provided with structured data for social media posts in JSON format. The data includes realistic engagement metrics and attributes for different post types. Your task is to provide insightful and optimized textual responses to user queries.\n\nKey Guidelines for Responses:\nAlways reference specific metrics from the data.\nUse comparative language to highlight differences between post types.\nProvide insights that are actionable, e.g., “To improve engagement, focus on using hashtags like #viral and #trending.”\nGive numbering words in percentage or figure for comparison to different post types\n\nQuestion: {question}\n\nAnswer: "
  },
  "SplitText-2q7Aj": {
    "chunk_overlap": 200,
    "chunk_size": 7800,
    "separator": "\n"
  },
  "OpenAIModel-O0saY": {
    "api_key": OPENAI-API-KEY,
    "input_value": "",
    "json_mode": False,
    "max_tokens": None,
    "model_kwargs": {},
    "model_name": "gpt-4o",
    "openai_api_base": "",
    "output_schema": {},
    "seed": 1,
    "stream": True,
    "system_message": "",
    "temperature": 0.1
  },
  "ChatOutput-sEZH2": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "AstraDB-o9XYR": {
    "advanced_search_filter": "{}",
    "api_endpoint": "https://83dc40c9-9923-4581-ae1d-1ad52dd9ff1d-us-east-2.apps.astra.datastax.com",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "random_data",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "ASTRA_DB_APPLICATION_TOKEN"
  },
  "AstraDB-0e8yl": {
    "advanced_search_filter": "{}",
    "api_endpoint": "https://83dc40c9-9923-4581-ae1d-1ad52dd9ff1d-us-east-2.apps.astra.datastax.com",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "random_data",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "ASTRA_DB_APPLICATION_TOKEN"
  },
  "OpenAIEmbeddings-tIHF8": {
    "chunk_size": 1000,
    "client": "",
    "default_headers": {},
    "default_query": {},
    "deployment": "",
    "dimensions": None,
    "embedding_ctx_length": 1536,
    "max_retries": 3,
    "model": "text-embedding-3-small",
    "model_kwargs": {},
    "openai_api_base": "",
    "openai_api_key": OPENAI-API-KEY,
    "openai_api_type": "",
    "openai_api_version": "",
    "openai_organization": "",
    "openai_proxy": "",
    "request_timeout": None,
    "show_progress_bar": False,
    "skip_empty": False,
    "tiktoken_enable": True,
    "tiktoken_model_name": ""
  },
  "File-24pzY": {
    "concurrency_multithreading": 4,
    "path": "random_post_data.csv",
    "silent_errors": False,
    "use_multithreading": False
  },
  "Google Generative AI Embeddings-wEOJd": {
    "api_key": GENERATIVEAI-API-KEY,
    "model_name": "models/text-embedding-004"
  },
  "GoogleGenerativeAIModel-lzKWL": {
    "google_api_key": GENERATIVEAI-API-KEY,
    "input_value": "",
    "max_output_tokens": 10000,
    "model": "gemini-1.5-flash",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 0.1,
    "top_k": None,
    "top_p": None
  },
  "AnthropicModel-BnSOy": {
    "anthropic_api_key": ANTHROPIC-API-KEY,
    "anthropic_api_url": "",
    "input_value": "",
    "max_tokens": 4096,
    "model": "claude-3-5-sonnet-latest",
    "prefill": "",
    "stream": False,
    "system_message": "",
    "temperature": 0.1
  },
  "GroqModel-YnRl4": {
    "groq_api_base": "https://api.groq.com",
    "groq_api_key": "",
    "input_value": "",
    "max_tokens": None,
    "model_name": "llama-3.1-8b-instant",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 0.1
  },
  "OpenAIEmbeddings-u3mNf": {
    "chunk_size": 1000,
    "client": "",
    "default_headers": {},
    "default_query": {},
    "deployment": "",
    "dimensions": None,
    "embedding_ctx_length": 1536,
    "max_retries": 3,
    "model": "text-embedding-ada-002",
    "model_kwargs": {},
    "openai_api_base": "",
    "openai_api_key": OPENAI-API-KEY,
    "openai_api_type": "",
    "openai_api_version": "",
    "openai_organization": "",
    "openai_proxy": "",
    "request_timeout": None,
    "show_progress_bar": False,
    "skip_empty": False,
    "tiktoken_enable": True,
    "tiktoken_model_name": ""
  },
  "Google Generative AI Embeddings-mqtj9": {
    "api_key": GENERATIVEAI-API-KEY,
    "model_name": "models/text-embedding-004"
  },
  "GoogleGenerativeAIModel-47sLK": {
    "google_api_key": GENERATIVEAI-API-KEY,
    "input_value": "",
    "max_output_tokens": 2000000,
    "model": "gemini-1.5-flash",
    "n": None,
    "stream": True,
    "system_message": "you are a data scientist",
    "temperature": 0.1,
    "top_k": None,
    "top_p": None
  },
  "GroqModel-kTC4G": {
    "groq_api_base": "https://api.groq.com",
    "groq_api_key": GROQ-API-KEY,
    "input_value": "",
    "max_tokens": None,
    "model_name": "llama-3.1-8b-instant",
    "n": None,
    "stream": False,
    "system_message": "give helpful data insights",
    "temperature": 0.1
  },
  "AIMLEmbeddings-AZ4FC": {
    "aiml_api_key": AIML-API-KEY,
    "model_name": "text-embedding-3-small"
  },
  "Google Generative AI Embeddings-4QpfI": {
    "api_key": GENERATIVEAI-API-KEY,
    "model_name": "models/text-embedding-004"
  }
}

result = run_flow_from_json(flow="Untitled document.json",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)