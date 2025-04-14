import requests

def consultar_api_externa(nome: str):
    url = f"https://economia.awesomeapi.com.br/json/last/{nome}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta foi bem-sucedida (status 200)
        data = response.json()

        # Verifica se a chave para a moeda existe na resposta
        moeda_data = data.get(f"{nome}BRL")  # Por exemplo, "EURBRL" para EUR
        if moeda_data:
            # Retorna o valor do campo 'bid', que é o valor da moeda
            return float(moeda_data['bid'])
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição para a API externa: {e}")
        return None
