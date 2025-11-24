`include "components.v"
`include "lib2.v"

module reg8a (
    input wire EN, //habilita o circuito
    input wire [7:0] Reg_In, //entrada
    input wire res, // reset assíncrono
    input wire clk, //relógio
    output wire [7:0] Reg_Out // saída
    );

    wire [7:0] saida_mux;

    // o multiplexador 2 para 1 serve para decidir, de acordo com a entrada de controle EN, se o registrador vai manter o valor armazenado (EN = 0) ou carregar uma nova entrada (EN = 1)
    MUX2to1_8b mux(saida_mux, Reg_Out, Reg_In, EN); 
    
    // esse conjunto de fliflops D armazena 8 bits - cada FF armazena 1 bit da saida do MUX, alem disso contam com o sinal de reset (caso zere o conteudo) e usa Clk com sinal de borda
    dflipflop dff0 (.Q(Reg_Out[0]), .Clock(clk),.Reset(res),.D(saida_mux[0])); 
    dflipflop dff1 (.Q(Reg_Out[1]), .Clock(clk),.Reset(res),.D(saida_mux[1]));
    dflipflop dff2 (.Q(Reg_Out[2]), .Clock(clk),.Reset(res),.D(saida_mux[2]));
    dflipflop dff3 (.Q(Reg_Out[3]), .Clock(clk),.Reset(res),.D(saida_mux[3]));
    dflipflop dff4 (.Q(Reg_Out[4]), .Clock(clk),.Reset(res),.D(saida_mux[4]));
    dflipflop dff5 (.Q(Reg_Out[5]), .Clock(clk),.Reset(res),.D(saida_mux[5]));
    dflipflop dff6 (.Q(Reg_Out[6]), .Clock(clk),.Reset(res),.D(saida_mux[6]));
    dflipflop dff7 (.Q(Reg_Out[7]), .Clock(clk),.Reset(res),.D(saida_mux[7]));
endmodule