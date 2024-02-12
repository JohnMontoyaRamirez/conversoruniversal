# conversor.py

import streamlit as st

def convertir_temperatura(valor, de, a):
    if de == "Celsius" and a == "Fahrenheit":
        return (valor * 9/5) + 32
    elif de == "Fahrenheit" and a == "Celsius":
        return (valor - 32) * 5/9
    elif de == "Celsius" and a == "Kelvin":
        return valor + 273.15
    elif de == "Kelvin" and a == "Celsius":
        return valor - 273.15
    else:
        return valor  # Si las unidades son las mismas, no hay conversión

def convertir_longitud(valor, de, a):
    if de == "Pies" and a == "Metros":
        return valor * 0.3048
    elif de == "Metros" and a == "Pies":
        return valor / 0.3048
    elif de == "Pulgadas" and a == "Centímetros":
        return valor * 2.54
    elif de == "Centímetros" and a == "Pulgadas":
        return valor / 2.54
    else:
        return valor

def convertir_peso(valor, de, a):
    if de == "Libras" and a == "Kilogramos":
        return valor * 0.453592
    elif de == "Kilogramos" and a == "Libras":
        return valor / 0.453592
    elif de == "Onzas" and a == "Gramos":
        return valor * 28.3495
    elif de == "Gramos" and a == "Onzas":
        return valor / 28.3495
    else:
        return valor

def convertir_volumen(valor, de, a):
    if de == "Galones" and a == "Litros":
        return valor * 3.78541
    elif de == "Litros" and a == "Galones":
        return valor / 3.78541
    elif de == "Pulgadas cúbicas" and a == "Centímetros cúbicos":
        return valor * 16.3871
    elif de == "Centímetros cúbicos" and a == "Pulgadas cúbicas":
        return valor / 16.3871
    else:
        return valor

def convertir_tiempo(valor, de, a):
    if de == "Horas" and a == "Minutos":
        return valor * 60
    elif de == "Minutos" and a == "Segundos":
        return valor * 60
    elif de == "Días" and a == "Horas":
        return valor * 24
    elif de == "Semanas" and a == "Días":
        return valor * 7
    else:
        return valor

def convertir_velocidad(valor, de, a):
    if de == "Millas por hora" and a == "Kilómetros por hora":
        return valor * 1.60934
    elif de == "Kilómetros por hora" and a == "Metros por segundo":
        return valor / 3.6
    elif de == "Nudos" and a == "Millas por hora":
        return valor * 1.15078
    elif de == "Metros por segundo" and a == "Pies por segundo":
        return valor * 3.28084
    else:
        return valor

def convertir_area(valor, de, a):
    if de == "Metros cuadrados" and a == "Pies cuadrados":
        return valor * 10.764
    elif de == "Pies cuadrados" and a == "Metros cuadrados":
        return valor / 10.764
    elif de == "Kilómetros cuadrados" and a == "Millas cuadradas":
        return valor * 0.386102
    elif de == "Millas cuadradas" and a == "Kilómetros cuadrados":
        return valor / 0.386102
    else:
        return valor

def convertir_energia(valor, de, a):
    if de == "Julios" and a == "Calorías":
        return valor * 0.239006
    elif de == "Calorías" and a == "Kilojulios":
        return valor * 0.004184
    elif de == "Kilovatios-hora" and a == "Megajulios":
        return valor * 3.6
    elif de == "Megajulios" and a == "Kilovatios-hora":
        return valor / 3.6
    else:
        return valor

def convertir_presion(valor, de, a):
    if de == "Pascales" and a == "Atmósferas":
        return valor * 9.86923e-6
    elif de == "Atmósferas" and a == "Pascales":
        return valor / 9.86923e-6
    elif de == "Barras" and a == "Libras por pulgada cuadrada":
        return valor * 14.5038
    elif de == "Libras por pulgada cuadrada" and a == "Barras":
        return valor / 14.5038
    else:
        return valor

def convertir_tamano_datos(valor, de, a):
    if de == "Megabytes" and a == "Gigabytes":
        return valor / 1024
    elif de == "Gigabytes" and a == "Terabytes":
        return valor / 1024
    elif de == "Kilobytes" and a == "Megabytes":
        return valor / 1024
    elif de == "Terabytes" and a == "Petabytes":
        return valor / 1024
    else:
        return valor

