from flask import Flask, jsonify

app = Flask(__name__)

pet1={"pet":"Melody","raca":"lhasa apso", "idade":12, "distancia":30}
pet2={"pet":"Fufy","raca":"Dalmata","idade":8, "distancia":15}
pet3={"pet":"Luke","raca":"Labrador","idade":6, "distancia":45}
pet4={"pet":"Retina","raca":"beagle","idade":10, "distancia":22}
pet5={"pet":"Cristalina","raca":"Pinscher","idade":4, "distancia":17}
pet6={"pet":"Sofia","raca":"labrador","idade":12, "distancia":20}
pet7={"pet":"Safira","raca":"bulldog","idade":1, "distancia":32}
pet8={"pet":"Bingo","raca":"doberman","idade":3, "distancia":40}
pet9={"pet":"Drogon","raca":"dalmata","idade":4, "distancia":20}
pet10={"pet":"Blue","raca":"bullterier","idade":8, "distancia"30}

@app.route("/pets")
def pets_routes():
	return jsonify([pet1,pet2,pet3,pet4, pet5, pet6, pet7, pet8, pet9, pet10])

@app.route("/pets/<distancia_moto>")
def pets_routes_with_distance(distancia_moto):
	pets_no_raio = []
	for pet in [pet1,pet2,pet3,pet4, pet5, pet6, pet7, pet8, pet9, pet10]:
		if pet["distancia"]<=int(distancia_moto):
			pets_no_raio.append(pet)
	return jsonify(pets_no_raio)

app.run(host="192.168.0.104", port=5000)
