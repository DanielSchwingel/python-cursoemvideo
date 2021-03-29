#Pintando a parede
largura = float(input('Informe a largura da sua parede (mt):'))
altura = float(input('Informe a altura da sua parede (mt):'))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para você pintar essa parede você precisará de {}l de tinta'.format(tinta))
