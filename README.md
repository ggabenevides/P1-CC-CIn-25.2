# CC 25.2 @ CIn-UFPE

Este repositório contém os exercícios e projetos desenvolvidos para as disciplinas do **primeiro período do curso de bacharelado em Ciência da Computação**: Introdução à Programação (IP), em Python, e Sistemas Digitais (SD), em Verilog.

## Sobre as disciplinas

- **IP (Introdução à Programação)**: exercícios de lógica de programação e fundamentos em Python — desde exercícios de fixação (loops, condicionais) até listas com problemas mais elaborados (ordenação, estruturas de dados básicas, manipulação de dados).
- **SD (Sistemas Digitais)**: implementação e simulação de circuitos digitais em Verilog, partindo de portas lógicas básicas até um datapath e unidade de controle completos, com testbenches para validação.

## Estrutura do Repositório

A organização segue uma lógica de pastas por disciplina e módulos para manter o ambiente limpo:

```text
.
├── IP/                          # Introdução à Programação (Python)
│   ├── exercicios_fixacao/      # Exercícios de fixação (fatorial, notas, plano cartesiano, etc.)
│   └── listas/                  # Listas de exercícios
│       └── lista1 a lista6/     # Uma pasta por lista, com um script .py por exercício
├── SD/                          # Sistemas Digitais (Verilog)
│   ├── APS1/                    # Portas lógicas básicas (and, or, xor, not, mux)
│   ├── APS2/                    # Somadores, multiplexadores/demultiplexadores e testbenches
│   ├── APS3/                    # Registradores, contadores e máquinas de estado (FSM)
│   └── APS4/                    # Datapath, unidade de controle e memória
├── .gitignore                   # Regras para manter o repo limpo
└── README.md                    # Este arquivo
```

## Instruções gerais

### Execução de códigos Python (IP)
```bash
python3 IP/listas/listaX/arquivo.py
```

### Simulação de códigos Verilog (SD)
Usando o Icarus Verilog (`iverilog`):
```bash
iverilog -o bin/arquivo.vvp SD/APSX/arquivo.v SD/APSX/arquivo_tb.v
vvp bin/arquivo.vvp
```

Para visualizar as formas de onda geradas (`.vcd`), use o GTKWave:
```bash
gtkwave arquivo.vcd
```
