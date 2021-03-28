.text
.global CountCommon
.type CountCommon, "function"
//w3 = copy of w2
//w2 = nº de elementos em seq B
//w1 = nº de elementos em seq A
CountCommon: mov w8, 0
             mov w3, w2
             mov x9, 0
             mov x10, 0
ciclo: cbz w1, fim
       cbz w2, reset
       ldr w4, [x1, x9]
       ldr w5, [x2, x10]
       cmp w4, w5
       b.eq add1

add1: add w8, w8, 1
      b s
s: add w10, w10, 4
   sub w2, w2, 1
   b ciclo

reset: mov w2, w3
       sub w1, w1, 1
       add x9, x9, 4
       b ciclo

fim: mov w0, w8
     RET
