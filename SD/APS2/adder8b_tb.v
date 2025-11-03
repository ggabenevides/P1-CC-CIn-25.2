`timescale 1ns / 1ps

module adder8b_tb;

    // inputs (reg)
    reg [7:0] A_tb, B_tb; 
    reg Cin_tb; 
    
    // outputs (wire)
    wire [7:0] Sum_tb;
    wire Cout_tb;
    
    // instanciando teste
    adder8b DUT (.Sum(Sum_tb), .Cout(Cout_tb), .A(A_tb), .B(B_tb), .Cin(Cin_tb));

    initial begin

        $dumpfile("adder8b_tb.vcd");
        $dumpvars(0, adder8b_tb); 

        // A=010101010, B=11101011 Cin=0 -> S=10010101 = (95)hex, Cout=1
        A_tb = 8'hAA;
        B_tb = 8'hEB;
        Cin_tb = 1'b0;  
        #10;

        // A=01100100 , B=00000100  Cin=0 -> S=01101000 = (68)hex, Cout=0
        A_tb = 8'h64;
        B_tb = 8'h04;
        Cin_tb = 1'b0;  
        #10;

        // A=11111111 , B=0000001  Cin=0 -> S=00000000 = (00)hex, Cout=1
        A_tb = 8'hFF;
        B_tb = 8'h01;
        Cin_tb = 1'b0;  
        #10;    

        // A=11111111 , B=11111111  Cin=0 -> S=11111110 = (FE)hex, Cout=1
        A_tb = 8'hFF;
        B_tb = 8'hFF;
        Cin_tb = 1'b0;  
        #10;

        // A=00000000 , B=00000000  Cin=1 -> S=00000001 = (01)hex, Cout=0
        A_tb = 8'h00;
        B_tb = 8'h00;
        Cin_tb = 1'b1;  
        #10; 

        // A=11111111 , B=00000100  Cin=1  -> S=00000000 = (00)hex, Cout=1
        A_tb = 8'hFF;
        B_tb = 8'h00;
        Cin_tb = 1'b1;  
        #10;

        $finish;
    end
endmodule