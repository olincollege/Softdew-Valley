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
    # randomize the song list
    random.shuffle(discography)
    # play the songs in the list one by one
    for song in discography:
        pygame.mixer.music.load(f"Assets/music/{song}.mp3")
    pygame.mixer.music.play()
    print(f"playing '{song}' ...")
    # wait until the song completes
    pygame.mixer.music.set_endevent(MUSIC_END)


def play_sound(sound_name, num_versions=0):
    try:
        pygame.mixer.Sound.play(
            pygame.mixer.Sound(
                f"Assets/sound_bites/{sound_name}{random.randint(0, num_versions)}.wav"
            )
        )
    except pygame.error:
        pass
