# LangChain Structured Outputs

This directory explores robust methods for extracting predictable, machine-readable data from LLMs using LangChain's `with_structured_output` method. It demonstrates how to transform unstructured text into validated objects.

## What We Learned

### 1. Schema-First Extraction
- **Pydantic Models**: Defining schemas with `BaseModel` for automatic type validation and coercion.
- **TypedDict**: Using Python 3.8+ `TypedDict` for lightweight, dictionary-based schemas with type hints.
- **Raw JSON Schema**: Defining constraints using standard JSON Schema dictionaries, useful for cross-language compatibility.

### 2. Prompt Engineering for Extraction
- **Field Descriptions**: Utilizing `Field(description=...)` (Pydantic) or `Annotated[..., "description"]` (TypedDict) to provide the LLM with semantic context for each field.
- **Enums & Literals**: Restricting model outputs to specific sets of values (e.g., `Literal['positive', 'negative']`) to ensure consistency.
- **Optionality**: Handling missing or null data using `Optional` types.

### 3. Practical Use Cases
- **Review Analysis**: Extracting sentiment, key themes, pros, and cons from complex product reviews (e.g., Samsung Galaxy S24 Ultra).
- **Entity Extraction**: Identifying names and specific attributes from natural language.

### 4. Comparison of Methods
- **Validation**: Pydantic's strict validation vs. TypedDict's lean structure.
- **Usage**: When to use bound methods (`model.with_structured_output(Schema)`) for guaranteed output formats.

## Key Files
- `with_structured_output_pydantic.py`: Advanced extraction using Pydantic models.
- `with_structured_output_typed_dict.py`: Lightweight extraction using TypedDict.
- `with_structured_output_json.py`: Schema-driven extraction using raw JSON dictionaries.
- `pydantic_demo.py` & `typed_dict_demo.py`: Basic entry points for understanding these Python features.
- `json_schema.json`: Example of a standalone schema definition.
