.text
.global CountCommon
.type CountCommon, "function"

//w0 - Tamanho da seq_A
//x1 - Endereço-base da seq_A
//w2 - Tamanho da seq_B
//x3 - Endereço-base da seq_B

CountCommon:	mov w4, #0			//Inicia contador de números em comum das sequências
				mov w5,	w0			//Guarda o tamanho da seq_A
				mov x6, x1			//Guarda o endereço-base da seq_A

Cicle1:			cbz w2,	End			//Se o tamanho da seq_B for zero, já comparou todos os valores e termina
				mov w0, w5			//O tamanho da seq_A volta a ter o valor inicial
				mov x1, x6			//O endereço-base da seq_A volta a ter o valor inicial
				ldr w7, [x3]		//Carrega um elemento da seq_B
				add x3, x3, #4		//Passa ao próximo elemento da seq_B
				sub w2, w2, #1		//Decrementa um valor do tamanho da seq_B

Cicle2:			cbz w0, Cicle1
				ldr w9, [x1]		//Carrega elemento da seq_A
				add	x1, x1, #4		//Passa ao próximo elemento da seq_A
				sub	w0, w0, #1		//Decrementa um valor do tamanho da seq_A
				cmp w9, w7			//Compara os elemento de cada sequência
				bne	Cicle2
				add w4, w4, #1		//Incrementa um valor ao contador caso sejam iguais
				b Cicle2

End:			mov w0, w4
				ret


