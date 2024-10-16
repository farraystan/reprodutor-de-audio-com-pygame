import pygame

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega o arquivo de áudio
audio_file = "We'll Be Right Back - Sound Effect (HD).wav"  # Substitua pelo caminho do seu arquivo de áudio
pygame.mixer.music.load(audio_file)

# Inicia a reprodução do áudio
pygame.mixer.music.play()

# Mantém o script em execução enquanto o áudio está tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
