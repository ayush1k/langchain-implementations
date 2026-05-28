# LangChain Prompts & Interaction Patterns

This directory explores how to structure inputs for LLMs, manage conversational state, and build user interfaces for LangChain applications.

## What We Learned

### 1. Message Structuring
- Understanding the three core message types in LangChain:
    - `SystemMessage`: Setting the behavior/persona of the AI.
    - `HumanMessage`: Capturing user input.
    - `AIMessage`: Representing the model's response.

### 2. Prompt Templates
- **Dynamic Prompts**: Using `PromptTemplate` to create reusable prompts with placeholders (e.g., `{paper_input}`, `{style_input}`).
- **Persistence**: Saving templates to `template.json` and loading them using `load_prompt` to separate prompt logic from code.

### 3. Conversational Memory
- Implementing basic **Chat History** by maintaining a list of interactions to provide context for subsequent model calls.

### 4. LangChain Expression Language (LCEL)
- Introduction to the pipe operator (`|`) to chain prompts and models together (`chain = template | model`), simplifying the execution flow.

### 5. Application Development
- **Streamlit Integration**: Building interactive web UIs for LLM tools (e.g., a Research Paper Summarizer) with inputs like select boxes and buttons.
- **Temperature Control**: Understanding how the `temperature` parameter affects the randomness and creativity of the model's output.

## Key Files
- `chatbot.py`: Basic stateful chat implementation.
- `messages.py`: Demonstrates the use of System, Human, and AI messages.
- `prompt_generator.py`: Creating and saving prompt templates.
- `prompt-ui.py`: A Streamlit application using LCEL and loaded templates.
- `template.json`: Externalized prompt configuration.
