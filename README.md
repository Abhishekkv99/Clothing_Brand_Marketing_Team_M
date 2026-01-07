# Clothing Brand Marketing Team 👗

A multi-agent system built with [crewAI](https://crewai.com) to handle the research and strategy for fashion campaigns. It automates the process of analyzing trends, brainstorming content, and reviewing the final strategy.

## How it works

This project uses a hierarchical crew setup with three distinct roles:

*   **Lead Market Research Analyst**: Uses search tools to find current fashion trends and competitor insights for Gen Z/Millennial markets.
*   **Creative Content Specialist**: Takes those insights and crafts content strategies, including Instagram and TikTok copy.
*   **Senior Marketing Manager**: Coordinates the team, reviews the work, and ensures everything hits the brand's sustainability and style marks.

The Manager oversees the whole flow, providing a final executive summary once the research and creative work are done.

## Getting Started

### 1. Requirements
- Python 3.12 or higher
- An [OpenAI API Key](https://platform.openai.com/)
- A [Serper API Key](https://serper.dev/) (for web search)

### 2. Installation
You can use `pip` or `uv` to install dependencies.

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using uv:**
```bash
uv sync
```

### 3. Setup
1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```
2. Open `.env` and add your API keys.

### 4. Running the Crew
Kick off the campaign planning by running the main script:

```bash
python src/marketing_team/main.py
```

## Changing the Topic

To run research for a different collection, just update the `topic` in `src/marketing_team/main.py`:

```python
inputs = {
    'topic': 'Minimalist Urban Spring 2026'
}
```

## Configuration

If you want to change agent personalities or task requirements, you don't need to touch the code. Just edit the YAML files in `src/marketing_team/config/`:
- `agents.yaml`: Change roles, goals, and backstories.
- `tasks.yaml`: Define exactly what each agent should produce.

## Structure

- `src/marketing_team/crew.py`: Core logic and agent assembly.
- `src/marketing_team/main.py`: Entry point and input handling.
- `src/marketing_team/config/`: YAML configs for agents and tasks.
- `requirements.txt` & `uv.lock`: Dependency management.
