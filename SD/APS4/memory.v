`timescale 1ps/1ps

module memory
(output reg [7:0] port_out_00,
output reg [7:0] port_out_01,
output reg [7:0] port_out_02,
output reg [7:0] port_out_03,
output reg [7:0] port_out_04,
output reg [7:0] port_out_05,
output reg [7:0] port_out_06,
output reg [7:0] port_out_07,
output reg [7:0] port_out_08,
output reg [7:0] port_out_09,
output reg [7:0] port_out_10,
output reg [7:0] port_out_11,
output reg [7:0] port_out_12,
output reg [7:0] port_out_13,
output reg [7:0] port_out_14,
output reg [7:0] port_out_15,
output reg [7:0] data_out,
input wire [7:0] address,
input wire [7:0] data_in,
input wire [7:0] port_in_00,
input wire [7:0] port_in_01,
input wire [7:0] port_in_02,
input wire [7:0] port_in_03,
input wire [7:0] port_in_04,
input wire [7:0] port_in_05,
input wire [7:0] port_in_06,
input wire [7:0] port_in_07,
input wire [7:0] port_in_08,
input wire [7:0] port_in_09,
input wire [7:0] port_in_10,
input wire [7:0] port_in_11,
input wire [7:0] port_in_12,
input wire [7:0] port_in_13,
input wire [7:0] port_in_14,
input wire [7:0] port_in_15,
input wire write, clk, reset);

wire [7:0] rom_data_out, rw_data_out;

always @ (address, rom_data_out, rw_data_out, port_in_00, port_in_01, port_in_02, port_in_03, port_in_04, port_in_05, port_in_06, port_in_07, port_in_08, port_in_09, port_in_10, port_in_11, port_in_12, port_in_13, port_in_14, port_in_15)

begin: Multiplexing_to_Memory_Data_Bus

  if (address == 8'hF0) 
			data_out = port_in_00;
  else if (address == 8'hF1) 
			data_out = port_in_01; 
  else if (address == 8'hF2) 
			data_out = port_in_02; 
  else if (address == 8'hF3) 
			data_out = port_in_03; 
  else if (address == 8'hF4) 
			data_out = port_in_04; 
  else if (address == 8'hF5) 
			data_out = port_in_05; 
  else if (address == 8'hF6) 
			data_out = port_in_06; 
  else if (address == 8'hF7) 
			data_out = port_in_07; 
  else if (address == 8'hF8) 
			data_out = port_in_08; 
  else if (address == 8'hF9) 
			data_out = port_in_09; 
  else if (address == 8'hFA) 
			data_out = port_in_10; 
  else if (address == 8'hFB) 
			data_out = port_in_11; 
  else if (address == 8'hFC) 
			data_out = port_in_12; 
  else if (address == 8'hFD) 
			data_out = port_in_13; 
  else if (address == 8'hFE) 
			data_out = port_in_14; 
  else if (address == 8'hFF) 
			data_out = port_in_15;
  else if ((address >= 0) && (address <= 127)) 
			data_out = rom_data_out;
  else if ((address >= 128) && (address <= 223)) 
			data_out = rw_data_out;
      
end

// Complement the module

rom_128x8_sync rom_inst (.address(address), .data_out(rom_data_out), .clk(clk));

rw_96x8_sync rw_inst (.address(address), .data_in(data_in), .WE(write), .clk(clk), .data_out(rw_data_out));

port_out8_sync port_out_inst (.address(address), .data_in(data_in), .write(write), .clk(clk), .reset(reset), .port_out_00(port_out_00), .port_out_01(port_out_01), .port_out_02(port_out_02), .port_out_03(port_out_03), .port_out_04(port_out_04), .port_out_05(port_out_05), .port_out_06(port_out_06), .port_out_07(port_out_07), .port_out_08(port_out_08), .port_out_09(port_out_09), .port_out_10(port_out_10), .port_out_11(port_out_11), .port_out_12(port_out_12), .port_out_13(port_out_13), .port_out_14(port_out_14), .port_out_15(port_out_15));

endmodule

// RW

module rw_96x8_sync
	(output reg [7:0] data_out,
	 input wire [7:0] address,
	 input wire       WE,
	 input wire [7:0] data_in,
	 input wire       clk);
	 
	 reg[7:0] RW[128:223];
	 reg EN;
	 
	 always @ (address) 
	 	begin
		if ( (address >= 128) && (address <= 223) ) 
			EN = 1'b1;
		else
			EN = 1'b0;
		end
	 
	 always @ (posedge clk)
	 	begin
	 		if (WE && EN)
	 			RW[address] = data_in;
	 		else if (!WE && EN)
	 			data_out = RW[address];
	 	end
	 		
endmodule

// ROM

module rom_128x8_sync
	(output reg [7:0] data_out,
	 input wire [7:0] address,
	 input wire clk);
	 
	 reg[7:0] ROM[0:127];
	 reg EN;
	 
	 // Mnemonics of Instruction Set
	 // Feel free to add other
	 
	 // Loads and Stores
	 parameter LDA_IMM = 8'h86; // Load Register A (Immediate Addressing)
	 parameter LDA_DIR = 8'h87; // Load Register A from memory (RAM or IO) (Direct Addressing)
	 parameter LDB_IMM = 8'h88; // Load Register B (Immediate Addressing)
	 parameter LDB_DIR = 8'h89; // Load Register B from memory (RAM or IO) (Direct Addressing)
	 parameter STA_DIR = 8'h96; // Store Register A to memory (RAM or IO)
	 parameter STB_DIR = 8'h97; // Store Register B to memory (RAM or IO)
	 
	 // Data Manipulations
	 parameter ADD_AB  = 8'h42; // A <= A + B
	 parameter SUB_AB  = 8'h43; // A <= A - B
	 parameter AND_AB  = 8'h44; // A <= A & B
	 parameter OR_AB   = 8'h45; // A <= A | B
	 parameter INCA    = 8'h46; // A <= A + 1
	 parameter INCB    = 8'h47; // B <= B + 1
	 parameter DECA	   = 8'h48; // A <= A - 1
	 parameter DECB    = 8'h49; // B <= B - 1
	 parameter XOR_AB  = 8'h4A; // A <= A ^ B
	 parameter NOTA	   = 8'h4B; // A <= ~A
	 parameter NOTB    = 8'h4C; // B <= ~B
	 
	 // Branches
	 parameter BRA     = 8'h20; // Branch Always    to (ROM) Address
	 parameter BMI     = 8'h21; // Branch if N == 1 to (ROM) Address
	 parameter BPL     = 8'h22; // Branch if N == 0 to (ROM) Address
	 parameter BEQ     = 8'h23; // Branch if Z == 1 to (ROM) Address
	 parameter BNE	   = 8'h24; // Branch if Z == 0 to (ROM) Address
	 parameter BVS	   = 8'h25; // Branch if V == 1 to (ROM) Address 
	 parameter BVC     = 8'h26; // Branch if V == 0 to (ROM) Address
	 parameter BCS     = 8'h27; // Branch if C == 1 to (ROM) Address
	 parameter BCC     = 8'h28; // Branch if C == 0 to (ROM) Address
	 
	 initial
	 	begin					// You need to load your own example
	 		ROM[0] = LDA_IMM; 	
	 		ROM[1] = 8'hAA;		// Data
	 		ROM[2] = STA_DIR;		
	 		ROM[3] = 8'hE0;		// Address (Output Port 0)
	 		ROM[4] = BRA;		
	 		ROM[5] = 8'h00;		// Address (ROM)
	 	end
	 
	 always @ (address) 
	 	begin
		if ( (address >= 0) && (address <= 127) ) 
			EN = 1'b1;
		else
			EN = 1'b0;
		end
	 	
	 always @ (posedge clk)
	 	if (EN)
		 	data_out = ROM[address];
	 		
endmodule

// PORT OUT

module port_out8_sync
	(output reg [7:0] port_out_00,
	 output reg [7:0] port_out_01,
	 output reg [7:0] port_out_02,
	 output reg [7:0] port_out_03,
	 output reg [7:0] port_out_04,
	 output reg [7:0] port_out_05,
	 output reg [7:0] port_out_06,
	 output reg [7:0] port_out_07,
	 output reg [7:0] port_out_08,
	 output reg [7:0] port_out_09,
	 output reg [7:0] port_out_10,
	 output reg [7:0] port_out_11,
	 output reg [7:0] port_out_12,
	 output reg [7:0] port_out_13,
	 output reg [7:0] port_out_14,
	 output reg [7:0] port_out_15,
	 input wire [7:0] address,
	 input wire [7:0] data_in,
	 input wire write, clk, reset);
	 
	 // port_out_00 (address E0)
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_00 <= 8'h00; 
			else if ((address == 8'hE0) && (write)) 
				port_out_00 <= data_in;
		end
				
	 // port_out_01 (address E2)
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_01 <= 8'h00; 
			else if ((address == 8'hE1) && (write))
				port_out_01 <= data_in;
		end
		
	 // port_out_02 (address E2)
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_02 <= 8'h00; 
			else if ((address == 8'hE2) && (write)) 
				port_out_02 <= data_in;
		end	
		
	 // port_out_03 (address E3)
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_03 <= 8'h00; 
			else if ((address == 8'hE3) && (write)) 
				port_out_03 <= data_in;
		end	
		
	 // port_out_04 (address E4)
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_04 <= 8'h00; 
			else if ((address == 8'hE4) && (write)) 
				port_out_04 <= data_in;
		end	
	 	
	 // port_out_05 (address E5)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_05 <= 8'h00; 
			else if ((address == 8'hE5) && (write)) 
				port_out_05 <= data_in;
		end
		
	 // port_out_06 (address E6)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_06 <= 8'h00; 
			else if ((address == 8'hE6) && (write)) 
				port_out_06 <= data_in;
		end	
		
	 // port_out_07 (address E7)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_07 <= 8'h00; 
			else if ((address == 8'hE7) && (write)) 
				port_out_07 <= data_in;
		end	
		
	 // port_out_08 (address E8)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_08 <= 8'h00; 
			else if ((address == 8'hE8) && (write)) 
				port_out_08 <= data_in;
		end	
		
	 // port_out_09 (address E9)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_09 <= 8'h00; 
			else if ((address == 8'hE9) && (write)) 
				port_out_09 <= data_in;
		end	
		
	 // port_out_10 (address EA)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_10 <= 8'h00; 
			else if ((address == 8'hEA) && (write)) 
				port_out_10 <= data_in;
		end	
		
	 // port_out_11 (address EB)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_11 <= 8'h00; 
			else if ((address == 8'hEB) && (write)) 
				port_out_11 <= data_in;
		end	
		
	 // port_out_12 (address EC)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_12 <= 8'h00; 
			else if ((address == 8'hEC) && (write)) 
				port_out_12 <= data_in;
		end	
		
	 // port_out_13 (address ED)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_13 <= 8'h00; 
			else if ((address == 8'hED) && (write)) 
				port_out_13 <= data_in;
		end
		
	 // port_out_14 (address EE)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_14 <= 8'h00; 
			else if ((address == 8'hEE) && (write)) 
				port_out_14 <= data_in;
		end	
		
	 // port_out_15 (address EF)		
	 always @ (posedge clk or negedge reset)
		begin
			if (!reset)
				port_out_15 <= 8'h00; 
			else if ((address == 8'hEF) && (write)) 
				port_out_15 <= data_in;
		end					
endmodule