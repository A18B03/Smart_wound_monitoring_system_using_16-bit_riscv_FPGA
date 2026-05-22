module dmem (
    input         clk,
    input         we,
    input  [7:0]  addr,
    input  [15:0] wd,
    output [15:0] rd
);

    reg [15:0] mem [0:255];

    assign rd = mem[addr];

    always @(posedge clk) begin
        if (we)
            mem[addr] <= wd;
    end

endmodule
