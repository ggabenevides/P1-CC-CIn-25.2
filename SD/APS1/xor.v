module  xor (output F, input wire A, B);
  
  wire P, G, H;

  nand(P, A, B);
  nand(G, A, P);
  nand(H, B, P);
  nand(F, G, H);

endmodule