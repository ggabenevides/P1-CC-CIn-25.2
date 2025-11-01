`timescale 1ns / 1ps

module mux8_4to1_tb;

    // inputs (reg)
    reg [7:0] A_tb, B_tb, C_tb, D_tb; 
    reg [1:0] Sel_tb;
    
    // outputs (wire)
    wire [7:0] F_tb;
    
    // instanciando o teste
    mux8_4to1 DUT (.F (F_tb), .A (A_tb), .B (B_tb), .C (C_tb), .D (D_tb), .Sel (Sel_tb));

    initial begin
        
        $dumpfile("mux8_4to1_tb.vcd");
        $dumpvars(0, mux8_4to1_tb); 

        // atribuindo valores aos inputs de dados
        A_tb = 8'h11; // 00010001
        B_tb = 8'h22; // 00100010
        C_tb = 8'h44; // 01000100
        D_tb = 8'h88; // 10001000
        Sel_tb = 2'b00;
        #5;

        // A (Sel = 00) -> F = 8'h11 = 00010001
        Sel_tb = 2'b00;
        #10;

        // B (Sel = 01) -> F = 8'h22 = 00100010
        Sel_tb = 2'b01;
        #10;

        // C (Sel = 10) -> F = 8'h44 = 01000100
        Sel_tb = 2'b10;
        #10;

        // D (Sel = 11) -> F = 8'h88 = 10001000
        Sel_tb = 2'b11;
        #10;
        
        // mudando dados e verificando mais uma vez
        A_tb = 8'hF0; // 11110000
        D_tb = 8'h0F; // 00001111
        Sel_tb = 2'b00; // A -> F = 8'hF0 = 11110000
        #10;
        
        $finish;
    end
endmodule