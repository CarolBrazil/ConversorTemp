segundos_str = input("Por favor, entre com o numero de segundos que deseja converter: ")
total_segs = int(segundos_str)
dias = total_segs // 86400
segs_restantes = total_segs % 86400
horas = segs_restantes // 3600
segs_restantes1 = segs_restantes % 3600
minutos = segs_restantes1 // 60
segs_restantes_final = segs_restantes1 % 60

print (dias, "Dias,", horas, "Horas, ", minutos, "Minutos e ", segs_restantes_final, "Segundos.")