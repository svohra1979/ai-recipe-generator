import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

MODEL_NAME = "gemini-3.8-flash"

st.set_page_config(
    page_title="AI Recipe Generator",
    page_icon="🍽️",
    layout="centered",
)

st.title("AI Recipe Generator")
st.caption("Turn the ingredients you have into a recipe that fits your goals.")


def get_client() -> genai.Client:
    """Create the Gemini client after the user submits the form."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing from your .env file.")
    return genai.Client(api_key=api_key)


def generate_recipe(
    ingredients: list[str],
    cuisine: str,
    diet: str,
    goal: str,
    weight: float,
) -> str:
    prompt = f"""
Generate one practical recipe using these ingredients: {", ".join(ingredients)}.

Cuisine: {cuisine}
Diet: {diet}
Fitness goal: {goal}
Weight: {weight:g} kg

Respect the dietary preference. Adjust the approximate calorie level and
portion guidance for the fitness goal. Include a recipe name, ingredients,
short instructions, and approximate calories. Keep the complete response
under 100 words. Do not include medical advice.
"""

    interaction = get_client().interactions.create(
        model=MODEL_NAME,
        input=prompt,
    )
    return interaction.output_text


with st.form("recipe_form"):
    ingredients_text = st.text_input(
        "Ingredients",
        placeholder="chicken, basil, garlic, tomatoes",
    )

    cuisine = st.selectbox(
        "Cuisine",
        ["Any", "Italian", "Indian", "Mexican", "Chinese", "Mediterranean"],
    )

    diet = st.selectbox(
        "Diet",
        ["Any", "Vegan", "Vegetarian", "Carnivore"],
    )

    goal = st.selectbox(
        "Goal",
        ["Maintain weight", "Gain weight", "Lose weight"],
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=75.0,
        step=0.5,
    )

    submitted = st.form_submit_button("Generate Recipe", type="primary")

if submitted:
    ingredients = [
        ingredient.strip()
        for ingredient in ingredients_text.split(",")
        if ingredient.strip()
    ]

    if not ingredients:
        st.warning("Enter at least one ingredient.")
    else:
        try:
            with st.spinner("Creating your recipe..."):
                recipe = generate_recipe(ingredients, cuisine, diet, goal, weight)
            st.subheader("Your Recipe")
            st.write(recipe)
        except Exception as error:
            st.error(f"Could not generate the recipe: {error}")
