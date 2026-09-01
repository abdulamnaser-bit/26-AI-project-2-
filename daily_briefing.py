from memory import recall
from achievement_memory import get_achievements
from goal_manager import get_goal

def get_daily_briefing():

    project = recall("current_project")
    bike = recall("favorite_bike")
    achievements = get_achievements()
    goal = get_goal()
    briefing = "Good morning, Boss.\n\n"

    if goal:

        briefing += (
            f"Current goal: {goal}\n"
        )

    if project:
        briefing += (
            f"Current project: {project}\n"
        )

    if achievements:

        briefing += (
            f"Recent achievement: "
            f"{achievements[-1]}\n"
        )

    if bike:

        briefing += (
            f"Favorite bike: {bike}\n"
        )

    briefing += (
        "\nReady to continue where we left off?"
    )

    return briefing