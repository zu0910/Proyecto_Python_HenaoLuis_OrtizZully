import json 

with open("./Campusland.json", encoding="utf-8") as file:
    archivo=json.load(file)

user=input("Ingrese el usuario\n")
for i in range(len(archivo["Campers"])):
    if user in archivo["Campers"][i]["user"]["login"]:
        passwordCamper=input("Ingresa la contraseña\n")
        if passwordCamper==archivo["Campers"][i]["user"]["contraseña"]:
            print("Bienvenido",archivo["Campers"][i]["nombres"] )

for q in range(len(archivo["Trainers"])):
    if user in archivo["Campers"][i]["user"]["login"]:
        print(archivo["Trainers"][q]["nombres"])
        passwordTrainer=input("Ingresa la contraseña\n")

if user in archivo["Coordinador"]["user"]["login"]:
    print(archivo["Coordinador"]["nombres"])
    passwordCoordinador=input("Ingresa la contraseña\n")
else:
    print("usuario no encontrado")

json_archivo=json.dumps(archivo)
with open("./Campusland.json","w") as files:
    files.write(json_archivo)
#hola