`include "reg8a.v"

module count8a (
    output wire [7:0] CNT,                // Saída
    input wire        clk, res, EN, load, // Entradas de controle
    input wire  [7:0] CNT_In              // Entrada de dados
);

    // Incrementa o valor atual do registrador
    wire [7:0] inc_out;
    adder8b increment (inc_out, , CNT, 8'b0000_0001);

    // Passa o incremento da saída do registrador ou a entrada de dados do contador para a saída dependendo do valor do load
    wire [7:0] mux_out;
    MUX2to1_8b mux (mux_out, inc_out, CNT_In, load);

    // Registrador, recebendo a saída do multiplexador como entrada de dados
    reg8a register (EN, mux_out, res, clk, CNT);

endmodule