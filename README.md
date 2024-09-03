
# Aplicativo Desktop PyQT5 para enviar email

Esse pequeno projeto é referente a uma interface gráfica bem simples, utilizando o PyQT5, para envio de email.



## Autores

- [Francisco Gomes](https://www.linkedin.com/in/fgsj-developer/)


## Referência

 - [Wiki Python](https://wiki.python.org/moin/PyQt#:~:text=PyQt%20is%20one%20of%20the%20most%20popular%20Python,provides%20bindings%20for%20Qt%204%20and%20Qt%205.)
 - [Real Python](https://realpython.com/python-pyqt-gui-calculator/)
 - [fman build system](https://build-system.fman.io/qt-designer-download)

Requisito e passo a passo do projeto

![image](https://github.com/user-attachments/assets/4770a5be-aa38-4e07-8dc3-d0aab1518559)
- Na imagem acima você irá precisar realizar o download do Qt Designer para a criação da(s) janela(s) de interface gráfica, Não se preocupe é muito de "Clica e arrasta" porém 
Se faz necessário realizar algumas configurações e entender um pouco sobre CSS mas é algo muito simples, a própria plataforma é intuitiva e ajuda nas customizações de telas.

![image](https://github.com/user-attachments/assets/e62c8c91-63e2-438a-83a2-22ec3029b9a2)
- Aqui está a tela do projeto, basicamente dois campos de textos, um para o destinatário e outro para o corpo do email
E um botão para realizar a ação de enviar o email, o qual será necessário clicar com botão direito e apenas para realizar a customização de tela.

![image](https://github.com/user-attachments/assets/a717c200-ac75-4a44-ac22-aa2d5f041881)
- Script de customização das cores da interface gráfica 

![image](https://github.com/user-attachments/assets/93668125-c31a-4912-b9fb-a5e6980ccfd3)
- Tela inicial do projeto

![image](https://github.com/user-attachments/assets/f959d267-4a02-4b5e-896c-250c99d1f332)
- Essa foi basicamente a organização dos arquivos do projeto, vale ressaltarr que o arquivo no formato ".UI" foi gerado a partir do Qt Designer

![image](https://github.com/user-attachments/assets/0ce5d2fc-2f6e-4c1f-9339-176000c6de4f)
- No meu exemplo, utilizando o GMAIL, procure na janela de "App passwords" 

![image](https://github.com/user-attachments/assets/421fad42-5ddb-43e4-98ca-c1c5425e6df5)
- Aqui você vai precisar criar um app, pra gerar uma senha aleatória que será utilizada no projeto para uma espécie de autenticação.

![image](https://github.com/user-attachments/assets/fc2a32e8-6867-476c-a46d-b17d89d7560c)
- Os valores das variáveis em questão, você deverá colocar o seu email e a senha que foi gerada ao criar o app lá no "App passwords" no Gmail
