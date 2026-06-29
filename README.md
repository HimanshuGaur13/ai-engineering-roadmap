# Employee Salary Processing System

Production-style Python backend mini project.

## Features

- CSV processing
- Data cleaning
- Salary analysis
- JSON export
- Logging
- Exception handling
- Config management

## Tech Stack

- Python
- Pandas
- Logging
- JSON



# Employee Management Backend API

Production-style backend API built using FastAPI.

## Features

- CRUD APIs
- JWT Authentication
- Protected Routes
- Request Validation
- Service Layer
- Clean Architecture
- Logging
- Postman Testing

## Tech Stack

- Python
- FastAPI
- JWT
- Pydantic
- Uvicorn

```
ai-engineering-roadmap
├─ README.md
├─ week1-python-foundation
│  ├─ app.py
│  ├─ config.py
│  ├─ data
│  │  ├─ cleaned.csv
│  │  ├─ employee.json
│  │  ├─ employee_report.json
│  │  ├─ employees.csv
│  │  ├─ output.txt
│  │  ├─ sample.txt
│  │  └─ test.csv
│  ├─ models
│  │  ├─ developer.py
│  │  ├─ employee.py
│  │  └─ manager.py
│  ├─ notebooks
│  │  └─ notebook.ipynb
│  ├─ requirements.txt
│  ├─ salary_analyzer.py
│  ├─ test.py
│  ├─ tests
│  │  └─ test_salary_analyzer.py
│  └─ utils
│     ├─ __init__.py
│     ├─ calculator.py
│     ├─ custom_exceptions.py
│     ├─ data_cleaner.py
│     ├─ file_handler.py
│     ├─ json_handler.py
│     ├─ logger.py
│     ├─ report_generator.py
│     └─ validators.py
├─ week2-fastapi
│  ├─ app.py
│  ├─ config.py
│  ├─ database
│  │  ├─ connection.py
│  │  └─ models.py
│  ├─ requirements.txt
│  ├─ routes
│  │  ├─ auth_routes.py
│  │  └─ employee_routes.py
│  ├─ schemas
│  │  ├─ employee_schema.py
│  │  ├─ response_schema.py
│  │  └─ user_schema.py
│  ├─ services
│  │  ├─ auth_service.py
│  │  └─ employee_service.py
│  └─ utils
│     ├─ auth_handler.py
│     ├─ custom_exceptions.py
│     ├─ jwt_handler.py
│     ├─ logger.py
│     └─ password_handler.py
├─ week3_ai_ml_foundation
│  ├─ Notes
│  │  ├─  day3-embeddings.md
│  │  ├─ day1-ai-fundamentals.md
│  │  ├─ day2-nlp.md
│  │  └─ day4-document-search.md
│  ├─ README.md
│  ├─ __init__.py
│  ├─ create_embeddings.py
│  ├─ datasets
│  │  ├─ documents.csv
│  │  ├─ knowledge_base
│  │  │  ├─ fastapi.txt
│  │  │  ├─ python.txt
│  │  │  └─ rag.txt
│  │  ├─ reviews.csv
│  │  └─ sample_texts.txt
│  ├─ experiments
│  │  ├─ embeddings_demo.py
│  │  ├─ semantic_search_demo.py
│  │  └─ similarity_demo.py
│  ├─ main.py
│  ├─ models
│  │  └─ search_result.py
│  ├─ requirements.txt
│  ├─ services
│  │  ├─ __init__.py
│  │  ├─ embedding_service.py
│  │  ├─ faiss_retrieval_service.py
│  │  ├─ retrieval_service.py
│  │  ├─ search_service.py
│  │  └─ vector_store_service.py
│  ├─ utils
│  │  ├─ file_loader.py
│  │  ├─ similarity_helper.py
│  │  └─ text_preprocessor.py
│  └─ vector_store
│     ├─ document_embeddings.npy
│     └─ faiss_index.bin
├─ week4_llm_engineering
│  ├─ __init__.py
│  ├─ app.py
│  ├─ chatbots
│  ├─ config
│  │  ├─ __init__.py
│  │  └─ settings.py
│  ├─ experiments
│  │  ├─ __init__.py
│  │  ├─ chatbot.py
│  │  ├─ faq_assistant.py
│  │  ├─ first_llm_call.py
│  │  ├─ function_calling.py
│  │  └─ json_output.py
│  ├─ notes
│  │  ├─ day1-llm-fundamentals.md
│  │  ├─ day2-tokens-context.md
│  │  ├─ day3-prompt-engineering.md
│  │  └─ day4-openai-api.md
│  ├─ prompt
│  │  └─ prompts.py
│  ├─ requirements.txt
│  └─ services
│     ├─ __init__.py
│     └─ llm_service.py
└─ week5_rag
   ├─ __init__.py
   ├─ documents
   │  └─ company_policy.txt
   ├─ experiments
   │  ├─ __init__.py
   │  └─ rag_chat.py
   ├─ services
   │  ├─ __init__.py
   │  ├─ embedding_service.py
   │  ├─ rag_service.py
   │  └─ vector_store_service.py
   └─ utils
      ├─ chunker.py
      └─ document_loader.py

```