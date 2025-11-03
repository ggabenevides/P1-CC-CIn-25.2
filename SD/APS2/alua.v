`timescale 1ns/1ps

// MÓDULO PRINCIPAL - UNIDADE LÓGICA E ARITMÉTICA (ULA) DE 8 BITS
module alua (
    output wire [7:0] Result,   // resultado da operação
    output wire [3:0] NZVC,     // Flags: negative, zero, overflow, carry
    input wire [7:0]  A,        // entrada A
    input wire [7:0]  B,        // entrada B
    input wire [2:0]  ALU_Sel   // seletor de operação
);

    // Fios Internos

    // Fios das saídas da Unidade Lógica
    wire [7:0] fio_saida_E;
    wire [7:0] fio_saida_OU;
    wire [7:0] fio_saida_XOR;
    wire [7:0] fio_saida_NAO;

    // Fio com o resultado final da Unidade Lógica
    wire [7:0] fio_resultado_logico;

    // Fios da Unidade Aritmética
    wire [7:0] fio_B_invertido;         // Saída do inversor da Entrada B
    wire [7:0] fio_entrada_B_somador;   // Entrada B final para o somador (pode ser B, 0, ~B, ou -1)
    wire       fio_vem_um_somador;      // Carry de Entrada para o somador
    wire [7:0] fio_resultado_aritmetico; // Resultado da Unidade Aritmética
    wire       fio_vai_um_somador;      // Carry de Saída da Unidade Aritmética

    // Fios para as Flags
    wire fio_Flag_N, fio_Flag_Z, fio_Flag_V, fio_Flag_C;
    wire fio_verificacao_zero; // Fio auxiliar para a flag Zero (saída do redutor OR)

    // Implementação Estrutural

    // Unidade Lógica (ALU_Sel[2] == 1)
    
    // Instancia todas as portas lógicas de 8 bits 
    and8b inst_porta_E (
        .F(fio_saida_E), 
        .A(A), 
        .B(B)
    );
    or8b inst_porta_OU (
        .F(fio_saida_OU), 
        .A(A), 
        .B(B)
    );
    xor8b inst_porta_XOR (
        .F(fio_saida_XOR), 
        .A(A), 
        .B(B)
    );
    not8b inst_porta_NAO (
        .F(fio_saida_NAO), 
        .A(A)
    );

    // Mux 4:1 para selecionar o resultado da Unidade Lógica (usando o nome fornecido)
    // Sel[1:0] = 00 -> E   (Sel=4)
    // Sel[1:0] = 01 -> OU  (Sel=5)
    // Sel[1:0] = 10 -> XOR (Sel=6)
    // Sel[1:0] = 11 -> NAO (Sel=7)
    mux8_4to1 inst_mux_logico (
        .F(fio_resultado_logico),
        .A(fio_saida_E),
        .B(fio_saida_OU),
        .C(fio_saida_XOR),
        .D(fio_saida_NAO),
        .Sel(ALU_Sel[1:0])
    );

    // Unidade Aritmética (ALU_Sel[2] == 0)
    
    // Inversor para a Entrada B (usado na subtração)
    not8b inst_inversor_B (
        .F(fio_B_invertido), 
        .A(B)
    );

    // Mux 4:1 para selecionar a segunda entrada do somador
    // Sel[1:0] = 00 -> Add (usa B)
    // Sel[1:0] = 01 -> Inc (usa 0)
    // Sel[1:0] = 10 -> Sub (usa ~B)
    // Sel[1:0] = 11 -> Dec (usa -1 ou 8'hFF)
    mux8_4to1 inst_mux_entrada_B_somador (
        .F(fio_entrada_B_somador),
        .A(B),
        .B(8'h00),
        .C(fio_B_invertido),
        .D(8'hFF),
        .Sel(ALU_Sel[1:0])
    );

    // Lógica para gerar o Cin
    assign fio_vem_um_somador = ALU_Sel[0] ^ ALU_Sel[1];

    // Somador de 8 bits por propagação de carry (Ripple Carry Adder)
    adder8b inst_somador_principal (
        .Sum(fio_resultado_aritmetico),
        .Cout(fio_vai_um_somador),
        .A(A),
        .B(fio_entrada_B_somador),
        .Cin(fio_vem_um_somador)
    );

    // 3. Mux Final (Seleciona o Resultado)
    
    // Seleciona entre a saída aritmética e a lógica baseado em ALU_Sel[2]
    mux8_2to1 inst_mux_final (
        .F(Result),
        .A(fio_resultado_aritmetico),
        .B(fio_resultado_logico),
        .Sel(ALU_Sel[2])
    );

    // Lógica das Flags (NZVC)
    
    // N (Negativo): Bit mais significativo (MSB) do resultado
    assign fio_Flag_N = Result[7];

    // Z (Zero): 1 se Result == 0.
    or8b_bw inst_verificador_zero (
        .F(fio_verificacao_zero), 
        .A(Result)
    );
    assign fio_Flag_Z = ~fio_verificacao_zero; // Z é o NOT da saída do redutor OR

    // V (Overflow) e C (Carry):
    
    // Lógica do Carry (C):
    assign fio_Flag_C = (ALU_Sel[2] == 1'b0) ? fio_vai_um_somador : 1'b0;

    // Lógica do Overflow (V):
    wire fio_overflow_aritmetico = (A[7] == fio_entrada_B_somador[7]) && (A[7] != fio_resultado_aritmetico[7]);
    assign fio_Flag_V = (ALU_Sel[2] == 1'b0) ? fio_overflow_aritmetico : 1'b0;
    
    // Atribuição final das flags
    assign NZVC = {fio_Flag_N, fio_Flag_Z, fio_Flag_V, fio_Flag_C};

endmodule

