module control_unit 
    (output reg IR_Load, 
     output reg MAR_Load, 
     output reg PC_Load, PC_Inc, 
     output reg A_Load, B_Load,
     output reg CCR_Load,
     output reg [2:0] ALU_Sel,
     output reg [1:0] Bus1_Sel, Bus2_Sel,
     output reg write, 
     input wire [7:0] IR, 
     input wire [3:0] CCR_Result,
     input wire Clk, Reset);
             
    reg [7:0] current_state, next_state;

    // parâmetros de estado
    parameter S0_FETCH = 8'd0,  //opcode de estados de busca (fetch)
              S1_FETCH = 8'd1,
              S2_FETCH = 8'd2,
              
              S3_DECODE = 8'd3, //opcode de estado de decodificação (decode)
              
              S4_LDA_IMM = 8'd4, //LDA_IMM = load A immediate ; estados de execução
              S5_LDA_IMM = 8'd5,
              S6_LDA_IMM = 8'd6,
              
              S4_LDA_DIR = 8'd7, //LDA_DIR = load A direct ; estados de execução
              S5_LDA_DIR = 8'd8,
              S6_LDA_DIR = 8'd9,
              S7_LDA_DIR = 8'd10,
              S8_LDA_DIR = 8'd11,

              S4_STA_DIR = 8'd12, // store A direct ; estados de execução
              S5_STA_DIR = 8'd13,
              S6_STA_DIR = 8'd14,
              
              S4_ADD_IMM = 8'd15, // add immediate to A ; estados de execução
              S5_ADD_IMM = 8'd16,
              S6_ADD_IMM = 8'd17;
              
    // definições de opcode 
    parameter [7:0] LDA_IMM = 8'h01; // load A immediate
    parameter [7:0] LDA_DIR = 8'h02; // load A direct
    parameter [7:0] STA_DIR = 8'h12; // store A direct
    parameter [7:0] ADD_IMM = 8'h21; // add immediate to A
              
    // códigos de seleção de bus
    // Bus1_Sel: 00 = PC, 01 = A, 10 = B 
    parameter [1:0] SEL_PC = 2'b00;
    parameter [1:0] SEL_A  = 2'b01;
    parameter [1:0] SEL_B  = 2'b10;
    
    // Bus2_Sel: 00 = ALU, 01 = Bus1, 10 = from_memory 
    parameter [1:0] SEL_ALU = 2'b00;
    parameter [1:0] SEL_BUS1 = 2'b01;
    parameter [1:0] SEL_MEM  = 2'b10;

    // códigos de seleção da ULA
    // ALU_Sel: 000 = ADD, 001 = SUB, 010 = PASS_B 
    parameter [2:0] ALU_ADD = 3'b000;
    parameter [2:0] ALU_PASS_B = 3'b010; // dados de B para o bus/A
    parameter [2:0] ALU_INC = 3'b111; // PC_Inc (PC=PC+1)

    initial
        begin
            current_state = S0_FETCH;
            next_state = S0_FETCH;
            IR_Load = 0;
            MAR_Load = 0;
            PC_Load = 0;
            PC_Inc = 0;
            A_Load = 0;
            B_Load = 0;
            CCR_Load = 0;
            ALU_Sel = ALU_PASS_B; 
            Bus1_Sel = SEL_PC; 
            Bus2_Sel = SEL_BUS1; 
            write = 0;
        end 

    // bloco de memória de estado
    always @ (posedge Clk or negedge Reset)
        begin: STATE_MEMORY
            if (!Reset)
                current_state <= S0_FETCH;
            else
                current_state <= next_state;
        end

    // bloco de lógica do próximo estado
    always @ (current_state, IR)
        begin: NEXT_STATE_LOGIC
            next_state = S0_FETCH; // transição padrão
            case (current_state)
                S0_FETCH : next_state = S1_FETCH;
                S1_FETCH : next_state = S2_FETCH;
                S2_FETCH : next_state = S3_DECODE;
                
                S3_DECODE : 
                    begin 
                        case (IR)
                            LDA_IMM: next_state = S4_LDA_IMM;
                            LDA_DIR: next_state = S4_LDA_DIR;
                            STA_DIR: next_state = S4_STA_DIR;
                            ADD_IMM: next_state = S4_ADD_IMM;
                            default: next_state = S0_FETCH; 
                        endcase
                    end
            
                // sequência LDA_IMM 
                S4_LDA_IMM : next_state = S5_LDA_IMM; // operando vai para o MAR
                S5_LDA_IMM : next_state = S6_LDA_IMM; // carregar A
                S6_LDA_IMM : next_state = S0_FETCH;   // fim
                                     
                // sequência LDA_DIR
                S4_LDA_DIR : next_state = S5_LDA_DIR; // LSB do endereço vai para o MAR
                S5_LDA_DIR : next_state = S6_LDA_DIR; // incrementa PC
                S6_LDA_DIR : next_state = S7_LDA_DIR; // MSB do endereço vai para o MAR (upper bits of MAR)
                S7_LDA_DIR : next_state = S8_LDA_DIR; // busca de dados para B
                S8_LDA_DIR : next_state = S0_FETCH;   // carregar A e finalizar

                // sequência STA_DIR 
                S4_STA_DIR : next_state = S5_STA_DIR; // LSB do endereço vai para o MAR
                S5_STA_DIR : next_state = S6_STA_DIR; // incrementa PC, MSB para MAR
                S6_STA_DIR : next_state = S0_FETCH;   // escrever A em endereço de memória

                // sequência ADD_IMM
                S4_ADD_IMM : next_state = S5_ADD_IMM; // operando vai para MAR
                S5_ADD_IMM : next_state = S6_ADD_IMM; // carregar B
                S6_ADD_IMM : next_state = S0_FETCH;   // ADD A+B -> A
                
                default : next_state = S0_FETCH;
            endcase
        end

    // bloco de lógica do output
    always @ (current_state)
        begin: OUTPUT_LOGIC
            // valores padrão para sinais de controle
            IR_Load = 0;
            MAR_Load = 0;
            PC_Load = 0;
            PC_Inc = 0;
            A_Load = 0;
            B_Load = 0;
            CCR_Load = 0;
            write = 0;
            Bus1_Sel = SEL_PC;     
            Bus2_Sel = SEL_BUS1;    
            ALU_Sel = ALU_PASS_B;   

            case (current_state)
                
                // FETCH CYCLE
                S0_FETCH : 
                    begin // MAR <- PC
                        MAR_Load = 1;
                        Bus1_Sel = SEL_PC; 
                        Bus2_Sel = SEL_BUS1; 
                    end
                    
                S1_FETCH : 
                    begin // PC <- PC + 1
                        PC_Inc = 1;
                        Bus1_Sel = SEL_PC; // PC input para ALU
                        Bus2_Sel = SEL_BUS1; 
                        ALU_Sel = ALU_INC; // ALU faz +1
                    end
                    
                S2_FETCH : 
                    begin // carregar registro de instruções (IR <- M[MAR])
                        IR_Load = 1;
                        Bus1_Sel = SEL_PC; // don't care
                        Bus2_Sel = SEL_MEM; // M[MAR] para Main Bus
                    end
                
                S3_DECODE : 
                    begin // decode: No operation needed, control unit transitions
                    end

                // LDA_IMM 
                // instrução: [OPCODE] [DATA]
                S4_LDA_IMM : 
                    begin // Get operand address/data LSB into MAR (MAR <- PC)
                        // Assuming 1-byte immediate data. M[PC] is the data.
                        MAR_Load = 1;
                        Bus1_Sel = SEL_PC; 
                        Bus2_Sel = SEL_BUS1; 
                    end
                S5_LDA_IMM : 
                    begin // Increment PC (PC <- PC + 1)
                        PC_Inc = 1;
                        Bus1_Sel = SEL_PC; 
                        Bus2_Sel = SEL_BUS1; 
                        ALU_Sel = ALU_INC; 
                    end
                S6_LDA_IMM : 
                    begin // Load A (A <- M[MAR])
                        A_Load = 1;
                        Bus2_Sel = SEL_MEM; // M[MAR] to Main Bus
                    end

                // --- LDA_DIR (Load A Direct) ---
                // Instruction: [OPCODE] [ADDR_LSB] [ADDR_MSB] (2-byte address)
                S4_LDA_DIR : 
                    begin // Get Address LSB into MAR (MAR <- PC)
                        MAR_Load = 1; 
                        Bus1_Sel = SEL_PC; 
                        Bus2_Sel = SEL_BUS1; 
                    end
                S5_LDA_DIR : 
                    begin // Increment PC and put LSB of address into MAR LSB
                        PC_Inc = 1;
                        Bus1_Sel = SEL_PC; 
                        Bus2_Sel = SEL_BUS1; 
                        ALU_Sel = ALU_INC; 
                    end
                S6_LDA_DIR : 
                    begin // Get Address MSB from memory into MAR MSB
                        MAR_Load = 1; // Load MAR (MSB part)
                        Bus2_Sel = SEL_MEM; // M[MAR] (which is ADDR_LSB) to MAR (upper bits)
                    end
                S7_LDA_DIR : 
                    begin // MAR is now loaded with the full data address. Data fetch to B
                        B_Load = 1;
                        Bus2_Sel = SEL_MEM; // M[MAR] (Data) to B
                    end
                S8_LDA_DIR : 
                    begin // Load A from B (A <- B)
                        A_Load = 1;
                        Bus1_Sel = SEL_B;
                        Bus2_Sel = SEL_BUS1; 
                    end

                // --- STA_DIR (Store A Direct) ---
                // Instruction: [OPCODE] [ADDR_LSB] [ADDR_MSB]
                S4_STA_DIR : 
                    begin // Get Address LSB into MAR (MAR <- PC)
                        MAR_Load = 1; 
                        Bus1_Sel = SEL_PC; 
                        Bus2_Sel = SEL_BUS1; 
                    end
                S5_STA_DIR : 
                    begin // Increment PC and get Address MSB from memory into MAR MSB
                        PC_Inc = 1;
                        MAR_Load = 1; 
                        Bus2_Sel = SEL_MEM; 
                        ALU_Sel = ALU_INC;
                    end
                S6_STA_DIR : 
                    begin // Write A to memory at M[MAR] (M[MAR] <- A)
                        write = 1;
                        Bus1_Sel = SEL_A; // A to memory data bus
                        Bus2_Sel = SEL_BUS1; 
                    end

                // --- ADD_IMM (Add Immediate) ---
                // Instruction: [OPCODE] [DATA]
                S4_ADD_IMM : 
                    begin // Get operand address/data LSB into MAR (MAR <- PC)
                        MAR_Load = 1;
                        Bus1_Sel = SEL_PC; 
                        Bus2_Sel = SEL_BUS1; 
                    end
                S5_ADD_IMM : 
                    begin // Increment PC and Load B (B <- M[MAR])
                        PC_Inc = 1; // Increment PC
                        B_Load = 1; // Load B
                        Bus2_Sel = SEL_MEM; // M[MAR] to B
                        ALU_Sel = ALU_INC; 
                    end
                S6_ADD_IMM : 
                    begin // ADD A+B -> A (A <- A + B)
                        A_Load = 1;
                        CCR_Load = 1; // Update Condition Codes
                        Bus1_Sel = SEL_A; // A to ALU input
                        ALU_Sel = ALU_ADD; // A+B operation
                        Bus2_Sel = SEL_ALU; // ALU result to A register
                    end
                
                default : 
                    begin // Catch-all or error state, transition to fetch
                    end
            endcase
        end
        
endmodule