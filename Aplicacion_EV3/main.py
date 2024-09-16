from pickle import FALSE

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formularioNotas', methods=['GET', 'POST'])
def formularioNotas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asisten = float(request.form['asistencia'])
        EstaAprobado = 'REPROBADO'
        prom = float((nota1 + nota2 + nota3)/3)
        if(prom >= 40 and asisten >= 75):
            EstaAprobado = 'APROBADO'
            return render_template('formularioNotas.html', promedio = prom, aprobado = EstaAprobado)
        else:
            return render_template('formularioNotas.html', promedio = prom, aprobado = EstaAprobado)
    return render_template('formularioNotas.html')

@app.route('/nombresFormulario', methods=['GET', 'POST'])
def nombresFormulario():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        if(len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3)):
            tamanio = len(nombre1)
            return render_template('nombresFormulario.html', nombreLargo = nombre1, tamanoNombre = tamanio)
        elif (len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3)):
            tamanio = len(nombre2)
            return render_template('nombresFormulario.html', nombreLargo = nombre2, tamanoNombre = tamanio)
        else:
            tamanio = len(nombre3)
            return render_template('nombresFormulario.html', nombreLargo = nombre3, tamanoNombre = tamanio)
    return render_template('nombresFormulario.html')

if __name__ == '__main__':
    app.run(debug=True)