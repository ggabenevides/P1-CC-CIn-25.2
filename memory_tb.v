`timescale 1ps/1ps

module memory_tb;

reg clk;
reg reset;
reg write;
reg [7:0] data_in;
reg [7:0] address;
reg [7:0] port_in_00;
reg [7:0] port_in_01;
reg [7:0] port_in_02;
reg [7:0] port_in_03;
reg [7:0] port_in_04;
reg [7:0] port_in_05;
reg [7:0] port_in_06;
reg [7:0] port_in_07;
reg [7:0] port_in_08;
reg [7:0] port_in_09;
reg [7:0] port_in_10;
reg [7:0] port_in_11;
reg [7:0] port_in_12;
reg [7:0] port_in_13;
reg [7:0] port_in_14;
reg [7:0] port_in_15;

wire [7:0] data_out;
wire [7:0] port_out_00;
wire [7:0] port_out_01;
wire [7:0] port_out_02;
wire [7:0] port_out_03;
wire [7:0] port_out_04;
wire [7:0] port_out_05;
wire [7:0] port_out_06;
wire [7:0] port_out_07;
wire [7:0] port_out_08;
wire [7:0] port_out_09;
wire [7:0] port_out_10;
wire [7:0] port_out_11;
wire [7:0] port_out_12;
wire [7:0] port_out_13;
wire [7:0] port_out_14;
wire [7:0] port_out_15;

memory DUT (.address(address), .data_in(data_in), .write(write), .clk(clk), .reset(reset), .data_out(data_out), .port_out_00(port_out_00), .port_out_01(port_out_01), .port_out_02(port_out_02), .port_out_03(port_out_03), .port_out_04(port_out_04), .port_out_05(port_out_05), .port_out_06(port_out_06), .port_out_07(port_out_07), .port_out_08(port_out_08), .port_out_09(port_out_09), .port_out_10(port_out_10), .port_out_11(port_out_11), .port_out_12(port_out_12), .port_out_13(port_out_13), .port_out_14(port_out_14), .port_out_15(port_out_15), .port_in_00(port_in_00), .port_in_01(port_in_01), .port_in_02(port_in_02), .port_in_03(port_in_03), .port_in_04(port_in_04), .port_in_05(port_in_05), .port_in_06(port_in_06), .port_in_07(port_in_07), .port_in_08(port_in_08), .port_in_09(port_in_09), .port_in_10(port_in_10), .port_in_11(port_in_11), .port_in_12(port_in_12), .port_in_13(port_in_13), .port_in_14(port_in_14), .port_in_15(port_in_15));

initial clk = 0;

always #10
    clk = ~clk;

initial
    begin

        write = 0;
        reset = 1;
        address = 8'hF0;
        data_in = 8'hF1;

        @ (posedge clk);
        @ (posedge clk);
        @ (posedge clk);
      
      	reset = 0;
      
		@ (posedge clk);
      
        // ROM: teste de leitura

        write = 0;
        address = 0;
        @ (posedge clk);
      	@ (posedge clk);
        if (data_out == 8'h86) $display("ROM TEST: PASS");
        else $display("ROM TEST: FAIL");
        
        @ (posedge clk);

        // RW: teste de escrita
        
        write = 1;
        address = 128;
        data_in = 8'h80;
        @ (posedge clk);
        write = 0;
      	address = 128;
      	@ (posedge clk);

        // RW: teste de leitura

        write = 0;
        address = 128;
      	data_in = 8'h80;
        @ (posedge clk);
        if (data_out == data_in) $display("RW READING TEST: PASS");
        else $display("RW READING TEST: FAIL");

        @ (posedge clk);

        // PORT OUT: teste de escrita
      	
      	reset = 1;
      	
      	@ (posedge clk);
      
        write = 1;
        data_in = 8'hF5;
        address = 8'hE5;
        @ (posedge clk);
        write = 0;
        @ (posedge clk);
        if (port_out_05 == 8'hF5) $display("PORT OUT WRITING TEST: PASS");
        else $display("PORT OUT WRITING TEST: FAIL — EXPECTED F5, GOT %h", port_out_05);

        @ (posedge clk);

        write = 1;
      	@ (posedge clk);
        data_in = 8'hF6;
        address = 8'hE6;
        @ (posedge clk);
        write = 0;
        @ (posedge clk);
        if (port_out_06 == 8'hF6) $display("PORT OUT WRITING TEST: PASS");
        else $display("PORT OUT WRITING TEST: FAIL — EXPECTED F6, GOT %h", port_out_06);

        @ (posedge clk);

        write = 1;
      	@ (posedge clk);
        data_in = 8'hF7;
        address = 8'hE7;
        @ (posedge clk);
        write = 0;
        @ (posedge clk);
        if (port_out_07 == 8'hF7) $display("PORT OUT WRITING TEST: PASS");
        else $display("PORT OUT WRITING TEST: FAIL — EXPECTED F7, GOT %h", port_out_07);

        @ (posedge clk);
 
        write = 1;
      	@ (posedge clk);
        data_in = 8'hF8;
        address = 8'hE8;
        @ (posedge clk);
        write = 0;
        @ (posedge clk);
        if (port_out_08 == 8'hF8) $display("PORT OUT WRITING TEST: PASS");
        else $display("PORT OUT WRITING TEST: FAIL — EXPECTED F5, GOT %h", port_out_08);

        @ (posedge clk);
      	
      $dumpfile("waveform.vcd");
      $dumpvars(0, memory_tb);
      $finish;

    end

endmodule   