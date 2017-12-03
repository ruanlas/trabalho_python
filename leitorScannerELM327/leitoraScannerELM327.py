import obd
import time

def conectar():
    return obd.OBD(); #retorna uma conexão obd automática

def conectarAsync():
    return obd.Async() #retorna uma conexão obd automática assíncrona

def obterLeituraAsync(conexao, comando):
    conexao.watch(comando) #acompanha o rpm
    conexao.start() #inicia o loop de atualização assíncrono
    return conexao.query(comando)

def obterLeitura(conexao, comando):
    return conexao.query(comando) #obtem uma leitura do veículo

def exibeLeitura(medicao):
    print(medicao.value)

def obterLeituraAsync2(conexao, comando):
    conexao.watch(comando, callback=exibeLeitura) #acompanha o rpm
    conexao.start() #inicia o loop de atualização assíncrono
    time.sleep(60)
    conexao.stop()

def main():
    conexaoElm = conectar()
    comandoMedicao = obd.commands.RPM
    print(obterLeitura(conexaoElm, comandoMedicao))


if __name__ == '__main__':
    main()