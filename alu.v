module alu (
    input  [15:0] a,
    input  [15:0] b,
    input  [2:0]  alu_op,
    output reg [15:0] y,
    output        zero
);

    always @(*) begin
        case (alu_op)
            3'b000: y = a + b;   // ADD
            3'b001: y = a - b;   // SUB
            3'b010: y = a & b;   // AND
            3'b011: y = a | b;   // OR
            default: y = 16'h0000;
        endcase
    end

    assign zero = (y == 16'h0000);

endmodule
