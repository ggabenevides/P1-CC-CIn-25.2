`include "components.v"
`include "lib2.v"

module semaforo (
    output wire GRN, YLW, RED,
    input wire car, timeout, clk, res
);

    // fios intermediarios
    wire q0, q0n, q1, q1n, d0, d1, and_temp, timeout_n, saida_and;

    // logica combinacional de entrada
    and and1 (and_temp, car, q1n);
    and and2 (d0, and_temp, q0n);
    not not1 (timeout_n, timeout);
    and and3 (saida_and, timeout_n, q1n);
    or or1 (d1, saida_and, q0n);

    // logica sequencial 
    dflipflop dff0 (.Q(q0), .Qn(q0n), .Clock(clk),.Reset(res),.D(d0)); 
    dflipflop dff1 (.Q(q1), .Qn(q1n), .Clock(clk),.Reset(res),.D(d1)); 

    // logica combinacional de saida
    nor nor1 (GRN, q0, q1);
    and and4 (YLW, q0n, q1n);
    and and5 (RED, q1, q0n);

endmodule