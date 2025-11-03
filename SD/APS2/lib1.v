// modulos 1bit
module not1b (output wire F, input wire A);

  nand (F, A, A); 

endmodule

module  and1b (output wire F, input wire A, B);
  
  wire P;

  nand(P, A, B);
  nand(F, P, P);

endmodule

module  or1b (output wire F, input wire A, B);
  
  wire G, H;

  nand(G, A, A);
  nand(H, B, B);
  nand(F, G, H);

endmodule

module  xor1b (output wire F, input wire A, B);
  
  wire P, G, H;

  nand(P, A, B);
  nand(G, A, P);
  nand(H, B, P);
  nand(F, G, H);

endmodule

//modulos 8bit - unidade logica
module  not8b (output wire [7:0] F, input wire [7:0] A);
  
  genvar i;
      generate
          for (i = 0; i <= 7; i = i + 1) begin : bit_slice
              not1b NOT_inst (.F (F[i]), .A (A[i]));
          end
      endgenerate
    
endmodule

module  and8b (output wire [7:0] F, input wire [7:0] A, input wire [7:0] B);
  
  genvar i;
      generate
          for (i = 0; i <= 7; i = i + 1) begin : bit_slice
              and1b AND_inst (.F (F[i]), .A (A[i]), .B (B[i]));
          end
      endgenerate

endmodule

module or8b (output wire [7:0] F, input wire [7:0] A, input wire [7:0] B);
  
  genvar i;
      generate
          for (i = 0; i <= 7; i = i + 1) begin : bit_slice
              or1b OR_inst (.F (F[i]), .A (A[i]), .B (B[i]));
          end
      endgenerate

endmodule

module or8b_bw (output wire F, input wire [7:0] A);
  
  //declarando fios intermediarios
  wire temp0, temp1, temp2, temp3, temp4, temp5;

  or1b or0bw (.F(temp0), .A(A[0]), .B(A[1]));
  or1b or1bw (.F(temp1), .A(temp0), .B(A[2]));
  or1b or2bw (.F(temp2), .A(temp1), .B(A[3]));
  or1b or3bw (.F(temp3), .A(temp2), .B(A[4]));
  or1b or4bw (.F(temp4), .A(temp3), .B(A[5]));
  or1b or5bw (.F(temp5), .A(temp4), .B(A[6]));
  or1b or6bw (.F(F), .A(temp5), .B(A[7]));

endmodule

// multiplexadores p seleção na ula
module  xor8b (output wire [7:0] F, input wire [7:0] A, input wire [7:0] B);
  
  genvar i;
      generate
          for (i = 0; i <= 7; i = i + 1) begin : bit_slice
              xor1b XOR_inst (.F (F[i]), .A (A[i]), .B (B[i]));
          end
      endgenerate

endmodule

module mux8_4to1 (output wire [7:0] F, 
                  input wire [7:0] A, input wire [7:0] B, input wire [7:0] C, input wire [7:0] D, 
                  input wire [1:0] Sel);

        // fios internos de controle complementares
        wire comp_S0, comp_S1;
        
        // fios intermediarios
        wire [7:0] prod_A, prod_B, prod_C, prod_D;
        wire [7:0] prod_A_temp, prod_B_temp, prod_C_temp, prod_D_temp;
        wire [7:0] or_temp1, or_temp2;

        // mintermos
        not1b not1 (.F(comp_S0), .A(Sel[0]));
        not1b not2 (.F(comp_S1), .A(Sel[1]));

        // multiplicando dados pelo mintermo correto
        and8b and1 (.F(prod_A_temp), .A(A), .B({8{comp_S1}})); //quando sel = 00, seleciona A
        and8b and2 (.F(prod_A), .A(prod_A_temp), .B({8{comp_S0}}));

        and8b and3 (.F(prod_B_temp), .A(B), .B({8{comp_S1}})); //quando sel = 01, seleciona B
        and8b and4 (.F(prod_B), .A(prod_B_temp), .B({8{Sel[0]}}));

        and8b and5 (.F(prod_C_temp), .A(C), .B({8{Sel[1]}})); // quando sel = 10, seleciona C
        and8b and6 (.F(prod_C), .A(prod_C_temp), .B({8{comp_S0}}));

        and8b and7 (.F(prod_D_temp), .A(D), .B({8{Sel[1]}})); //quando sel = 11, seleciona D
        and8b and8 (.F(prod_D), .A(prod_D_temp), .B({8{Sel[0]}}));

        // sop
        or8b or1 (.F(or_temp1), .A(prod_A), .B(prod_B));
        or8b or2 (.F(or_temp2), .A(prod_C), .B(or_temp1));
        or8b or3 (.F(F), .A(or_temp2), .B(prod_D));

endmodule 

module mux8_2to1 (output wire [7:0] F, input wire [7:0] A, input wire [7:0] B, input wire Sel);

        // fio interno complementar
        wire comp;

        // atribuindo valor ao fio complementar pra gerar mintermos
        not1b not1 (.F(comp), .A(Sel));

        // fios intermediarios
        wire [7:0] prod_A, prod_B;

        and8b and1 (.F(prod_A), .A(A), .B({8{comp}}));
        and8b and2 (.F(prod_B), .A(B), .B({8{Sel}}));

        or8b or1 (.F(F), .A(prod_A), .B(prod_B));

