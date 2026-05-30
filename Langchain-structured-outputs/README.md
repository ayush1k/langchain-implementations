# LangChain Structured Outputs

This directory explores various methods to extract structured data from LLMs using LangChain's `with_structured_output` method. It covers different ways to define schemas, including Pydantic models, TypedDicts, and raw JSON schemas.

## What We Learned

### 1. Schema Definitions
- **Pydantic Models**: Using `BaseModel` and `Field` to define robust schemas with validation and descriptions.
- **TypedDict**: Utilizing Python's `TypedDict` and `Annotated` for lightweight, type-hinted schema definitions.
- **JSON Schema**: Directly using dictionary-based JSON schemas to guide the model's output format.

### 2. The `with_structured_output` Method
- Learning how to bind a schema to a chat model (like Gemini) to ensure the `invoke` method returns a structured object (dictionary or Pydantic instance) instead of a raw string or message.

### 3. Metadata and Descriptions
- **Field Descriptions**: Using `Field(description=...)` in Pydantic or `Annotated[..., "description"]` in TypedDict to provide clear instructions to the LLM about what each field should contain.
- **Optional & Literal Types**: Implementing optional fields and fixed enumerations (e.g., `Literal['pos', 'neg']`) to refine the structured output.

### 4. Data Validation
- Basic exploration of how Pydantic handles type coercion and validation compared to standard dictionaries.

## Key Files
- `with_structured_output_pydantic.py`: Implementation using Pydantic models for extraction.
- `with_structured_output_typed_dict.py`: Implementation using TypedDict for extraction.
- `with_structured_output_json.py`: Implementation using raw JSON schema for extraction.
- `pydantic_demo.py`: Basic demonstration of Pydantic model usage.
- `typed_dict_demo.py`: Basic demonstration of TypedDict usage.
- `json_schema.json`: An external JSON schema example.
