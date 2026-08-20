def format_episode(episode: dict) -> str:
    if not episode:
        return "No episode found."

    name = episode.get("Name", "N/A")
    season = episode.get("Season", "N/A")
    ep_num = episode.get("Episode", "N/A")
    themes = ", ".join(episode.get("Main Themes", [])) if episode.get("Main Themes") else "None listed"
    characters = ", ".join(episode.get("Characters", [])) if episode.get("Characters") else "None listed"

    return (f" --- Episode Details ---\n"
            f"Name: {name}\n"
            f"Season: {season}, Episode: {ep_num}\n"
            f"Themes: {themes}\n"
            f"Characters: {characters}\n"
            f"                          ")

def display_episodes(episodes: list[dict], title: str = "Matching Episodes"):
    print(f"\n    {title}    ")
    if not episodes:
        print("No episodes to display.")
        return

    for i, episode in enumerate(episodes):
        print(f"\n{i+1}. {format_episode(episode)}")
    print(f"                               \nTotal found: {len(episodes)}")

def display_message(message: str):
    print(f"/n{message}\n")

def display_error(error_message: str):
    print(f"\nERROR: {error_message}\n")