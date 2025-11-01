module not1b_tb();

	reg fio1;
	wire fio2;
    
  	not1b inv1(.F(fio2), .A(fio1));
    
  	initial begin
      $dumpfile("not1b_tb.vcd");
      $dumpvars(0, not1b_tb);

      fio1 = 1'b0;
      #5;

      fio1 = 1'b1;
      #5;
    end
endmodule