<div align="center">
  <img src="logo.png" alt="sandbox-gradio" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
  [![Gradio](https://img.shields.io/badge/Gradio-5.0+-orange.svg)](https://gradio.app/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **🎨 A hands-on collection of Gradio examples for learning interactive ML interfaces ⚡**

  [Gradio Docs](https://gradio.app/docs/) · [Gradio Guides](https://www.gradio.app/guides)
</div>

## Overview

A sandbox repository for experimenting with the Gradio library (v5.0.0+). Contains 50+ standalone examples organized by feature category, demonstrating patterns from basic calculators to complete applications like chat interfaces, tic-tac-toe, and audio mixers.

## Features

- **Blocks API** - Low-level control over layouts and interactions
- **ChatInterface** - Streaming, multimodal, thinking step-by-step patterns
- **Event Handling** - Decorators, chaining with `.then()`, selection events
- **State Management** - Session, global, and browser state examples
- **Dynamic Rendering** - Conditional components with `@gr.render`
- **JavaScript Integration** - Client-side preprocessing and custom behavior

## Quick Start

```bash
# Clone the repository
git clone https://github.com/tsilva/sandbox-gradio.git
cd sandbox-gradio

# Create and activate conda environment
conda env create -f environment.yml
conda activate gradio-sandbox

# Run any example
python basic/calculator.py
```

Open http://127.0.0.1:7860 in your browser.

## Installation

### Using Conda (Recommended)

```bash
conda env create -f environment.yml
conda activate gradio-sandbox
```

### Using the Activation Script

```bash
source activate-env.sh
```

This script creates the environment if needed and activates it.

### Environment Includes

- Python 3.10
- PyTorch with CUDA 11.8 support
- Transformers library
- Gradio >= 5.0.0

## Examples

### Basic

| Example | Description |
|---------|-------------|
| `calculator.py` | Simple arithmetic operations |
| `session_state.py` | Per-user persistent data |
| `global_state.py` | State shared across users |
| `live_updates.py` | Real-time input processing |
| `image_input.py` | Image upload handling |
| `webcam_streaming.py` | Live webcam feed |

### Chat

| Example | Description |
|---------|-------------|
| `streaming_responses.py` | Token-by-token output |
| `multimodal_inputs.py` | Text + image inputs |
| `thinking_step_by_step.py` | Reasoning with metadata |
| `user_feedback.py` | Like/dislike responses |
| `theming.py` | Custom chat appearance |

### Layouts

| Example | Description |
|---------|-------------|
| `layout_columns.py` | Multi-column layouts |
| `layout_tabs_accordions.py` | Tabbed interfaces |
| `layout_fillheight.py` | Full-height components |
| `layout_column_visibility.py` | Show/hide sections |

### Events

| Example | Description |
|---------|-------------|
| `events_then.py` | Chaining with `.then()` |
| `events_selection.py` | Handle component selection |
| `events_multiple_bindings_decorators.py` | Decorator syntax |

### Use Cases

| Example | Description |
|---------|-------------|
| `tic_tac_toe.py` | Interactive game |
| `audio_mixer.py` | Audio processing app |
| `speech_sentiment.py` | Speech analysis |
| `todo_list.py` | Task management |

## Repository Structure

```
sandbox-gradio/
├── basic/          # Fundamental patterns
├── blocks/         # Low-level Blocks API
├── chat/           # ChatInterface examples
├── events/         # Event handling patterns
├── flows/          # Data flow patterns
├── javascript/     # JS integration
├── layouts/        # UI layout patterns
├── render/         # Dynamic @gr.render
├── state/          # State management
├── styling/        # Custom CSS
├── timer/          # Periodic updates
├── usecases/       # Complete applications
└── block_functions/ # gr.load() usage
```

## Key Concepts

### Two Main APIs

1. **Interface API** (`gr.Interface`) - High-level, declarative for simple I/O
2. **Blocks API** (`gr.Blocks`) - Low-level for complex layouts

### Event Binding

```python
# Method chaining
button.click(fn, inputs=[textbox], outputs=[output])

# Decorators
@button.click(inputs=[textbox], outputs=[output])
def handle_click(text):
    return process(text)

# Sequential operations
button.click(step1, ...).then(step2, ...).then(step3, ...)
```

### State Types

```python
# Per-user session state
state = gr.State(initial_value)

# Browser-persisted state
browser_state = gr.BrowserState(key="user_prefs")
```

## Contributing

Each example is self-contained and demonstrates a specific feature. To add a new example:

1. Create a Python file in the appropriate directory
2. Include a complete, runnable Gradio app
3. Focus on demonstrating one concept clearly

## License

MIT

## TODO

- [ ] Learn about [Gradio's queuing system](https://www.gradio.app/guides/queuing)
