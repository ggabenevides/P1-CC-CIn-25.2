module mux4to1 (output wire F, input wire A, B, C, D, input wire [1:0] Sel);

        // fios internos de controle complementares
        wire comp_S0, comp_S1;
        
        // fios intermediarios
        wire prod_A, prod_B, prod_C, prod_D;
        wire prod_A_temp, prod_B_temp, prod_C_temp, prod_D_temp;
        wire or_temp1, or_temp2;

        // mintermos
        INV not1 (.F(comp_S0), .A(Sel[0]));
        INV not2 (.F(comp_S1), .A(Sel[1]));

        // multiplicando dados pelo mintermo correto
        AND and1 (.F(prod_A_temp), .A(A), .B(comp_S1)); //quando sel = 00, seleciona A
        AND and2 (.F(prod_A), .A(prod_A_temp), .B(comp_S0));

        AND and3 (.F(prod_B_temp), .A(B), .B(comp_S1)); //quando sel = 01, seleciona B
        AND and4 (.F(prod_B), .A(prod_B_temp), .B(Sel[0]));

        AND and5 (.F(prod_C_temp), .A(C), .B(Sel[1])); // quando sel = 10, seleciona C
        AND and6 (.F(prod_C), .A(prod_C_temp), .B(comp_S0));

        AND and7 (.F(prod_D_temp), .A(D), .B(Sel[1])); //quando sel = 11, seleciona D
        AND and8 (.F(prod_D), .A(prod_D_temp), .B(Sel[0]));

        // sop
        OR or1 (.F(or_temp1), .A(prod_A), .B(prod_B));
        OR or2 (.F(or_temp2), .A(prod_C), .B(or_temp1));
        OR or3 (.F(F), .A(or_temp2), .B(prod_D));

endmodule 