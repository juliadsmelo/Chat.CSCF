# Chat.CSCF
Este projeto consiste em implementar em comunicação TCP entre diferentes clientes. Como o chat é em "tempo real" foram utilizadas threads para cuidar do envio e do recebimento no servidor. Assim, as mensagem poderão ser vistas por todos os envolvidos no momento de envio/recebimento.

**Resumo do Fluxo**
1. O cliente se conecta ao servidor e envia o nome do usuário.
2. Um thread é iniciado para receber e exibir mensagens do servidor.
3. O loop principal permite que o usuário envie mensagens ou saia do chat digitando "sair".
4. A conexão é encerrada de forma segura em caso de saída ou erro.
