# TPC5: A cabine telefónica

Hoje em dia, as cabines telefónicas, popularizadas pela famosa cabine londrina vermelha, caíram em desuso e têm vindo gradualmente a desaparecer. No entanto, podem ainda ser encontradas num ou noutro local.

Neste problema, pretende-se que implemente uma máquina de estados que modele a interacção dum utilizador com um telefone numa cabine pública.

O telefone reage aos seguintes comandos:

  1. **LEVANTAR** - levantar o auscultador, marca o início duma interacção;
  2. **POUSAR** - pousar o auscultador, fim da interacção, deverá ser indicado o montante a ser devolvido;
  3. **MOEDA \<lista de valores>** - inserção de moedas (só deverá aceitar moedas válidas, para valores inválidos deverá ser gerada uma mensagem de erro): `lista de valores = num, num, ..., num`;
  4. **T=numero** - disca o número ( o número deve ter 9 dígitos excepto se for iniciado por "00"); as diferentes chamadas deverão ser tratadas da seguinte maneira:
    * para números iniciados por "601" ou "641" a chamada é "_bloqueada_";
    * para chamadas internacionais (iniciadas por "00") o utilizador tem que ter um saldo igual ou superior a 1,5 euros, caso contrário deverá ser avisado que o saldo é insuficiente e a máquina volta ao estado anterior; a chamada se for realizada tem um custo de 1,5 euros;
    * para chamadas nacionais (iniciadas por "2") o saldo mínimo e custo de chamada é de 25 cêntimos;
    * para chamadas verdes (iniciadas por "800") o custo é 0;
    * para chamadas azuis (iniciadas por "808") o custo é de 10 cêntimos.
  5. **ABORTAR** - interromper a interacção; a máquina devolve as moedas.

Como extra pode ainda detalhar como é que é devolvido o troco: quantas moedas e de que espécie compõem o troco.

A seguir apresenta-se uma possível interacção exemplo.

```
LEVANTAR
maq: "Introduza moedas."
MOEDA 10c, 30c, 50c, 2e.
maq: "30c - moeda inválida; saldo = 2e60c"
T=601181818
maq: "Esse número não é permitido neste telefone. Queira discar novo número!"
T=253604470
maq: "saldo = 2e35c"
POUSAR
maq: "troco=2e35c; Volte sempre!" ou maq: "troco= 1x2e, 1x20c, 1x10c, 1x5c; Volte sempre!"
```

Nota: as linhas iniciadas por "maq:" correspondem às respostas da máquina.