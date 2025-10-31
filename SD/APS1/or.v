module  or (output F, input wire A, B);
  
  wire G, H;

  nand(G, A, A);
  nand(H, B, B);
  nand(F, G, H);

endmodule