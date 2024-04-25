# Princípios SOLID

Este repositório contém exemplos de código para ilustrar os princípios SOLID da programação orientada a objetos.

## O que são os Princípios SOLID?

Os Princípios SOLID são um conjunto de cinco princípios de design de software que visam criar sistemas mais compreensíveis, flexíveis e fáceis de manter. Esses princípios foram introduzidos por Robert C. Martin (também conhecido como Uncle Bob) e são amplamente adotados na indústria de desenvolvimento de software.

Os cinco princípios SOLID são:

1. **S - Princípio da Responsabilidade Única (Single Responsibility Principle - SRP):** Uma classe deve ter apenas um motivo para mudar. Isso significa que uma classe deve ter apenas uma responsabilidade ou tarefa e deve estar focada em realizá-la.

2. **O - Princípio do Aberto/Fechado (Open/Closed Principle - OCP):** Entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação. Isso significa que o comportamento de uma entidade deve poder ser estendido sem modificar seu código-fonte.

3. **L - Princípio da Substituição de Liskov (Liskov Substitution Principle - LSP):** Os objetos de uma classe derivada devem poder ser substituídos por objetos de sua classe base sem afetar a corretude do programa. Isso significa que uma classe derivada deve ser substituível por sua classe base sem que o programa produza resultados incorretos.

4. **I - Princípio da Segregação de Interfaces (Interface Segregation Principle - ISP):** Muitas interfaces específicas são melhores do que uma interface única. Isso significa que as interfaces devem ser coesas e não devem forçar as classes a implementar métodos que elas não usam.

5. **D - Princípio da Inversão de Dependência (Dependency Inversion Principle - DIP):** Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.

## Exemplos

Este repositório contém exemplos de código para ilustrar cada um dos princípios SOLID. Cada princípio é exemplificado com código em uma linguagem específica.

1. **SRP:**
   - Exemplo em [Python](/srp/python)
   - Exemplo em [Java](/srp/java)

2. **OCP:**
   - Exemplo em [Python](/ocp/python)
   - Exemplo em [Java](/ocp/java)

3. **LSP:**
   - Exemplo em [Python](/lsp/python)
   - Exemplo em [Java](/lsp/java)

4. **ISP:**
   - Exemplo em [Python](/isp/python)
   - Exemplo em [Java](/isp/java)

5. **DIP:**
   - Exemplo em [Python](/dip/python)
   - Exemplo em [Java](/dip/java)

Cada exemplo contém uma breve descrição do princípio, seguido por implementações de código que demonstram como aplicar o princípio em um cenário específico.

## Contribuições

Contribuições são bem-vindas! Se você tiver exemplos adicionais ou melhorias nos exemplos existentes, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
