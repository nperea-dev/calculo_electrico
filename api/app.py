from flask import Flask, render_template, request

app = Flask(__name__)

app.template_folder = '../api'


def calcular_torque(V_L, I_L, cos_phi, f):
    denominador = 3.6276 * f
    torque = (V_L * I_L * cos_phi) / denominador
    return torque

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tension_linea = float(request.form['tension_linea'])
        corriente_linea = float(request.form['corriente_linea'])
        factor_potencia = float(request.form['factor_potencia'])
        frecuencia = float(request.form['frecuencia'])
        
        torque_resultante = calcular_torque(tension_linea, corriente_linea, factor_potencia, frecuencia)
        return render_template('index.html', resultado=torque_resultante, tension_linea=tension_linea, corriente_linea=corriente_linea, factor_potencia=factor_potencia, frecuencia=frecuencia)

    return render_template('index.html', resultado=None, tension_linea=None, corriente_linea=None, factor_potencia=None, frecuencia=None)

if __name__ == '__main__':
    app.run(debug=True)
