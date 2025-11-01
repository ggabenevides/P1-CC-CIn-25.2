`timescale 1ns / 1ps

module and8b_tb;

    // inputs (reg)
    reg [7:0] A_tb, B_tb; 
    
    // outputs (wire)
    wire [7:0] F_tb;
    
    // instanciando teste
    and8b DUT (.F (F_tb), .A (A_tb), .B (B_tb));

    initial begin

        $dumpfile("and8b_tb.vcd");
        $dumpvars(0, and8b_tb); 

        // A=0, B=0 -> F=0 (estado inicial)
        A_tb = 8'h00; 
        B_tb = 8'h00; 
        #10;

        // A=11111111, B=00000000 -> F=00000000 (sem bits em comum)
        A_tb = 8'hFF; 
        B_tb = 8'h00; 
        #10;

        // A=11111111, B=11111111 -> F=11111111
        A_tb = 8'hFF; 
        B_tb = 8'hFF; 
        #10;

        // A = 10101010, B = 01010101 -> F=00000000 (sem bits em comum)
        A_tb = 8'hAA; 
        B_tb = 8'h55; 
        #10;

        // A = 11110000, B = 10100000 -> F = 10100000.
        A_tb = 8'hF0; 
        B_tb = 8'hA0; 
        #10;
        
        // A=11110000, B=00001111 ->  F=00000000 (sem bits em comum)
        A_tb = 8'hF0; 
        B_tb = 8'h0F; 
        #10;

        $finish;
    end
endmodule