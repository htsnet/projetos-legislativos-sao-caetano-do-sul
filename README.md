# projetos-legislativos-sao-caetano-do-sul
Busca do histórico de projetos legislativos da Câmara Municipal de São Caetano do Sul


A Câmara Municipal de São Caetano do Sul disponibiliza um site (https://mlegislativo.mirasoft.com.br/PortalMunicipe/Processos) com todos os projetos legislativos propostos pelos vereadores do município (a partir de 1985). São 10 projetos por página, sendo que, em 08/08/2020, são 7.295 páginas com 10 projetos em cada uma delas. 

O formato é bom para uma consulta isolada, mas ruim para a obtenção de todos os projetos para uma análise dos dados.

Diante desta situação, foi criado um programa em Python, usando as bibliotecas Pandas, Selenium e BeautifulSoup para acessar cada página e buscar os blocos de informações de cada projeto. Ao final, as informações são gravadas em um arquivo CSV para qualquer avaliação posterior.

O processamento completo demorou mais de 6 horas!
