from pygame import mixer
mixer.init() #Inicializa o mixer
mixer.music.load('ex021.mp3') #Chama o arquivo de reprodução
mixer.music.set_volume(0.05) #Volume do som
mixer.music.play() #Inicia a reprodução
input('Digite algo para parar: ')
