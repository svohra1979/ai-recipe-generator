# AI Recipe Generator

AI Recipe Generator is a lightweight Streamlit application that turns available ingredients into a practical recipe recommendation based on cuisine, dietary preference, and fitness goals. It is designed to help users quickly generate meal ideas without requiring a full recipe database or manual planning.

## Overview

The application accepts a list of ingredients and a few user preferences, then uses the Google Gemini API to generate a short recipe that matches the selected criteria. It is intended for everyday cooking support, meal planning, and rapid recipe ideation.

## Features

- Ingredient-based recipe generation
- Cuisine selection
- Dietary preference filtering
- Fitness goal-aware portion and calorie guidance
- Simple, browser-based interface using Streamlit
- Lightweight configuration through environment variables

## Technology Stack

- Python
- Streamlit
- Google GenAI SDK
- python-dotenv

## Project Structure

- `streamlit_app.py` — Streamlit UI and recipe generation logic
- `.env.example` — sample environment configuration
- `requirements.txt` — Python dependencies
- `README.md` — project documentation

## Setup

1. Create and activate a virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example` and add your Gemini API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

4. Run the app:

```bash
streamlit run streamlit_app.py
```

## Usage

1. Enter the ingredients you have available.
2. Select the cuisine, diet, and fitness goal.
3. Enter your weight.
4. Click the generate button to produce a recipe suggestion.

## Notes

This project is best suited for personal or prototype use. The generated recipe is intentionally concise and focused on practical suggestions rather than long-form meal planning.
