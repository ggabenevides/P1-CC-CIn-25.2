module inv_tb();

	reg fio1;
	wire fio2;
    
  	not inv1(.F(fio2), .A(fio1));
    
  	initial begin
      $dumpfile("INV_tb.vcd");
      $dumpvars(0, INV_tb);

      fio1 = 1'b0;
      #5;

      fio1 = 1'b1;
      #5;
    end
endmodule