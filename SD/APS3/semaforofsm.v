module semaforofsm(
    output reg GRN, YLW, RED,
    input wire timeout, car, clk, res
);
    // Definindo estados
    parameter VERDE = 2'b00, AMARELO = 2'b01, VERMELHO = 2'b10; 
	 parameter TIMEOUT_amarelo = 50000000, TIMEOUT_vermelho = 750000000;
    reg [1:0] state, next_state;
	 reg [32:0] counter_red; // contador p o tempo de espera no estado VERMELHO (15s = 15*50milhoes)
	 reg [32:0] counter_yellow; // contador p o tempo de espera no estado AMARELO (1s = 50 milhoes)

    // Bloco de memória de estado
    always @ (posedge clk or negedge res) begin
        if (!res)
            state <= VERDE;
        else
            state <= next_state;
    end

    // Bloco de lógica do próximo estado
    always @ (posedge next_state) begin
        case (state)
            VERDE: begin
                if (car)
                    next_state = AMARELO;
                else
                    next_state = VERDE;
            end
            AMARELO: begin
					if (counter_yellow >= TIMEOUT_amarelo) begin
						next_state <= VERMELHO;
						counter_yellow <= 0;
						end
					else begin
						next_state <= AMARELO;
						counter_yellow <= counter_yellow + 1;
						end
				end
            VERMELHO: begin
                if (counter_red >= TIMEOUT_vermelho) begin
                    next_state <= VERDE;
						  counter_red <= 0;
						  end
                else begin
                    next_state <= VERMELHO;
						  counter_red <= counter_red + 1;
						  end
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
