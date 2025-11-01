module xor1b_tb();

	reg fio1, fio2;
	wire fio3;
    
  	xor1b xor1(.F(fio3), .A(fio1), .B(fio2));
    
  	initial begin
      $dumpfile("xor1b_tb.vcd");
      $dumpvars(0, xor1b_tb);

      fio1 = 1'b0;
      fio2 = 1'b0;
      #5;

      fio1 = 1'b1;
      fio2 = 1'b0;
      #5;

      fio1 = 1'b0;
      fio2 = 1'b1;
      #5;

      fio1 = 1'b1;
      fio2 = 1'b1;
      #5;  
    end
endmodule