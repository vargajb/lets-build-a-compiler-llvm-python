    MOVE #3, D0                    ; D0 = 3
    LEA A1(PC),A0                  ; A0 = addr(A1)
    MOVE D0,(A0)                   ; A1 = D0
    MOVE #7, D0                    ; D0 = 7
    MOVE D0,-(SP)                  ; push D0 onto stack
    MOVE A1(PC), D0                ; D0 = A1
    MOVE D0,-(SP)                  ; decrement SP; (SP)=D0 (push)
    MOVE #5, D0                    ; D0 = 5
    MULS (SP)+,D0                  ; D0 *= (SP); increment SP (pop)
    ADD (SP)+,D0                   ; D0 += (SP); increment SP (pop)
    LEA A2(PC),A0                  ; A0 = addr(A2)
    MOVE D0,(A0)                   ; A2 = D0
    MOVE A2(PC), D0                ; D0 = A2
    MOVE D0,-(SP)                  ; decrement SP; (SP)=D0 (push)
    MOVE A1(PC), D0                ; D0 = A1
    MOVE (SP)+,D1                  ; D1 = (SP); increment SP (pop)
    EXT.L D0                       ; Sign-extend the value in D0 to 32 bits
    DIVS D1,D0                     ; D0 /= D1 (signed division)
    LEA BB(PC),A0                  ; A0 = addr(BB)
    MOVE D0,(A0)                   ; BB = D0
    MOVE A2(PC), D0                ; D0 = A2
    MOVE D0,-(SP)                  ; decrement SP; (SP)=D0 (push)
    MOVE #0, D0                    ; D0 = 0
    MOVE D0,-(SP)                  ; push D0 onto stack
    MOVE A1(PC), D0                ; D0 = A1
    SUB (SP)+,D0                   ; D0 -= (SP); increment SP (pop)
    NEG D0                         ; D0 = -D0 (negate)
    MOVE (SP)+,D1                  ; D1 = (SP); increment SP (pop)
    EXT.L D0                       ; Sign-extend the value in D0 to 32 bits
    DIVS D1,D0                     ; D0 /= D1 (signed division)
    LEA BB2(PC),A0                 ; A0 = addr(BB2)
    MOVE D0,(A0)                   ; BB2 = D0
    MOVE BB(PC), D0                ; D0 = BB
    MOVE D0,-(SP)                  ; push D0 onto stack
    MOVE BB2(PC), D0               ; D0 = BB2
    SUB (SP)+,D0                   ; D0 -= (SP); increment SP (pop)
    NEG D0                         ; D0 = -D0 (negate)
    LEA BB3(PC),A0                 ; A0 = addr(BB3)
    MOVE D0,(A0)                   ; BB3 = D0
