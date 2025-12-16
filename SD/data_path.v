module data_path (
    output reg [7:0] address,
    output reg [7:0] to_memory,
    output reg [7:0] IR_out,
    output reg [3:0] CCR_Result, 

    input wire [7:0] from_memory,
    input wire [2:0] ALU_Sel,
    input wire [1:0] Bus1_Sel, Bus2_Sel,
    input wire IR_Load, MAR_Load, PC_Load, A_Load, B_Load, CCR_Load,  
    input wire Clk, Reset
);

    // Buses
    reg [7:0] Bus1, Bus2;

    // Registers
    reg [7:0] PC, MAR, A, B;
    reg [7:0] ALU_Result;

    /* =========================
       MUX BUS 1
    ==========================*/
    always @(*) begin
        case (Bus1_Sel)
            2'b00: Bus1 = PC;
            2'b01: Bus1 = A;
            2'b10: Bus1 = B;
            default: Bus1 = 8'h00;
        endcase
    end

    /* =========================
       ALU
    ==========================*/
    always @(*) begin
        case (ALU_Sel)
            3'b000: ALU_Result = A + B;
            3'b001: ALU_Result = A - B;
            3'b010: ALU_Result = A & B;
            3'b011: ALU_Result = A | B;
            3'b100: ALU_Result = ~A;
            3'b101: ALU_Result = A ^ B;
            default: ALU_Result = 8'h00;
        endcase
    end

    /* =========================
       MUX BUS 2
    ==========================*/
    always @(*) begin
        case (Bus2_Sel)
            2'b00: Bus2 = ALU_Result;
            2'b01: Bus2 = Bus1;
            2'b10: Bus2 = from_memory;
            default: Bus2 = 8'h00;
        endcase
    end

    /* =========================
       REGISTRADORES
    ==========================*/
    always @(posedge Clk or posedge Reset) begin
        if (Reset) begin
            PC <= 8'h00;
            MAR <= 8'h00;
            A <= 8'h00;
            B <= 8'h00;
            IR_out <= 8'h00;
            CCR_Result <= 4'b0000;
        end else begin
            if (PC_Load)  PC <= Bus2;
            if (MAR_Load) MAR <= Bus2;
            if (A_Load)   A <= Bus2;
            if (B_Load)   B <= Bus2;
            if (IR_Load)  IR_out <= Bus2;

            if (CCR_Load) begin
                CCR_Result[3] <= (ALU_Result == 8'h00); // Zero
                CCR_Result[2] <= ALU_Result[7];         // Negativo
                CCR_Result[1] <= 1'b0;                   // Carry (simplificado)
                CCR_Result[0] <= 1'b0;                   // Overflow (simplificado)
            end
        end
    end

    /* =========================
       SAÍDA PARA MEMÓRIA
    ==========================*/
    always @(*) begin
        to_memory = Bus1;
        address   = MAR;
    end

endmodule
