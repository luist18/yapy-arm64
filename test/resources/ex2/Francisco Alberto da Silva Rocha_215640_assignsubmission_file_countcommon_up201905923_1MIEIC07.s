.text
.global CountCommon
.type CountCommon, "function"

CountCommon:
	mov w4, #0 //contador
main_cicle:
	cbz w0, END
	ldr w5, [x1], #4
	sub w0, w0, #1
	mov w7, w2 // copia do tamanho do vetor B
	mov x8, x3 // copia do endereço de B
sub_cicle:
	cbz w7, main_cicle
	ldr w6, [x8], #4
	sub w7, w7, #1
	cmp w5, w6
	b.ne sub_cicle
	add w4, w4, #1
	b main_cicle
END:
	mov w0, w4
	ret
