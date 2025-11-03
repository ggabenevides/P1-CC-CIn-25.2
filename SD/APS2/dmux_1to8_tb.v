`timescale 1ns / 1ps

module dmux8_1to8_tb;

    // inputs (reg)
    reg [7:0] A_tb;
    reg [2:0] Sel_tb; 
    
    //outputs (wire)
    wire [7:0] Y0_tb, Y1_tb, Y2_tb, Y3_tb, Y4_tb, Y5_tb, Y6_tb, Y7_tb;
    
    localparam TEST_DATA = 8'hAA; 
    
    // instanciando o teste
    dmux8_1to8 DUT (
        .Y0(Y0_tb), .Y1(Y1_tb), .Y2(Y2_tb), .Y3(Y3_tb),
        .Y4(Y4_tb), .Y5(Y5_tb), .Y6(Y6_tb), .Y7(Y7_tb),
        .A(A_tb),
        .Sel(Sel_tb)
    );

    initial begin

        $dumpfile("dmux8_1to8_tb.vcd");
        $dumpvars(0, dmux8_1to8_tb); 

        //Teste de Roteamento com Dados ATIVOS (A = 8'hAA)
        A_tb = TEST_DATA; 

        // Sel=000 (0) -> Y0 = AA
        Sel_tb = 3'b000;
        #10;

        // Sel=001 (1) -> Y1 = AA
        Sel_tb = 3'b001; 
        #10;

        // Sel=010 (2) -> Y2 = AA
        Sel_tb = 3'b010;
        #10;

        // Sel=011 (3) -> Y3 = AA
        Sel_tb = 3'b011; 
        #10;

        // Sel=100 (4) -> Y4 = AA
        Sel_tb = 3'b100;
        #10;

        // Sel=101 (5) -> Y5 = AA
        Sel_tb = 3'b101; 
        #10;

        // Sel=110 (6) -> Y6 = AA
        Sel_tb = 3'b110;
        #10;

        // Sel=111 (7) -> Y7 = AA
        Sel_tb = 3'b111; 
        #10;
        
        // Teste de Saída Inativa (A = 8'h00)
        A_tb = 8'h00; 

        // Sel=100 (4) -> Y4 = 00
        Sel_tb = 3'b100;
        #10;
        
        // Sel=001 (1) -> Y1 = 00
        Sel_tb = 3'b001;
        #10;

        $finish; 
    end

endmodule