`timescale 1ns / 1ps

module full_adder_tb;

    // inputs (reg)
    reg A_tb, B_tb, Cin_tb; 
    
    // outputs (wire)
    wire S_tb, Cout_tb;
    
    // instanciando teste
    full_adder DUT (.S(S_tb), .Cout(Cout_tb), .A(A_tb), .B(B_tb), .Cin(Cin_tb));

    initial begin

        $dumpfile("full_adder_tb.vcd");
        $dumpvars(0, full_adder_tb); 

        // A=0, B=0 Cin=0 -> S=0, Cout=0
        A_tb = 1'b0;
        B_tb = 1'b0;
        Cin_tb = 1'b0;  
        #10;

        // A=0, B=0 Cin=1 -> S=1, Cout=0
        A_tb = 1'b0;
        B_tb = 1'b0;
        Cin_tb = 1'b1;  
        #10;

        // A=0, B=1 Cin=0 -> S=1, Cout=0
        A_tb = 1'b0;
        B_tb = 1'b1;
        Cin_tb = 1'b0;  
        #10;

        // A=0, B=1 Cin=1 -> S=0, Cout=1
        A_tb = 1'b0;
        B_tb = 1'b1;
        Cin_tb = 1'b1;  
        #10;

        // A=1, B=0 Cin=0 -> S=1, Cout=0
        A_tb = 1'b1;
        B_tb = 1'b0;
        Cin_tb = 1'b0;  
        #10;

        // A=1, B=0 Cin=1 -> S=0, Cout=1
        A_tb = 1'b1;
        B_tb = 1'b0;
        Cin_tb = 1'b1; 
        #10;

        // A=1, B=1 Cin=0 -> S=0, Cout=1
        A_tb = 1'b1;
        B_tb = 1'b1;
        Cin_tb = 1'b0; 
        #10;

        // A=1, B=1 Cin=1 -> S=1, Cout=1
        A_tb = 1'b1;
        B_tb = 1'b1;
        Cin_tb = 1'b1;  
        #10;

        $finish;
    end
endmodule