def main():
    st.title("Bienvenido a mi conversor de unidades")

    categorias = [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de Datos"
    ]

    categoria_seleccionada = st.sidebar.selectbox("Selecciona una categoría", categorias)

    if categoria_seleccionada == "Temperatura":
        conversiones_temperatura()
    elif categoria_seleccionada == "Longitud":
        conversiones_longitud()
    elif categoria_seleccionada == "Peso/Masa":
        conversiones_peso()
    elif categoria_seleccionada == "Volumen":
        conversiones_volumen()
    elif categoria_seleccionada == "Tiempo":
        conversiones_tiempo()
    elif categoria_seleccionada == "Velocidad":
        conversiones_velocidad()
    elif categoria_seleccionada == "Área":
        conversiones_area()
    elif categoria_seleccionada == "Energía":
        conversiones_energia()
    elif categoria_seleccionada == "Presión":
        conversiones_presion()
    elif categoria_seleccionada == "Tamaño de Datos":
        conversiones_tamano_datos()

def conversiones_temperatura():
    tipos_temperatura = [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_temperatura)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Celsius a Fahrenheit" in conversion_seleccionada:
            resultado = convertir_temperatura(valor, "Celsius", "Fahrenheit")
        elif "Fahrenheit a Celsius" in conversion_seleccionada:
            resultado = convertir_temperatura(valor, "Fahrenheit", "Celsius")
        elif "Celsius a Kelvin" in conversion_seleccionada:
            resultado = convertir_temperatura(valor, "Celsius", "Kelvin")
        elif "Kelvin a Celsius" in conversion_seleccionada:
            resultado = convertir_temperatura(valor, "Kelvin", "Celsius")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_longitud():
    tipos_longitud = [
        "Pies a Metros",
        "Metros a Pies",
        "Pulgadas a Centímetros",
        "Centímetros a Pulgadas"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_longitud)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Pies a Metros" in conversion_seleccionada:
            resultado = convertir_longitud(valor, "Pies", "Metros")
        elif "Metros a Pies" in conversion_seleccionada:
            resultado = convertir_longitud(valor, "Metros", "Pies")
        elif "Pulgadas a Centímetros" in conversion_seleccionada:
            resultado = convertir_longitud(valor, "Pulgadas", "Centímetros")
        elif "Centímetros a Pulgadas" in conversion_seleccionada:
            resultado = convertir_longitud(valor, "Centímetros", "Pulgadas")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_peso():
    tipos_peso = [
        "Libras a Kilogramos",
        "Kilogramos a Libras",
        "Onzas a Gramos",
        "Gramos a Onzas"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_peso)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Libras a Kilogramos" in conversion_seleccionada:
            resultado = convertir_peso(valor, "Libras", "Kilogramos")
        elif "Kilogramos a Libras" in conversion_seleccionada:
            resultado = convertir_peso(valor, "Kilogramos", "Libras")
        elif "Onzas a Gramos" in conversion_seleccionada:
            resultado = convertir_peso(valor, "Onzas", "Gramos")
        elif "Gramos a Onzas" in conversion_seleccionada:
            resultado = convertir_peso(valor, "Gramos", "Onzas")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_volumen():
    tipos_volumen = [
        "Galones a Litros",
        "Litros a Galones",
        "Pulgadas cúbicas a Centímetros cúbicos",
        "Centímetros cúbicos a Pulgadas cúbicas"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_volumen)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Galones a Litros" in conversion_seleccionada:
            resultado = convertir_volumen(valor, "Galones", "Litros")
        elif "Litros a Galones" in conversion_seleccionada:
            resultado = convertir_volumen(valor, "Litros", "Galones")
        elif "Pulgadas cúbicas a Centímetros cúbicos" in conversion_seleccionada:
            resultado = convertir_volumen(valor, "Pulgadas cúbicas", "Centímetros cúbicos")
        elif "Centímetros cúbicos a Pulgadas cúbicas" in conversion_seleccionada:
            resultado = convertir_volumen(valor, "Centímetros cúbicos", "Pulgadas cúbicas")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_tiempo():
    tipos_tiempo = [
        "Horas a Minutos",
        "Minutos a Segundos",
        "Días a Horas",
        "Semanas a Días"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_tiempo)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Horas a Minutos" in conversion_seleccionada:
            resultado = convertir_tiempo(valor, "Horas", "Minutos")
        elif "Minutos a Segundos" in conversion_seleccionada:
            resultado = convertir_tiempo(valor, "Minutos", "Segundos")
        elif "Días a Horas" in conversion_seleccionada:
            resultado = convertir_tiempo(valor, "Días", "Horas")
        elif "Semanas a Días" in conversion_seleccionada:
            resultado = convertir_tiempo(valor, "Semanas", "Días")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_velocidad():
    tipos_velocidad = [
        "Millas por hora a Kilómetros por hora",
        "Kilómetros por hora a Metros por segundo",
        "Nudos a Millas por hora",
        "Metros por segundo a Pies por segundo"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_velocidad)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Millas por hora a Kilómetros por hora" in conversion_seleccionada:
            resultado = convertir_velocidad(valor, "Millas por hora", "Kilómetros por hora")
        elif "Kilómetros por hora a Metros por segundo" in conversion_seleccionada:
            resultado = convertir_velocidad(valor, "Kilómetros por hora", "Metros por segundo")
        elif "Nudos a Millas por hora" in conversion_seleccionada:
            resultado = convertir_velocidad(valor, "Nudos", "Millas por hora")
        elif "Metros por segundo a Pies por segundo" in conversion_seleccionada:
            resultado = convertir_velocidad(valor, "Metros por segundo", "Pies por segundo")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_area():
    tipos_area = [
        "Metros cuadrados a Pies cuadrados",
        "Pies cuadrados a Metros cuadrados",
        "Kilómetros cuadrados a Millas cuadradas",
        "Millas cuadradas a Kilómetros cuadrados"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_area)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Metros cuadrados a Pies cuadrados" in conversion_seleccionada:
            resultado = convertir_area(valor, "Metros cuadrados", "Pies cuadrados")
        elif "Pies cuadrados a Metros cuadrados" in conversion_seleccionada:
            resultado = convertir_area(valor, "Pies cuadrados", "Metros cuadrados")
        elif "Kilómetros cuadrados a Millas cuadradas" in conversion_seleccionada:
            resultado = convertir_area(valor, "Kilómetros cuadrados", "Millas cuadradas")
        elif "Millas cuadradas a Kilómetros cuadrados" in conversion_seleccionada:
            resultado = convertir_area(valor, "Millas cuadradas", "Kilómetros cuadrados")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_energia():
    tipos_energia = [
        "Julios a Calorías",
        "Calorías a Kilojulios",
        "Kilovatios-hora a Megajulios",
        "Megajulios a Kilovatios-hora"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_energia)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Julios a Calorías" in conversion_seleccionada:
            resultado = convertir_energia(valor, "Julios", "Calorías")
        elif "Calorías a Kilojulios" in conversion_seleccionada:
            resultado = convertir_energia(valor, "Calorías", "Kilojulios")
        elif "Kilovatios-hora a Megajulios" in conversion_seleccionada:
            resultado = convertir_energia(valor, "Kilovatios-hora", "Megajulios")
        elif "Megajulios a Kilovatios-hora" in conversion_seleccionada:
            resultado = convertir_energia(valor, "Megajulios", "Kilovatios-hora")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_presion():
    tipos_presion = [
        "Pascales a Atmósferas",
        "Atmósferas a Pascales",
        "Barras a Libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a Barras"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_presion)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Pascales a Atmósferas" in conversion_seleccionada:
            resultado = convertir_presion(valor, "Pascales", "Atmósferas")
        elif "Atmósferas a Pascales" in conversion_seleccionada:
            resultado = convertir_presion(valor, "Atmósferas", "Pascales")
        elif "Barras a Libras por pulgada cuadrada" in conversion_seleccionada:
            resultado = convertir_presion(valor, "Barras", "Libras por pulgada cuadrada")
        elif "Libras por pulgada cuadrada a Barras" in conversion_seleccionada:
            resultado = convertir_presion(valor, "Libras por pulgada cuadrada", "Barras")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

