.text
.global CountCommon
.type  CountCommon, "function"

CountCommon: mov x7,#0

ciclo1: cmp x0,#0
        b.eq fim
        ldr w9,[x1]
        add x1,x1,#4
        sub x0,x0,#1
        mov x11,x2
        mov x12,x3

ciclo2: cmp x11,#0
        b.eq ciclo1
        ldr w10,[x12]
        sub x11,x11,#1
        add x12,x12,#4
        cmp w9,w10
        b.ne ciclo2
        add x7,x7,#1
        b ciclo1

fim: mov x0,x7
     ret
