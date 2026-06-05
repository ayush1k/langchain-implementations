# LangChain Output Parsers

This directory focuses on transforming the raw text output from LLMs into structured, usable data formats. It demonstrates various LangChain output parsers that handle everything from simple strings to complex Pydantic models.

## What We Learned

### 1. String and List Parsing
- Using `StrOutputParser` for clean text extraction.
- Handling comma-separated or list-based outputs.

### 2. JSON and Schema-Based Parsing
- Implementing `JsonOutputParser` to get predictable JSON structures.
- Providing `format_instructions` to prompts to guide the LLM's output format.

### 3. Pydantic Validation
- Using `PydanticOutputParser` to enforce strict data schemas.
- Defining `BaseModel` and `Field` with descriptions to help the LLM understand the required output.

### 4. Structured Output Parser
- Using `StructuredOutputParser` and `ResponseSchema` for multi-field data extraction without Pydantic.

## Key Files
- `str-output-parsers.py`: Demonstrates basic string and list parsing.
- `json-output-parser.py`: Shows how to extract data as JSON objects.
- `pydantic-output-parser.py`: Uses Pydantic for robust schema validation and parsing.
- `structured-output-parser.py`: Implements parsing using `ResponseSchema`.
