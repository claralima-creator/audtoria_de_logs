print(f'[{"AUDITORIA DE EVENTOS":=^40}]')

eventos_brutos = [
    ("10:30:02", "user_17", 200),
    ("10:31:15", "user_42", 404),
    ("10:32:05", "user_42", 500),
    ("10:32:40", "", 200),
    ("10:33:10", "user_08", 999),
    ("10:34:02", "user_42", 500),
    ("10:35:20", "user_17", 200),
    ("10:36:45", "user_55", 500),
    ("10:37:01", "user_08", 201),
    ("10:38:12", "user_42", 400),
    ("10:39:30", "user_17", 500),
    ("10:40:05", "user_55", 200)
]

status_validos = (200, 201, 400, 404, 500)

print(f'Total de eventos brutos:{len(eventos_brutos)}')

janela_suspeita = eventos_brutos[2:8]

print(f'Janela suspeita: {len(janela_suspeita)}')

eventos_validos = []

for evento in eventos_brutos:
    print(evento)

for horario, usuario, status in eventos_brutos:
    if status in status_validos and usuario != "":
        eventos_validos.append((horario, usuario, status))
        print('Válido!')
    else:
        print('Inválido!')
print(f'Eventos válidos: {len(eventos_validos)} de {len(eventos_brutos)}')

total_500 = 0

for horario, usuario, status in eventos_validos:
    if status == 500:
        total_500 = total_500 + 1
print(f'Total de erros 500: {total_500}')

for indice, (horario, usuario, status) in enumerate(eventos_validos):
    if status == 500:
        print(indice)

criticos = []

for horario, usuario, status in eventos_validos:
    if status == 400:
        criticos.append((horario, usuario, status))

criticos_invertidos = criticos[::-1]

print('::- Transações mais críticas (Mais recente primeiro)::-')

for horario, usuario, status in criticos_invertidos:
    print(f'[{horario}] {usuario} :> status {status}')