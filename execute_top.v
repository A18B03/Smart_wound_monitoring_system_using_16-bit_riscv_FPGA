module execute_top (
    input clk,
    input [15:0] instr,
    input wb_we,
    input [15:0] wb_data,
    output [15:0] alu_y,
    output zero,
    output [15:0] rd2
);

    wire [3:0] opcode = instr[15:12];
    wire [2:0] ra1 = instr[8:6];
    wire [2:0] ra2 = instr[5:3];
    wire [2:0] wa  = instr[11:9];

    // ALU control
    reg [2:0] alu_op;

    always @(*) begin
        case (opcode)
            4'b0001: alu_op = 3'b000; // ADD
            4'b0010: alu_op = 3'b001; // SUB
            4'b0011: alu_op = 3'b010; // AND
            4'b0100: alu_op = 3'b011; // OR
            4'b0110: alu_op = 3'b000; // LOAD
            default: alu_op = 3'b000;
        endcase
    end

    wire [15:0] rd1;

    // REGISTER FILE
    regfile rf0 (
        .clk(clk),
        .we(wb_we),
        .ra1(ra1),
        .ra2(ra2),
        .wa(wa),
        .wd(wb_data),
        .rd1(rd1),
        .rd2(rd2)
    );

    // FIXED ALU INPUTS
    wire [15:0] alu_in_a;
    wire [15:0] alu_in_b;

    assign alu_in_a = rd1;
    assign alu_in_b = (opcode == 4'b0110) ? wb_data : rd2;

    // ALU
    alu alu0 (
        .a(alu_in_a),
        .b(alu_in_b),
        .alu_op(alu_op),
        .y(alu_y),
        .zero(zero)
    );

endmodule