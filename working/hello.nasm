global _start
section .text
_start:
xor rax,rax
mov al,1
mov rdi,rax
jmp data
hello:
pop rsi 
mov rdx,rax
add rdx,11
syscall
mov al,60
xor rdi,rdi
syscall
data:
call hello
hellod db "hello world",0xa
