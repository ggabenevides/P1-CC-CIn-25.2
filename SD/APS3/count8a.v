`include "components.v"
`include "lib2.v"

module count8a(
    output wire [7:0] CNT, // saída
    input wire clk, res, EN, load, // entradas de controle
    input wire [7:0] CNT_In // entrada de dados
);

wire [7:0] CNTn, CNT_INn, saidamux_res, saidamux_preset, saidamux_D; //fios intermediarios


// logica de controle
not8b not1 (CNT_INn, CNT_In); //

MUX2to1_8b mux1 (saidamux_res, {8{res}}, CNT_In, load); // Reset
MUX2to1_8b mux2 (saidamux_preset, {8'b1}, CNT_INn, load); // Preset
MUX2to1_8b mux3 (saidamux_D, CNT, CNTn, EN); // Dados (D) caso enable esteja habilitado

// Flip-Flop 0 recebe o clock externo e Enable

dflipflop FF0 (.Q(CNT[0]), .Qn(CNTn[0]), .Clock(clk), .Reset(saidamux_res[0]), .Preset(saidamux_preset[0]), .D(saidamux_D[0]));

// Demais Flip-Flops recebem o clock da saída negada do anterior

dflipflop FF1 (.Q(CNT[1]), .Qn(CNTn[1]), .Clock(CNTn[0]), .Reset(saidamux_res[1]), .Preset(saidamux_preset[1]), .D(saidamux_D[1]));
dflipflop FF2 (.Q(CNT[2]), .Qn(CNTn[2]), .Clock(CNTn[1]), .Reset(saidamux_res[2]), .Preset(saidamux_preset[2]), .D(saidamux_D[2]));
dflipflop FF3 (.Q(CNT[3]), .Qn(CNTn[3]), .Clock(CNTn[2]), .Reset(saidamux_res[3]), .Preset(saidamux_preset[3]), .D(saidamux_D[3]));
dflipflop FF4 (.Q(CNT[4]), .Qn(CNTn[4]), .Clock(CNTn[3]), .Reset(saidamux_res[4]), .Preset(saidamux_preset[4]), .D(saidamux_D[4]));
dflipflop FF5 (.Q(CNT[5]), .Qn(CNTn[5]), .Clock(CNTn[4]), .Reset(saidamux_res[5]), .Preset(saidamux_preset[5]), .D(saidamux_D[5]));
dflipflop FF6 (.Q(CNT[6]), .Qn(CNTn[6]), .Clock(CNTn[5]), .Reset(saidamux_res[6]), .Preset(saidamux_preset[6]), .D(saidamux_D[6]));
dflipflop FF7 (.Q(CNT[7]), .Qn(CNTn[7]), .Clock(CNTn[6]), .Reset(saidamux_res[7]), .Preset(saidamux_preset[7]), .D(saidamux_D[7]));

endmodule