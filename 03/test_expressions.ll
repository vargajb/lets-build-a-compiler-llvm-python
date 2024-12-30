define i32 @main(i32 %argc, i8** %argv) {
    %ssa_0 = add i32 3, 0          ; %ssa_0 = 3
    %A1 = alloca i32               ; int A1
    store i32 %ssa_0, i32* %A1     ; A1 = %ssa_0
    %ssa_1 = load i32, i32* %A1
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds([9 x i8], [9 x i8]* @str_0, i32 0, i32 0), i32 %ssa_1)
    %ssa_2 = add i32 7, 0          ; %ssa_2 = 7
    %stack_0 = add i32 %ssa_2, 0
    %ssa_3 = load i32, i32* %A1    ; %ssa_3 = A1
    %stack_1 = add i32 %ssa_3, 0   ; %stack_1 = %ssa_3
    %ssa_4 = add i32 5, 0          ; %ssa_4 = 5
    %ssa_5 = mul i32 %stack_1, %ssa_4
    %ssa_6 = add i32 %stack_0, %ssa_5
    %A2 = alloca i32               ; int A2
    store i32 %ssa_6, i32* %A2     ; A2 = %ssa_6
    %ssa_7 = load i32, i32* %A2
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds([9 x i8], [9 x i8]* @str_1, i32 0, i32 0), i32 %ssa_7)
    %ssa_8 = load i32, i32* %A2    ; %ssa_8 = A2
    %stack_2 = add i32 %ssa_8, 0   ; %stack_2 = %ssa_8
    %ssa_9 = load i32, i32* %A1    ; %ssa_9 = A1
    %ssa_10 = call i32 @floor_div(i32 %stack_2, i32 %ssa_9)
    %BB = alloca i32               ; int BB
    store i32 %ssa_10, i32* %BB    ; BB = %ssa_10
    %ssa_11 = load i32, i32* %BB
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds([9 x i8], [9 x i8]* @str_2, i32 0, i32 0), i32 %ssa_11)
    %ssa_12 = load i32, i32* %A2   ; %ssa_12 = A2
    %stack_3 = add i32 %ssa_12, 0  ; %stack_3 = %ssa_12
    %ssa_13 = add i32 0, 0         ; %ssa_13 = 0
    %stack_4 = add i32 %ssa_13, 0
    %ssa_14 = load i32, i32* %A1   ; %ssa_14 = A1
    %ssa_15 = sub i32 %stack_4, %ssa_14
    %ssa_16 = call i32 @floor_div(i32 %stack_3, i32 %ssa_15)
    %BB2 = alloca i32              ; int BB2
    store i32 %ssa_16, i32* %BB2   ; BB2 = %ssa_16
    %ssa_17 = load i32, i32* %BB2
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds([10 x i8], [10 x i8]* @str_3, i32 0, i32 0), i32 %ssa_17)
    %ssa_18 = load i32, i32* %BB   ; %ssa_18 = BB
    %stack_5 = add i32 %ssa_18, 0
    %ssa_19 = load i32, i32* %BB2  ; %ssa_19 = BB2
    %ssa_20 = sub i32 %stack_5, %ssa_19
    %BB3 = alloca i32              ; int BB3
    store i32 %ssa_20, i32* %BB3   ; BB3 = %ssa_20
    %ssa_21 = load i32, i32* %BB3
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds([10 x i8], [10 x i8]* @str_4, i32 0, i32 0), i32 %ssa_21)
   ret i32 0
}

declare i32 @printf(i8*, ...)

; Function for integer division that truncates to zero. (default in many
; programming languages like Java, LLVM, C, etc.)
define i32 @truncating_div(i32 %op1, i32 %op2) alwaysinline {
entry:
  %result = sdiv i32 %op1, %op2
  ret i32 %result
}

; Function for integer division that rounds to negative infinity.
; Compatible with Python's // operator
; Implements Java's Math.floorDiv() logic:
;    public static int floorDiv(int x, int y) {
;        int r = x / y;
;        // if the signs are different and modulo not zero, round down
;        if ((x ^ y) < 0 && (r * y != x)) {
;            r--;
;        }
;        return r;
;    }
define i32 @floor_div(i32 %x, i32 %y) alwaysinline {
    %q = sdiv i32 %x, %y
    %q_mul_y = mul i32 %q, %y
    %remainder = sub i32 %x, %q_mul_y
    %xor_result = xor i32 %x, %y
    %sign_diff = icmp slt i32 %xor_result, 0
    %non_zero_remainder = icmp ne i32 %remainder, 0
    %round_down_condition = and i1 %sign_diff, %non_zero_remainder
    %q_minus_1 = sub i32 %q, 1
    %final_result = select i1 %round_down_condition, i32 %q_minus_1, i32 %q
    ret i32 %final_result
}

@str_0 = private unnamed_addr constant [9 x i8] c"A1 = %d\0a\00", align 1
@str_1 = private unnamed_addr constant [9 x i8] c"A2 = %d\0a\00", align 1
@str_2 = private unnamed_addr constant [9 x i8] c"BB = %d\0a\00", align 1
@str_3 = private unnamed_addr constant [10 x i8] c"BB2 = %d\0a\00", align 1
@str_4 = private unnamed_addr constant [10 x i8] c"BB3 = %d\0a\00", align 1

