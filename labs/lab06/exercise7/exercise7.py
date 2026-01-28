def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):

    for songs in add_songs:
        current_playlist.add(songs)

    current_playlist.update(import_playlist)

    current_playlist.difference_update(banned_songs)

    while len(current_playlist) > 6:
        current_playlist.pop()

    return len(current_playlist) 

    """
    Manages a music playlist with adds, imports, and removals.
    
    Args:
        current_playlist: Set of currently in playlist
        add_songs: List of songs to add individually
        import_playlist: Set of songs to import from Spotify
        banned_songs: Set of songs to remove
    
    Returns:
        int: Count of final songs in playlist
    """
    pass
