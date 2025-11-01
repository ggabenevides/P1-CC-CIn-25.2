`timescale 1ns / 1ps

module or8b_tb;

    // inputs (reg)
    reg [7:0] A_tb, B_tb; 
    
    // outputs (wire)
    wire [7:0] F_tb;
    
    // instanciando teste
    or8b DUT (.F (F_tb), .A (A_tb), .B (B_tb));

    initial begin

        $dumpfile("or8b_tb.vcd");
        $dumpvars(0, or8b_tb); 

        // A=0, B=0 -> F=0 (estado inicial)
        A_tb = 8'h00; 
        B_tb = 8'h00; 
        #10;

        // A=11111111, B=00000000 -> F=11111111 
        A_tb = 8'hFF; 
        B_tb = 8'h00; 
        #10;

        // A=00000000, B=00000000 -> F=00000000
        A_tb = 8'h00; 
        B_tb = 8'h00; 
        #10;

        // A = 10101010, B = 01010101 -> F=11111111 
        A_tb = 8'hAA; 
        B_tb = 8'h55; 
        #10;

        // A = 01011001, B = 11010110 -> F = 11011111 = DF.
        A_tb = 8'h59; 
        B_tb = 8'hD6; 
        #10;


        $finish;
    end
endmodule