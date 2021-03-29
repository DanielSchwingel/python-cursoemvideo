#Conversor de medidas
medida = int(input('Digite a distância em metros(mt):'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('{}mt equivalem a {}km'.format(medida, km))
print('{}mt equivalem a {}hm'.format(medida, hm))
print('{}mt equivalem a {}dam'.format(medida, dam))
print('{}mt equivalem a {}dm'.format(medida, dm))
print('{}mt equivalem a {}cm'.format(medida, cm))
print('{}mt equivalem a {}mm'.format(medida, mm))
