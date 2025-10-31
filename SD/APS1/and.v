module  and (output wire F, input wire A, B);
  
  wire P;

  nand(P, A, B);
  nand(F, P, P);

endmodule