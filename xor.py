#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])

# Kalbert(developer - Fija) ^ KCarlos (adm de sistemas, cambia por entorno) = Kprod (Key Manager) 
# Kprod = 6 = 5 (developer) ^ 3 (Carlos)

#Metodo A
#m = bytes.fromhex("AE12FF2235BC015F")
#k = bytes.fromhex("1E12BC2135BD016D")

m = bytes.fromhex("AFAA1232BCEF")
k = bytes.fromhex("AFAA1232BDFF")
print(xor_data(m,k).hex())

#Metodo B

#Tanto el metodo A como metodo b son validos. 
#num1=0xAE12FF2235BC015F
#num2=0x1E12BC2135BD016D

num1=0xB1EF2ACFE2BAEEFF
num2=0xB98A15BA31AEBB3F
num3=(hex(num1^num2))
print(num3[2:])
print(num3)

