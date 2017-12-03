import json, requests

def getBytesWebService():
    response = requests.get("http://18.231.62.135:5000/collection")
    if (response.status_code != 200):
        return False
    return response.content

def getListMedicoes():
    stringDados = getBytesWebService().decode('utf8')
    return json.loads(stringDados)

def getMedicoesPorModelo(modelo):
    # lista = []
    tamanho = len(getListMedicoes())
    for i in range(tamanho):
        if getListMedicoes()[i]['modelo'] == modelo:
            print(getListMedicoes()[i])
    #         lista.append(getListMedicoes()[i])
    # return lista



def main():
    # print(getMedicoesPorModelo("celta"))
    getMedicoesPorModelo("celta")


if __name__ == '__main__':
    main()