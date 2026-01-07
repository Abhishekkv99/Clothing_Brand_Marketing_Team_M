# Clothing Brand Marketing Team Crew

This project implements a multi-agent marketing team using the CrewAI framework.

## Structure

- **Manager**: Senior Marketing Manager (orchestrates and reviews)
- **Researcher**: Market Research Analyst (gathers data)
- **Creator**: Content Specialist (creates content)

The process is **Hierarchical**, meaning the Manager oversees the execution and ensures quality.

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Set up environment variables:
    -   Copy `env.example` to `.env`.
    -   Add your `OPENAI_API_KEY` (required for agents).
    -   Add your `SERPER_API_KEY` (required for search tool).

3.  Run the Crew:
    ```bash
    python src/marketing_team/main.py
    ```

## Customization

-   **Agents**: defined in `src/marketing_team/config/agents.yaml`.
-   **Tasks**: defined in `src/marketing_team/config/tasks.yaml`.
-   **Logic**: defined in `src/marketing_team/crew.py`.

