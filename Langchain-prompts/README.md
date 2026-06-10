# LangChain Prompts

This directory explores how to structure inputs for LLMs, manage conversational state, and build user interfaces for LangChain applications. It focuses on the bridge between raw models and user-facing features.

## What We Learned

### 1. Advanced Prompt Templating
- **Dynamic Formatting**: Using `PromptTemplate` and `ChatPromptTemplate` for reusable, variable-driven inputs.
- **Role-Based Messaging**: Mastering the `('system', '...')`, `('human', '...')`, and `('ai', '...')` tuple syntax for structured chat prompts.
- **Partial Formatting**: Techniques for pre-filling parts of a prompt while leaving others dynamic.

### 2. Conversational State Management
- **Chat History**: Manually maintaining a list of `BaseMessage` objects to provide context to the LLM.
- **MessagesPlaceholder**: Using placeholders to dynamically inject variable-length chat history into the middle of a prompt template.
- **External Persistence**: Saving and loading chat history from local files (`chat_history.txt`).

### 3. LangChain Expression Language (LCEL)
- **Declarative Chains**: Using the pipe operator (`|`) to compose sequences: `chain = template | model | output_parser`.
- **Simplification**: How LCEL handles streaming, batching, and async calls out of the box.

### 4. Interactive Application Development
- **Streamlit UIs**: Building rapid prototypes with `streamlit`.
    - Using widgets (buttons, text inputs, select boxes) to control prompt parameters.
    - Displaying model responses and managing session state in a web browser.
- **Parameter Tuning**: Understanding the impact of `temperature` on model determinism and creativity.

## Key Files
- `chatbot.py`: A stateful, terminal-based chat implementation.
- `prompt-ui.py`: A Streamlit web application demonstrating LCEL and custom templates.
- `message_placeholder.py`: Detailed example of dynamic history injection.
- `prompt_generator.py`: Scripts for creating, saving (`template.json`), and loading prompt templates.
- `messages.py`: Exploration of the core `SystemMessage`, `HumanMessage`, and `AIMessage` classes.
