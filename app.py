from flask import Flask
from flask_restful import Resource, Api
import os

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
api = Api(app)


class CalculeTemps(Resource):
    def get(self, autonomie, temps_recharge, distance_parcours, vitesse_moyenne):
        temps_parcours = distance_parcours // vitesse_moyenne * 60
        nb_recharge = 0
        if distance_parcours % autonomie != 0:
            nb_recharge += 1
        nb_recharge += distance_parcours // autonomie
        temps_parcours += nb_recharge * temps_recharge
        return {"temps_total": temps_parcours}


class CalculeTempsMaps(Resource):
    def get(self, autonomie, temps_recharge, distance_parcours, temps_total):
        temps_parcours = temps_total
        nb_recharge = 0;
        if distance_parcours % autonomie != 0:
            nb_recharge += 1
        nb_recharge += distance_parcours // autonomie
        temps_parcours += nb_recharge * temps_recharge
        return {"temps_total" : temps_parcours, "nb_recharge": nb_recharge}


api.add_resource(CalculeTemps, '/temps/<int:autonomie>/<int:temps_recharge>/<int:distance_parcours>/<int:vitesse_moyenne>')
api.add_resource(CalculeTempsMaps, '/tempsMaps/<int:autonomie>/<int:temps_recharge>/<int:distance_parcours>/<int:temps_total>')

if __name__ == '__main__':
    # app.run(host="localhost", port=port)
    app.run(host='0.0.0.0', port=port)
