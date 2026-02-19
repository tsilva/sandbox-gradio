# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a sandbox repository for experimenting with the Gradio library (v5.0.0+), containing examples demonstrating various Gradio features and patterns. The repository is organized by feature categories with standalone Python scripts that can be run independently.

## Environment Setup

The project uses a conda environment with PyTorch, Transformers, and Gradio:

```bash
# Activate environment (creates if needed)
source activate-env.sh

# Or manually
conda env create -f environment.yml
conda activate gradio-sandbox
```

Environment includes:
- Python 3.10
- PyTorch with CUDA 11.8 support
- Transformers library
- Gradio >= 5.0.0

## Running Examples

Each Python file in the repository is a standalone Gradio application that can be run directly:

```bash
python <path-to-example>.py
```

The application will launch and provide a local URL (typically http://127.0.0.1:7860) to interact with the interface.

## Repository Structure

The codebase is organized into feature-specific directories, each containing standalone examples:

- **basic/** - Fundamental Gradio patterns (calculators, state management, live updates, image/webcam inputs)
- **chat/** - ChatInterface examples (multimodal I/O, streaming, theming, thinking step-by-step, user feedback)
- **blocks/** - Low-level Blocks API examples (buttons, input changes, multiple flows)
- **layouts/** - UI layout patterns (rows, columns, tabs, accordions, visibility control, fill-height)
- **events/** - Event handling (multiple bindings, decorators, selection events, chaining with `.then()`)
- **flows/** - Data flow patterns (lambda inputs, structured I/O, component creation, skip logic)
- **state/** - State management examples (browser state, session state)
- **javascript/** - Client-side JavaScript integration with Gradio
- **styling/** - Custom CSS and styling examples
- **render/** - Dynamic component rendering with `@gr.render` decorator
- **timer/** - Periodic/timer-based updates
- **usecases/** - Complete applications (audio mixer, speech sentiment, tic-tac-toe, todo list)
- **block_functions/** - Using Gradio spaces as functions via `gr.load()`

## Key Gradio Concepts

### Two Main APIs

1. **Interface API** (`gr.Interface`) - High-level, declarative API for simple input/output applications
2. **Blocks API** (`gr.Blocks`) - Low-level API for complex layouts and interactions

### Chat Interface

`gr.ChatInterface` is specialized for chat applications. Messages use `type="messages"` format with `ChatMessage` objects that support metadata (status, duration, titles) for features like thinking/reasoning displays.

### Event Handling

Events can be bound using:
- Method chaining: `component.click(fn, inputs, outputs)`
- Decorators: `@component.click(inputs, outputs)`
- `.then()` for sequential operations

### JavaScript Integration

The `js` parameter allows running client-side JavaScript before or instead of server-side Python functions. Useful for preprocessing or pure frontend operations.

### State Management

- **Session State**: `gr.State()` for per-user persistent data
- **Global State**: Regular Python variables (shared across all users)
- **Browser State**: `gr.BrowserState()` for storing data in the browser

### Dynamic Rendering

The `@gr.render` decorator enables conditional component creation based on state or inputs.

## Important Notes

- Each example is self-contained and can be run independently
- Examples demonstrate specific features rather than best practices for production apps
- Some examples (like `block_functions/`) may require external Gradio spaces or models to function
- The TODO in README.md references learning about Gradio's queuing system: https://www.gradio.app/guides/queuing
- README.md must be kept up to date with any significant project changes
