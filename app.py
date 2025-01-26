# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-simulation', methods=['POST'])
def run_simulation():
    try:
        main.main()
        return "Simulation terminée avec succès !"
    except Exception as e:
        return "Erreur lors de la simulation : {}".format(str(e))

if __name__ == '__main__':
    app.run(debug=True)
