1. Ejecutar un comando con ansible:
-------------------------------------------
ansible 192.168.0.10 -m ping
-m = modulo
#-a = permite ejecutar el comando

ansible 192.168.0.10 -u usuariojohn -m ping
#-u = indica el usuario

ansible all -a ping
#all = indica todos los servidores dentro del inventario

ansible all --become -a "id"
#ansible ejecutara todo como usuario root, volviendose administrador. 

test line
 
--------------------------------------------



