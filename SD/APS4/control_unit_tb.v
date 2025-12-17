`timescale 1ns/1ps
`include "control_unit.v"

module control_unit_tb;

    // sinais para a Unidade de Controle
    reg Clk = 1'b0;
    reg Reset = 1'b0;
    reg [7:0] IR_in = 8'h00; // simula a saída do registrador IR (entrada para a UC)
    reg [3:0] CCR_Result_in = 4'b0000;

    // saídas da Unidade de Controle 
    wire IR_Load, MAR_Load, PC_Load, PC_Inc;
    wire A_Load, B_Load, CCR_Load;
    wire [2:0] ALU_Sel;
    wire [1:0] Bus1_Sel, Bus2_Sel;
    wire write; 

    // instanciação device under test
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

    // geração do clock (50% duty cycle, 20ns period)
    always #10 Clk = ~Clk;

    initial begin
        $dumpfile("control_unit_tb.vcd");
        $dumpvars(0, control_unit_tb);

        // reset
        Reset = 1'b0;
        #20 Reset = 1'b1; // reset assíncrono ativo baixo
        
        // IR_in deve ser forçado com o opcode correto apenas no final de S2_FETCH

        // TESTE 1: LDA_IMM (Load A Immediate - Opcode 8'h01)
        // duração: 3 fetch + 3 execute = 6 ciclos

        // C1 (S0_FETCH)
        @(posedge Clk); IR_in = 8'h00;
        // C2 (S1_FETCH)
        @(posedge Clk);
        // C3 (S2_FETCH): IR <- M[MAR]
        @(posedge Clk); IR_in = 8'h01; // Força IR=LDA_IMM
        // C4 (S3_DECODE)
        @(posedge Clk); 
        
        // EXECUÇÃO LDA_IMM
        // C5 (S4_LDA_IMM)
        @(posedge Clk);
        // C6 (S5_LDA_IMM)
        @(posedge Clk);
        // C7 (S6_LDA_IMM)
        @(posedge Clk); 

        // TESTE 2: ADD_IMM (Add Immediate - Opcode 8'h21)
        // duração: 3 fetch + 3 execute = 6 ciclos

        // C8 (S0_FETCH)
        @(posedge Clk); IR_in = 8'h00;
        // C9 (S1_FETCH)
        @(posedge Clk);
        // C10 (S2_FETCH): IR <- M[MAR]
        @(posedge Clk); IR_in = 8'h21; // força IR=ADD_IMM 
        // C11 (S3_DECODE)
        @(posedge Clk); 
        
        // EXECUÇÃO ADD_IMM
        // C12 (S4_ADD_IMM)
        @(posedge Clk);
        // C13 (S5_ADD_IMM)
        @(posedge Clk);
        // C14 (S6_ADD_IMM)
        @(posedge Clk);

        // TESTE 3: STA_DIR (Store A Direct - Opcode 8'h12)
        // duração: 3 fetch + 3 execute = 6 ciclos
        
        // C15 (S0_FETCH)
        @(posedge Clk); IR_in = 8'h00; 
        // C16 (S1_FETCH)
        @(posedge Clk);
        // C17 (S2_FETCH): IR <- M[MAR]
        @(posedge Clk); IR_in = 8'h12; // força IR=STA_DIR 
        // C18 (S3_DECODE)
        @(posedge Clk); 
        
        // EXECUÇÃO STA_DIR
        // C19 (S4_STA_DIR)
        @(posedge Clk);
        // C20 (S5_STA_DIR)
        @(posedge Clk);
        // C21 (S6_STA_DIR): o sinal 'write' deve ser ativado neste ciclo!
        @(posedge Clk);

        // TESTE 4: LDA_DIR (Load A Direct - opcode 8'h02)
        // duração: 3 fetch + 5 execute = 8 ciclos

        // C22 (S0_FETCH)
        @(posedge Clk); IR_in = 8'h00; 
        // C23 (S1_FETCH)
        @(posedge Clk);
        // C24 (S2_FETCH): IR <- M[MAR] 
        @(posedge Clk); IR_in = 8'h02; // força IR=LDA_DIR 
        // C25 (S3_DECODE)
        @(posedge Clk);
        
        // EXECUÇÃO LDA_DIR 
        // C26 (S4_LDA_DIR)
        @(posedge Clk);
        // C27 (S5_LDA_DIR)
        @(posedge Clk);
        // C28 (S6_LDA_DIR)
        @(posedge Clk);
        // C29 (S7_LDA_DIR)
        @(posedge Clk);
        // C30 (S8_LDA_DIR)
        @(posedge Clk);

        #50 $finish; 
    end

endmodule