from interpolate import interpolate
import numpy as np

def main():
    print("Métodos de Interpolación")
    print("1. Regresión Lineal")
    print("2. Regresión Exponencial")
    print("3. Regresión Cuadrática")
    print("4. Regresión Cúbica")
    print("5. Regresión de Potencia")
    print("6. Regresión Hiperbólica")
    print("7. Regresión Logarítmica")
    
    while True:
        choice = input("Seleccione un método (1-7): ")
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            break
        print("Opción inválida.")
    
    n = interpolate.orden()
    data = interpolate.data(n)
    x_data, y_data = data[0], data[1]
    
    models = {
        '1': interpolate.RLineal,
        '2': interpolate.RExponencial,
        '3': interpolate.RCuadratica,
        '4': interpolate.RCubica,
        '5': interpolate.RPotencia,
        '6': interpolate.RHiperbolica,
        '7': interpolate.RLogaritmica
    }
    
    try:
        model = models[choice](n, x_data, y_data)
        resultado = model.resultado()
        error = model.error_est_regre()
        print(f"Resultado: {resultado}")
        print(f"Error (MSE): {error}")
        plot = model.plot()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()