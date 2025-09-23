n1 = 54
n2 = 3
resultado = 13 + n1 / n2;

print("El resultado de la operacion es: ", resultado)

print (3 * "s" + 4 * "h")
print (float("3") + int(4.3))


def velocidad(distancia, tiempo):
  resultado = ""
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable resultado
  # recuerda que los datos están en las variables distancia y tiempo
  velocidad_km = (distancia / 1000) / (tiempo / 3600)
  velocidad_ms = (distancia*1000)/tiempo
  resultado = f"La velocidad es {velocidad_km} km/h o {velocidad_ms} m/s"
  return resultado
print(velocidad (1, 4))