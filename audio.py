import random
import pygame

discography = [
    "Cloud Country",
    "Distant Banjo",
    "Playful",
    "It's A Big World Outside",
    "The Valley Comes Alive",
    "Wild Horseradish Jam",
]

MUSIC_END = pygame.USEREVENT + 1


def play_music():
    """
    Shuffles the list representation (discography) of the some of the mp3s
    provided in Assets/music and plays a random track; prints the track name
    to the terminal and waits until the track completes to start another

    Returns:
        None
    Raises:
        pygame.error: safeguarding against WSL pygame errors
    """
    try:
        # randomize the song list
        random.shuffle(discography)
        # play the songs in the list one by one
        for song in discography:
            pygame.mixer.music.load(f"Assets/music/{song}.mp3")
        pygame.mixer.music.play()
        print(f"playing '{song}' ...")
        # wait until the song completes
        pygame.mixer.music.set_endevent(MUSIC_END)
    except pygame.error:
        pass


def play_sound(sound_name, num_vers=0):
    """
    Plays a sound from Assets/sound_bites based off of a provided sound name
    and number of versions

    Args:
        sound_name: a string representing the name of a sound in sound_bites
        without the ending index number
        num_vers: an int representing the largest index number of any file
        in sound_bites with sound_name (for example, harvest3.wav means
        num_vers should be 3)

    Returns:
        None
    Raises:
        pygame.error: WSL has issues supporting pygame audio and throws this
        error
    """
    try:
        pygame.mixer.Sound.play(
            pygame.mixer.Sound(
                f"Assets/sound_bites/{sound_name}{random.randint(0, num_vers)}.wav"
            )
        )
    except pygame.error:
        pass
