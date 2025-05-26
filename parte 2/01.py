arquivo = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade da internet (Mbps): '))
tempo = (arquivo * 8) / velocidade / 60
print('Tempo aproximado de download:', tempo, 'minutos')