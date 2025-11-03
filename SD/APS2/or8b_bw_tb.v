`timescale 1ns / 1ps

module or8b_bw_tb;

    // inputs (reg)
    reg [7:0] A_tb; 
    
    // outputs (wire)
    wire F_tb;
    
    // instanciando teste
    or8b_bw DUT (.F(F_tb), .A(A_tb));

    initial begin

        $dumpfile("or8b_bw_tb.vcd");
        $dumpvars(0, or8b_bw_tb); 

        // A=00000000 -> F=0 (estado inicial)
        A_tb = 8'h00; 
        #10;

        // A=11111111 -> F=1
        A_tb = 8'hFF; 
        #10;

        // A=00000001 -> F=1
        A_tb = 8'h01; 
        #10;

        // A = 10101010 -> F=1
        A_tb = 8'hAA; 
        #10;

        $finish;
    end
endmodule