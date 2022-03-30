from influxdb import InfluxDBClient
import datetime 

client = InfluxDBClient(host="localhost",port="8086")
print(client.get_list_database())

#CRIANDO BANCO DE DADOS
basededados = client.create_database('bancodedados1')
client.get_list_database()
client.switch_database('bancodedados1')

json_body = [
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f",
            "cidade": "Caieiras"
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "duration": 127
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-29T8:04:00Z",
        "fields": {
            "duration": 132
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-30T8:02:00Z",
        "fields": {
            "duration": 129
        }
    }
]


client.write_points(json_body,database='bancodedados1')

results = client.query('SELECT * FROM "brushEvents"')


#MOSTRANDO O NOME DAS TABELAS
print(client.get_list_measurements())
#MOSTRANDO OS RESULTADOS
print(results)

#APLICANDO FILTRO DE DURAÇÃO
#duracao = client.query('SELECT "duration" FROM "bancodedados1"."autogen"."brushEvents" WHERE time > now() - 4d GROUP BY "user"')
#print(duracao)
