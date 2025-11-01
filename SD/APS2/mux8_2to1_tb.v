`timescale 1ns / 1ps

module mux8_2to1_tb;

    // inputs (reg)
    reg [7:0] A_tb, B_tb; 
    reg  Sel_tb;
    
    // outputs (wire)
    wire [7:0] F_tb;
    
    // instanciando o teste
    mux8_2to1 DUT (.F (F_tb), .A (A_tb), .B (B_tb), .Sel (Sel_tb));

    initial begin
        
        $dumpfile("mux8_2to1_tb.vcd");
        $dumpvars(0, mux8_2to1_tb); 

        // atribuindo valores aos inputs de dados
        A_tb = 8'h11; // 00010001
        B_tb = 8'h22; // 00100010
        Sel_tb = 1'b0;
        #5;

        // A (Sel = 0) -> F = 8'h11 
        Sel_tb = 2'b00;
        #10;

        // B (Sel = 1) -> F = 8'h22
        Sel_tb = 2'b01;
        #10;
        
        // mudando dados e verificando mais uma vez
        A_tb = 8'hF0; // 11110000
        B_tb = 8'h0F; // 00001111
        Sel_tb = 1'b0; // A -> F = 8'hF0
        #10;
        
        $finish;
    end
endmodule