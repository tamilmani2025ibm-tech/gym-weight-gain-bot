def get_advice(message: str) -> str:
    msg = message.lower()

    if "weight" in msg and "gain" in msg:
        return "To gain healthy weight: eat calorie-dense foods like nuts, oats, eggs, and exercise with progressive overload 💪"
    elif "diet" in msg:
        return "A good muscle gain diet includes 40% carbs, 30% protein, 30% fats. Try 5 small meals daily 🍽️"
    elif "workout" in msg:
        return "Focus on compound lifts — squats, deadlifts, bench press. Train 4-5 days per week 🏋️"
    elif "hi" in msg or "hello" in msg:
        return "Hey there! I'm your Gym Coach Bot 💥. Ask me about workouts or diets!"
    else:
        return "I didn’t quite get that. Try asking about 'diet', 'workout', or 'weight gain'."
