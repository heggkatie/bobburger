from data.episodes import bob_s_burgers_episodes
import random

def get_all_episodes() -> list[dict]:
    return bob_s_burgers_episodes

def find_episodes_by_theme(theme_query: str) -> list[dict]:
    theme_query_lower = theme_query.lower()
    matching_episodes = [
        episode for episode in bob_s_burgers_episodes
        if any(theme_query_lower in theme.lower() fot theme in episode.get("Main Themes", []))
    ]
    return matching_episodes

def find_episodes_by_character(character_query: str) -> list[dict]:
    character_name_lower = character_name.lower()
    matching_episodes = [
        episode for episode in bob_s_burgers_episodes
        if any(character_name_lower in char.lower() for char in episode.get("Characters", []))
    ]
    return matching_episodes

def get_random_episode(episode_list: list[dict] = None) -> dict:
    if episode_list is None:
        episode_list = bob_burgers_episodes

    if not episode_list:
        return None

    return random.choice(episode_list)