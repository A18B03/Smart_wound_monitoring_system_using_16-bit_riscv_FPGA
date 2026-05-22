module control_unit (
    input        clk,
    input        rst,
    input [15:0] instr,

    output reg   pc_en,
    output reg   fetch,
    output reg   decode
);

    // State encoding
    localparam FETCH  = 2'b00;
    localparam DECODE = 2'b01;

    reg [1:0] state, next_state;

    // State register
    always @(posedge clk) begin
        if (rst)
            state <= FETCH;
        else
            state <= next_state;
    end

    // Next-state logic
    always @(*) begin
        case (state)
            FETCH:  next_state = DECODE;
            DECODE: next_state = FETCH;
            default: next_state = FETCH;
        endcase
    end

    // Output logic
    always @(*) begin
        // defaults
        pc_en  = 0;
        fetch  = 0;
        decode = 0;

        case (state)
            FETCH: begin
                pc_en = 1;   // allow PC to increment
                fetch = 1;   // instruction fetch phase
            end
            DECODE: begin
                decode = 1;  // instruction decode phase
            end
        endcase
    end

endmodule
