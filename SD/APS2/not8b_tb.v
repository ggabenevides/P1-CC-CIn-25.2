`timescale 1ns / 1ps

module not8b_tb;

    // inputs (reg)
    reg [7:0] A_tb; 
    
    // outputs (wire)
    wire [7:0] F_tb;
    
    // instanciando teste
    not8b DUT (.F (F_tb), .A (A_tb));

    initial begin

        $dumpfile("not8b_tb.vcd");
        $dumpvars(0, not8b_tb); 

        // A=00000000 -> F=11111111 = FF
        A_tb = 8'h00;  
        #10;

        // A=11111111 -> F=00000000 = 00
        A_tb = 8'hFF; 
        #10;

        // A=01100101 -> F=10011010 = 9A
        A_tb = 8'h65; 
        #10;

        // A = 10101010 -> F=01010101 = 55
        A_tb = 8'hAA; 
        #10;

        // A = 01011001 -> F = 10100110 = A6.
        A_tb = 8'h59; 
        #10;


        $finish;
    end
endmodule