from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from Controller.battle_controller import battle_bp
from Controller.troop_controller import troop_bp

app = Flask(__name__)

# Configurações de MongoDB
app.config["MONGODB_SETTINGS"] = {
    'db': 'clash',
    'host': 'mongodb+srv://applicationuser:BHUnji@learnigmdb.chwf8.mongodb.net/?retryWrites=true&w=majority&appName=LearnigMDB'
}

db = MongoEngine()
db.init_app(app)

# Registra os blueprints
app.register_blueprint(battle_bp, url_prefix="/api/battles")
app.register_blueprint(troop_bp, url_prefix="/api/troops")

@app.route('/') 
def index():
     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
