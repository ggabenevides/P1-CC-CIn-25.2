module count8fsm (
    output reg [7:0] CNT,
    input wire clk, res, EN, load,
    input wire [7:0] CNT_In
);

    reg [1:0] state, next_state;
    parameter IDLE = 2'b00, LOAD = 2'b01, COUNT = 2'b10;

    // Bloco de memória de estado
    always @ (posedge clk or negedge res) begin
        if (!res)
            state <= IDLE;
        else
            state <= next_state;
    end

    // Bloco de lógica do próximo estado
    always @ (*) begin
        case (state)
            IDLE: begin
                if (load)
                    next_state = LOAD;
                else if (EN)
                    next_state = COUNT;
                else
                    next_state = IDLE;
            end
            LOAD:
                next_state = COUNT;
            COUNT: begin
                if (load)
                    next_state = LOAD;
                else if (!EN)
                    next_state = IDLE;
                else
                    next_state = COUNT;
            end
            default:
                next_state = IDLE;
        endcase
    end

    // Bloco de lógica do output
    always @ (posedge clk or negedge res) begin
        if (!res)
            CNT <= 8'b0;
        else begin
            case(next_state)
                LOAD : CNT <= CNT_In;
                COUNT : CNT <= CNT + 1;
                default: CNT <= CNT;
            endcase
        end
    end
    
endmodule