def conversiones_tamano_datos():
    tipos_tamano_datos = [
        "Megabytes a Gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a Megabytes",
        "Terabytes a Petabytes"
    ]
    conversion_seleccionada = st.sidebar.selectbox("Selecciona un tipo de conversión", tipos_tamano_datos)

    valor = st.number_input("Ingresa el valor a convertir:")
    boton_convertir = st.button("Convertir")

    resultado = None

    if boton_convertir:
        if "Megabytes a Gigabytes" in conversion_seleccionada:
            resultado = convertir_tamano_datos(valor, "Megabytes", "Gigabytes")
        elif "Gigabytes a Terabytes" in conversion_seleccionada:
            resultado = convertir_tamano_datos(valor, "Gigabytes", "Terabytes")
        elif "Kilobytes a Megabytes" in conversion_seleccionada:
            resultado = convertir_tamano_datos(valor, "Kilobytes", "Megabytes")
        elif "Terabytes a Petabytes" in conversion_seleccionada:
            resultado = convertir_tamano_datos(valor, "Terabytes", "Petabytes")

    if resultado is not None:
        st.success(f"{valor} {conversion_seleccionada.split(' a ')[0]} son {resultado:.2f} {conversion_seleccionada.split(' a ')[1]}")

if __name__ == "__main__":
    main()
