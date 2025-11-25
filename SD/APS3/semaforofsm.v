module semaforo (
    output reg GRN, YLW, RED,
    input wire timeout, car, clk, res
);
    // Definindo estados
    parameter VERDE = 2'b00, AMARELO = 2'b01, VERMELHO = 2'b10; 
    reg [1:0] state, next_state;

    // Bloco de memória de estado
    always @ (posedge clk or negedge res) begin
        if (!res)
            state <= VERDE;
        else
            state <= next_state;
    end

    // Bloco de lógica do próximo estado
    always @ (*) begin
        case (state)
            VERDE: begin
                if (car)
                    next_state = AMARELO;
                else
                    next_state = VERDE;
            end
            AMARELO:
                next_state = VERMELHO;
            VERMELHO: begin
                if (timeout)
                    next_state = VERDE;
                else
                    next_state = VERMELHO;
            end
            default:
                next_state = VERDE;
        endcase
    end

    // Bloco de lógica do output
    always @ (posedge clk) begin
        GRN = 0;
        YLW = 0;
        RED = 0;

        case (state)
            VERDE: GRN <= 1;
            AMARELO: YLW <= 1;
            VERMELHO: RED <= 1;
        endcase
    end
    
endmodule