`timescale 1ns/1ps
`include "semaforofsm.v"

module semaforofsm_tb;

    reg clk;
    reg res;
    reg car;
    reg timeout;

    wire GRN;
    wire YLW;
    wire RED;

    // instanciando o teste
    semaforo DUT (
        .GRN(GRN),
        .YLW(YLW),
        .RED(RED),
        .timeout(timeout),
        .car(car),
        .clk(clk),
        .res(res)
    );

    parameter CLK_PERIOD = 10;
    initial begin
        clk = 0;
        forever #(CLK_PERIOD/2) clk = ~clk; // alterna o clock a cada 5ns
    end

    initial begin
        // Inicialização de Inputs
        res = 0;      // Reset Ativo Baixo
        car = 0;
        timeout = 0;
        
        $display("----------------------------------------------------------------------------------");
        $display("Tempo | Reset | Car | Timeout | Estado (GRN/YLW/RED)");
        $display("----------------------------------------------------------------------------------");

        // Reset Assíncrono (Dura 2 ciclos de clock)
        // O estado deve ir para VERDE
        #CLK_PERIOD;
        res = 1; // Libera o Reset
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Estado Inicial (VERDE)", $time, res, car, timeout, GRN, YLW, RED);


        // Estado VERDE (Espera)
        // Permanece em VERDE pois car=0
        #CLK_PERIOD;
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Permanece VERDE", $time, res, car, timeout, GRN, YLW, RED);


        // Transição: VERDE -> AMARELO
        // Ativa a detecção de carro (`car = 1`). A transição ocorre no próximo posedge clk
        car = 1;
        #CLK_PERIOD;
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Transiciona para AMARELO", $time, res, car, timeout, GRN, YLW, RED);
        car = 0; // Desativa a detecção de carro após a transição


        // Transição: AMARELO -> VERMELHO
        // A transição de AMARELO para VERMELHO é incondicional no código.
        #CLK_PERIOD;
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Transiciona para VERMELHO", $time, res, car, timeout, GRN, YLW, RED);


        // Estado VERMELHO (Espera)
        // Permanece em VERMELHO pois timeout=0
        #CLK_PERIOD;
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Permanece VERMELHO", $time, res, car, timeout, GRN, YLW, RED);
        
        #CLK_PERIOD;
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Permanece VERMELHO", $time, res, car, timeout, GRN, YLW, RED);


        // Transição: VERMELHO -> VERDE
        // Ativa o timeout (`timeout = 1`). A transição ocorre no próximo posedge clk.
        timeout = 1;
        #CLK_PERIOD;
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Transiciona para VERDE", $time, res, car, timeout, GRN, YLW, RED);
        timeout = 0; // Desativa o timeout


        // Loop de volta para VERDE (Espera)
        #CLK_PERIOD;
        $display("%4dns |   %b   |  %b  |    %b    | (%b / %b / %b) - Volta para VERDE", $time, res, car, timeout, GRN, YLW, RED);

        #CLK_PERIOD;
        $finish;
    end

endmodule