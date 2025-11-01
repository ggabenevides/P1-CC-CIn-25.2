`timescale 1ns / 1ps

module xor8b_tb;

    // inputs (reg)
    reg [7:0] A_tb, B_tb; 
    
    // outputs (wire)
    wire [7:0] F_tb;
    
    // instanciando teste
    xor8b DUT (.F (F_tb), .A (A_tb), .B (B_tb));

    initial begin

        $dumpfile("xor8b_tb.vcd");
        $dumpvars(0, xor8b_tb); 

        // A=00000000, B=00000000 -> F=00000000 = 00 (estado inicial)
        A_tb = 8'h00; 
        B_tb = 8'h00; 
        #10;

        // A=11111111, B=11111111 -> F=00000000 = 00
        A_tb = 8'hFF; 
        B_tb = 8'hFF; 
        #10;

        // A=01100101, B=01111011 -> F=00011110 = 1E
        A_tb = 8'h65; 
        B_tb = 8'h7B; 
        #10;

        // A = 10101010, B = 01010101 -> F=11111111 = FF
        A_tb = 8'hAA; 
        B_tb = 8'h55; 
        #10;

        // A = 01011001, B = 11010110 -> F = 10001111 = 8F.
        A_tb = 8'h59; 
        B_tb = 8'hD6; 
        #10;


        $finish;
    end
endmodule