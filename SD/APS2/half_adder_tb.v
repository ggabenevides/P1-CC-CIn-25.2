`timescale 1ns / 1ps

module half_adder_tb;

    // inputs (reg)
    reg A_tb, B_tb; 
    
    // outputs (wire)
    wire S_tb, C_tb;
    
    // instanciando teste
    half_adder DUT (.S(S_tb), .C(C_tb), .A(A_tb), .B(B_tb));

    initial begin

        $dumpfile("half_adder_tb.vcd");
        $dumpvars(0, half_adder_tb); 

        // A=0, B=0 -> S=0, C=0
        A_tb = 1'b0;
        B_tb = 1'b0;  
        #10;

        // A=0, B=1 -> S=1, C=0
        A_tb = 1'b0;
        B_tb = 1'b1;   
        #10;

        // A=1, B=0 -> S=1, C=0
        A_tb = 1'b1;
        B_tb = 1'b0;  
        #10;

        // A=1, B=1 -> S=0, C=1
        A_tb = 1'b1;
        B_tb = 1'b1;  
        #10;

        $finish;
    end
endmodule