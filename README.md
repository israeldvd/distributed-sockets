# Sistemas Distribuídos: observações sobre a implementação de sockets na plataforma Linux com as ferramentas do Python

<!-- Python + UDP + Linux -->

## Sumário

- [Sistemas Distribuídos: observações sobre a implementação de sockets na plataforma Linux com as ferramentas do Python](#sistemas-distribuídos-observações-sobre-a-implementação-de-sockets-na-plataforma-linux-com-as-ferramentas-do-python)
  - [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Código](#código)
  - [Referências](#referências)

## Introdução

Sockets (tomadas, em tradução livre) são canais de baixo nível utilizados na comunicação de redes, cuja origem está associada ao sistema Unix Berkeley (BSD), que desenvolveu este “mecanismo para comunicação virtual entre processos” (SOCKET, 2003). É portanto um dos meios para que haja uma troca de serviços, ações e documentos entre processos; por exemplo, documentos hipertexto podem ser obtidos por requisições da pilha TCP/IP.

Constituem uma importante ferramenta para o entendimento das comunicações entre processos. Nesse sentido, foi proposto em aula o desenvolvimento de um sistema de comunicação cliente-servidor entre dois computadores (ou processos numa mesma máquina).

## Código

A **principal biblioteca** em que se apoia este projeto, conforme apontado anteriormente, é a **socket**. Um de seus principais métodos, por sua vez, pode ser chamado mediante o método `socket.socket()`. A partir dele é criado um objeto que funciona como o canal para a comunicação. Este método recebe como segundo parâmetro – pulando o primeiro, mas ele não será ignorado – o tipo de socket, o qual usualmente é definido pela constante `socket.SOCK_STREAM`, que é acompanhada nativamente pelo protocolo TCP, arranjado diferente do proposto aqui.

Para o uso do **protocolo UDP**, será possível valer-se da constante `socket.SOCK_DGRAM` (JENNINGS, 2022). Antes do envio dos dados entre os mensageiros por intermédio do protocolo TCP, seria preciso estabelecer uma conexão entre as partes; mais uma vez, este não vem ao caso. Porém, aqui também há trocas constantes mediantes os métodos `.send()` and `.recv()` – já mencionados na especificação da seção anterior.

Primeiramente, ficaram estabelecidas o endereço **_host_** (IP) e o **endereço de porta** (_port number_) `127.0.0.1` e `1234`, respectivamente (ver código). O número de interface (ou porta) pode ser definido como maior que `1023` (valor limite para portas específicas); o valor dado foi tomado por conveniência. Com a declaração with é possível chamar o método `socket.socket()` sem a necessidade do método `socket.close()`, pois é executado implicitamente.

## Referências

CAMPBELL, A. T. Computer Networks: want to program the Internet? [S. l.]: Universidade de Dartmouth, [2013]. Acesso em: ago. 2022. Disponível em: https://www.cs.dartmouth.edu/~campbell/cs60/. (Computer Science 60).

ERIK. Beginner's Guide to Python. [S. l.]: Python, 2022. Acesso em: ago. 2022. Disponível em: http://foldoc.org/python. (Wiki BeginnersGuide)

PYTHON: In:The Free On-line Dictionary of Computing. [S. l.]: FOLDOC, 2013. Acesso em: ago. 2022. Disponível em: http://foldoc.org/python.

PYTHON.ORG. The Python Language Reference. [S. l.]: Python, 2022. Acesso em: ago. 2022. Disponível em: https://docs.python.org/3/reference/index.html.

JENNINGS, N. Socket Programming in Python (Guide). Acesso em: ago. 2022. Disponível em: https://realpython.com/python-sockets/.

ROCHA, M. A A. Comunicação entre processos (Slides). [S. l.]: IFF, 2022. (Computação para Engenharia II).

SALGADO, P. G.. Socket: Low-level networking interface. [S. l.]: Python, 2022. Acesso em: ago. 2022. Disponível em: https://docs.python.org/3/library/socket.html.

SOCKET. In: The Free On-line Dictionary of Computing. [S. l.]: FOLDOC, 2003. Acesso em: ago. 2022. Disponível em: https://encyclopedia2.thefreedictionary.com/socket.
