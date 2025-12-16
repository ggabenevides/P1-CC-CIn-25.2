`timescale 1ns/1ps
`include "control_unit.v"

module control_unit_tb;

    // Sinais para a Unidade de Controle
    reg Clk = 1'b0;
    reg Reset = 1'b0;
    reg [7:0] IR_in = 8'h00; // Simula a saída do registrador IR (entrada para a UC)
    reg [3:0] CCR_Result_in = 4'b0000;

    // Saídas da Unidade de Controle
    wire IR_Load, MAR_Load, PC_Load, PC_Inc;
    wire A_Load, B_Load, CCR_Load;
    wire [2:0] ALU_Sel;
    wire [1:0] Bus1_Sel, Bus2_Sel;

    // Instanciação da Unidade de Controle
    control_unit dut (
        .IR_Load(IR_Load), 
        .MAR_Load(MAR_Load), 
        .PC_Load(PC_Load), 
        .PC_Inc(PC_Inc), 
        .A_Load(A_Load), 
        .B_Load(B_Load),
        .CCR_Load(CCR_Load),
        .ALU_Sel(ALU_Sel),
        .Bus1_Sel(Bus1_Sel), 
        .Bus2_Sel(Bus2_Sel),
        .write(write), 
        .IR(IR_in), 
        .CCR_Result(CCR_Result_in), 
        .Clk(Clk), 
        .Reset(Reset)
    );

    // Geração do Clock (50% duty cycle, 20ns period)
    always #10 Clk = ~Clk;

    // Main Test Sequence
    initial begin
        $dumpfile("control_unit_tb.vcd");
        $dumpvars(0, control_unit_tb);

        // 1. Reset
        Reset = 1'b0;
        #20 Reset = 1'b1; // Reset Assíncrono Ativo Baixo

        // 2. FETCH + LDA_IMM (Opcode 8'h01)
        
        // C1 (S0_FETCH): MAR <- PC
        @(posedge Clk); 
        IR_in = 8'h00; // IR 'don't care' durante o Fetch
        
        // C2 (S1_FETCH): PC <- PC + 1
        @(posedge Clk);
        IR_in = 8'h01;

        // C3 (S2_FETCH): IR <- M[MAR] (Simulamos o carregamento do opcode 01)
        @(posedge Clk);
        IR_in = 8'h02; // Força IR=LDA_IMM no final do ciclo de S2
        
        // C4 (S3_DECODE): Decodifica 01 (LDA_IMM) -> S4_LDA_IMM
        @(posedge Clk);
        IR_in = 8'h03; // Mantém o IR
        
        // EXECUÇÃO LDA_IMM
        
        // C5 (S4_LDA_IMM): MAR <- PC (PC aponta para o dado imediato)
        @(posedge Clk);
        IR_in = 8'h04;xs
        
        // C6 (S5_LDA_IMM): PC <- PC + 1
        @(posedge Clk);
        IR_in = 8'h05;
        
        // C7 (S6_LDA_IMM): A <- M[MAR] (Carga do dado para o Acumulador A)
        @(posedge Clk);
        IR_in = 8'h06;

        // 3. FETCH + ADD_IMM (Opcode 8'h21)
        
        // C8 (S0_FETCH): MAR <- PC
        @(posedge Clk); 
        IR_in = 8'h00; 
        
        // C9 (S1_FETCH): PC <- PC + 1
        @(posedge Clk);

        // C10 (S2_FETCH): IR <- M[MAR] (Simulamos o carregamento do opcode 21)
        @(posedge Clk);
        IR_in = 8'h21; // Força IR=ADD_IMM 
        
        // C11 (S3_DECODE): Decodifica 21 (ADD_IMM) -> S4_ADD_IMM
        @(posedge Clk);
        IR_in = 8'h21; 
        
        // EXECUÇÃO ADD_IMM
        
        // C12 (S4_ADD_IMM): MAR <- PC
        @(posedge Clk);
        
        // C13 (S5_ADD_IMM): PC <- PC + 1, B <- M[MAR] 
        @(posedge Clk);
        
        // C14 (S6_ADD_IMM): A <- A + B, CCR <- Result
        @(posedge Clk);
        
        #50 $finish; 
    end

endmodule