endmodule 

// modulos da unidade aritmetica 
module half_adder (output wire S, output wire C, input wire A, input wire B);

        xor1b xor1 (.F(S), .A(A), .B(B));
        and1b and1 (.F(C), .A(A), .B(B));

endmodule

module full_adder (output wire S, output wire Cout, 
                   input wire A, input wire B, input wire Cin);

        // fios intermediarios 
        wire Sum1, C1, C2;

        // A + B 
        half_adder HA1 (.S (Sum1), .C (C1), .A (A), .B (B));

        // soma: Sum1 + Cin 
        half_adder HA2 (.S (S), .C (C2), .A (Sum1), .B (Cin));

        // carry out : C1 ou C2
        or1b or1 (.F (Cout), .A (C1), .B (C2));

endmodule

// somador de 8 bits (ripple carry)
module adder8b (output wire [7:0] Sum,
                  output wire Cout,
                  input wire [7:0] A,
                  input wire [7:0] B,
                  input wire Cin);

        // fios internos pra transmitir os carry-outs
        wire [7:0] C; 

        // FA0 (LSB)
        full_adder FA0 (.S (Sum[0]), .Cout (C[0]), .A (A[0]), .B (B[0]), .Cin (Cin));

        // FA1
        full_adder FA1 (.S (Sum[1]), .Cout (C[1]), .A (A[1]), .B (B[1]), .Cin (C[0]));

        // FA2
        full_adder FA2 (.S (Sum[2]), .Cout (C[2]), .A (A[2]), .B (B[2]), .Cin (C[1]));

        // FA3
        full_adder FA3 (.S (Sum[3]), .Cout (C[3]), .A (A[3]), .B (B[3]), .Cin (C[2]));

        // FA4
        full_adder FA4 (.S (Sum[4]), .Cout (C[4]), .A (A[4]), .B (B[4]), .Cin (C[3]));

        // FA5
        full_adder FA5 (.S (Sum[5]), .Cout (C[5]), .A (A[5]), .B (B[5]), .Cin (C[4]));

        // FA6
        full_adder FA6 (.S (Sum[6]), .Cout (C[6]), .A (A[6]), .B (B[6]), .Cin (C[5]));

        // FA7 (MSB)
        full_adder FA7 (.S (Sum[7]), .Cout (Cout), .A (A[7]), .B (B[7]), .Cin (C[6]));

endmodule

// demultiplexador pra usar na lógica de flags
module dmux8_1to8 (
    output wire [7:0] Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7, // 8 Saídas de 8 bits
    input wire [7:0] A,                               // Entrada de Dados de 8 bits
    input wire [2:0] Sel                              // Seleção de 3 bits
);

    // Fios internos de controle complementares (complementos do Sel)
    wire comp_S0, comp_S1, comp_S2;
    
    // Mintermo 0 (Sel=000)
    not1b inst_not_S0 (.F(comp_S0), .A(Sel[0]));
    not1b inst_not_S1 (.F(comp_S1), .A(Sel[1]));
    not1b inst_not_S2 (.F(comp_S2), .A(Sel[2]));
    
    // Y0 (Sel=000): A & ~S2 & ~S1 & ~S0
    and8b inst_and_Y0 (.F(Y0), .A(A), .B({8{comp_S2 & comp_S1 & comp_S0}}));
    
    // Y1 (Sel=001): A & ~S2 & ~S1 & S0
    and8b inst_and_Y1 (.F(Y1), .A(A), .B({8{comp_S2 & comp_S1 & Sel[0]}}));

    // Y2 (Sel=010): A & ~S2 & S1 & ~S0
    and8b inst_and_Y2 (.F(Y2), .A(A), .B({8{comp_S2 & Sel[1] & comp_S0}}));

    // Y3 (Sel=011): A & ~S2 & S1 & S0
    and8b inst_and_Y3 (.F(Y3), .A(A), .B({8{comp_S2 & Sel[1] & Sel[0]}}));
    
    // Y4 (Sel=100): A & S2 & ~S1 & ~S0
    and8b inst_and_Y4 (.F(Y4), .A(A), .B({8{Sel[2] & comp_S1 & comp_S0}}));

    // Y5 (Sel=101): A & S2 & ~S1 & S0
    and8b inst_and_Y5 (.F(Y5), .A(A), .B({8{Sel[2] & comp_S1 & Sel[0]}}));

    // Y6 (Sel=110): A & S2 & S1 & ~S0
    and8b inst_and_Y6 (.F(Y6), .A(A), .B({8{Sel[2] & Sel[1] & comp_S0}}));

    // Y7 (Sel=111): A & S2 & S1 & S0
    and8b inst_and_Y7 (.F(Y7), .A(A), .B({8{Sel[2] & Sel[1] & Sel[0]}}));

endmodule