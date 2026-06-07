# LangChain Runnables

This directory explores the LangChain Expression Language (LCEL) through various `Runnable` primitives. It demonstrates how to compose complex chains using sequences, parallel execution, conditional branching, and custom functions.

## What We Learned

### 1. Chain Composition with RunnableSequence
- Using `RunnableSequence` to chain multiple components where the output of one step becomes the input of the next.
- Explicitly composing prompts, LLMs, and output parsers into a unified pipeline.

### 2. Parallel Execution with RunnableParallel
- Executing multiple chains or runnables simultaneously on the same input.
- Structuring output data into dictionaries for multi-modal processing (e.g., generating a tweet and a LinkedIn post concurrently).

### 3. Conditional Logic with RunnableBranch
- Implementing dynamic routing within chains based on specific conditions.
- Combining `RunnableBranch` with `RunnablePassthrough` to either transform data or pass it along unchanged based on logic.

### 4. Custom Logic with RunnableLambda
- Integrating custom Python functions into LCEL chains using `RunnableLambda`.
- Performing on-the-fly transformations such as calculating word counts or data cleaning within a sequence.

### 5. State Management with RunnablePassthrough
- Passing data through a chain step without modification.
- Using `RunnablePassthrough` to preserve original inputs for later stages in a parallel or branched execution.

## Key Files
- `runnable-sequence.py`: Demonstrates basic sequential chaining of prompts and models.
- `runnable-parallel.py`: Shows how to generate multiple outputs (tweet and LinkedIn post) in parallel.
- `runnable-lambda.py`: Illustrates integrating custom Python logic for word count analysis.
- `runnable-branch.py`: Implements conditional summarization logic based on text length.
- `runnable-passthrough.py`: Demonstrates preserving state across different parts of a chain.
