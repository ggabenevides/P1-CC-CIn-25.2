`timescale 1ns/1ps
`include "data_path.v"

module data_path_tb;

    // Outputs do DUT
    wire [7:0] address;
    wire [7:0] to_memory;
    wire [7:0] IR_out;
    wire [3:0] CCR_Result;

    // Inputs do DUT
    reg  [7:0] from_memory;
    reg  [2:0] ALU_Sel;
    reg  [1:0] Bus1_Sel, Bus2_Sel;
    reg  IR_Load, MAR_Load, PC_Load, A_Load, B_Load, CCR_Load;
    reg  Clk, Reset;

    // Instância do DUT
    data_path dut (
        .address(address),
        .to_memory(to_memory),
        .IR_out(IR_out),
        .CCR_Result(CCR_Result),
        .from_memory(from_memory),
        .ALU_Sel(ALU_Sel),
        .Bus1_Sel(Bus1_Sel),
        .Bus2_Sel(Bus2_Sel),
        .IR_Load(IR_Load),
        .MAR_Load(MAR_Load),
        .PC_Load(PC_Load),
        .A_Load(A_Load),
        .B_Load(B_Load),
        .CCR_Load(CCR_Load),
        .Clk(Clk),
        .Reset(Reset)
    );

    // Clock de 10 ns
    always #5 Clk = ~Clk;

    initial begin
        // >>> GERAÇÃO DO ARQUIVO DE ONDAS <<<
        $dumpfile("data_path_tb.vcd");
        $dumpvars(0, data_path_tb);

        // Inicialização
        Clk = 0;
        Reset = 1;
        IR_Load = 0; MAR_Load = 0; PC_Load = 0;
        A_Load  = 0; B_Load  = 0; CCR_Load = 0;
        Bus1_Sel = 0; Bus2_Sel = 0;
        ALU_Sel = 0;
        from_memory = 0;

        #10 Reset = 0;

        /* =========================
           TESTE 1: Carregar registradores da memória
           (IR, PC, A, B)
        ==========================*/
        from_memory = 8'h3C;
        Bus2_Sel = 2'b10; // from_memory
        IR_Load = 1; PC_Load = 1; A_Load = 1; B_Load = 1;
        #10;
        IR_Load = 0; PC_Load = 0; A_Load = 0; B_Load = 0;

        /* =========================
           TESTE 2: Enviar PC para memória
        ==========================*/
        Bus1_Sel = 2'b00; // PC
        #10;

        /* =========================
           TESTE 3: ALU soma A + B
        ==========================*/
        ALU_Sel = 3'b000; // ADD
        Bus2_Sel = 2'b00; // ALU_Result
        CCR_Load = 1;
        #10;
        CCR_Load = 0;

        /* =========================
           TESTE 4: Operação lógica (A AND B)
        ==========================*/
        ALU_Sel = 3'b010; // AND
        CCR_Load = 1;
        #10;
        CCR_Load = 0;

        /* =========================
           TESTE 5: Carregar MAR e verificar address
        ==========================*/
        from_memory = 8'hA5;
        Bus2_Sel = 2'b10; // from_memory
        MAR_Load = 1;
        #10;
        MAR_Load = 0;

        /* =========================
           Fim da simulação
        ==========================*/
        #20;
        $stop;
    end

endmodule
