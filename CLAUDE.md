# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Python 3.12, managed with `uv`.

- Install: `uv sync`
- Run: `uv run main.py`
- Lint / format: `uv run ruff check .` / `uv run ruff format .`
- Tests: none exist yet.

## Architecture

Single-script LangChain course project; all code is in `main.py`. It follows the standard LCEL flow: `load_dotenv()` → `PromptTemplate` → LLM → `chain.invoke({...})`. API keys are loaded from `.env` (never read or print it).

Installed provider packages: `langchain-openai`, `langchain-anthropic`, `langchain-openrouter`; `langsmith` is for tracing.

## Git

Commit to `dev`, not `main` (see the parent `/Users/ai/Documents/CLAUDE.md` for the full workflow, including the "wait for go ahead" planning rule).

## Known issues in `main.py` (unfixed)

- `chain = summary_template | llm` pipes the raw string; it should use `summary_prompt_template`.
- `input_variables=["inforamtion"]` is misspelled and doesn't match the `{information}` placeholder.
- `OpenAI` is the completion LLM and returns a `str`, so `response.content` fails; `ChatOpenAI` returns a message object.
