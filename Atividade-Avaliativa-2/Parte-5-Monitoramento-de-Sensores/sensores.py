# PARTE 5 - HANDS ON 2: MATRIZ APLICADA - MONITORAMENTO DE SENSORES

sensores = []

# Receber as Temperaturas dos Sensores
for sensor in range(5):

    temperaturas_sensor = []

    for horario in range(24):

        temperatura = float(
            input(f"Digite a temperatura do Sensor {sensor} " f"no horário {horario}: ")
        )

        temperaturas_sensor.append(temperatura)

    sensores.append(temperaturas_sensor)


# Solicitar Limite de Temperatura
limite = float(input("\nDigite o limite de temperatura: "))


# Analisar Sensores
def analisar_sensores(sensores, limite):

    medias_sensores = []

    maior_temperatura = sensores[0][0]

    sensor_maior_temperatura = 0

    horario_maior_temperatura = 0

    soma_geral = 0

    contador_acima_limite = 0

    # Percorrer os Sensores
    for sensor in range(len(sensores)):

        soma_sensor = 0

        # Percorrer os Horarios
        for horario in range(len(sensores[sensor])):

            # Temperatura Atual
            temperatura_atual = sensores[sensor][horario]

            # Somar Temperatura do Sensor
            soma_sensor += temperatura_atual

            # Somar Temperatura Geral
            soma_geral += temperatura_atual

            # Verificar a Maior Temperatura
            if temperatura_atual > maior_temperatura:

                maior_temperatura = temperatura_atual

                sensor_maior_temperatura = sensor

                horario_maior_temperatura = horario

            # Verificar Temperaturas Acima do Limite
            if temperatura_atual > limite:

                contador_acima_limite += 1

        # Calcular Media do Sensor
        media_sensor = soma_sensor / len(sensores[sensor])

        # Guardar Media do Sensor
        medias_sensores.append(media_sensor)

    # Calcular Quantidade Total de Medicoes
    quantidade_medicoes = 0

    for sensor in range(len(sensores)):

        quantidade_medicoes += len(sensores[sensor])

    # Calcular Media Geral
    media_geral = soma_geral / quantidade_medicoes

    # Retornar Resultados
    return (
        medias_sensores,
        maior_temperatura,
        sensor_maior_temperatura,
        horario_maior_temperatura,
        media_geral,
        contador_acima_limite,
    )


# Fazer Analise dos Sensores
(
    medias_sensores,
    maior_temperatura,
    sensor_maior_temperatura,
    horario_maior_temperatura,
    media_geral,
    contador_acima_limite,
) = analisar_sensores(sensores, limite)


# Mostrar Todas as Medicoes
print("\nMEDICOES DOS SENSORES")

print("-" * 50)


for sensor in range(len(sensores)):

    print(f"\nSensor {sensor}")

    for horario in range(len(sensores[sensor])):

        print(f"Horario {horario}: " f"{sensores[sensor][horario]}°C")


# Mostrar Medias dos Sensores
print("\n" + "-" * 50)

print("MEDIAS DOS SENSORES")

print("-" * 50)


for sensor in range(len(medias_sensores)):

    print(f"Media do Sensor {sensor}: " f"{medias_sensores[sensor]:.2f}°C")


# Mostrar Maior Temperatura
print("\n" + "-" * 50)

print("MAIOR TEMPERATURA REGISTRADA")

print("-" * 50)

print("Maior Temperatura:", maior_temperatura, "°C")

print("Sensor Responsavel:", sensor_maior_temperatura)

print("Horario da Ocorrencia:", horario_maior_temperatura)


# Mostrar Media Geral
print("\n" + "-" * 50)

print("MEDIA GERAL")

print("-" * 50)

print(f"Media Geral: {media_geral:.2f}°C")


# Mostrar Leituras Acima do Limite
print("\n" + "-" * 50)

print("LEITURAS ACIMA DO LIMITE")

print("-" * 50)

print("Limite Informado:", limite, "°C")

print("Quantidade de Leituras Acima do Limite:", contador_acima_limite)

