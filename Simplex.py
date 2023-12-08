import lippy as lp

numerodevariaveis = int(input("Numéro de variáveis: "))
numerorestricoes = int(input("Números de restrições: "))

objetivefunction = []
restricao = []
resultado = []

for i in range(numerodevariaveis):
    print("Informe o valor da variável X"+str(i+1))
    x= float(input())
    objetivefunction.append(x)

print("Informe as restrições:")
for i in range(numerorestricoes):
    l = []
    print("Restrição "+str(i+1))
    for j in range(numerodevariaveis+1):
        
        if(j!=numerodevariaveis):
            print("Informe o valor da variável X"+str(j+1))
            x= float(input())
            l.append(x)
        else:
            print("Informe o resultado:")
            x= float(input())
            resultado.append(x)
    restricao.append(l)
    
simplex = lp.SimplexMethod(objetivefunction, restricao, resultado,log_mode=lp.LogMode.FULL_LOG)
solution, func_value = simplex.solve()
print(solution,func_value)

print("Simplex Dual:")


objetivefunction, restricao, resultado = lp.primal_to_dual_lp(objetivefunction, restricao, resultado)
simplex = lp.SimplexMethod(objetivefunction, restricao, resultado, log_mode=lp.LogMode.FULL_LOG)
solution, func_value = simplex.solve()
print(solution,func_value)