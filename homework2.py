# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# NOT(X OR Y OR Z) = NOT X AND NOT Y AND NOT Z

x = y = z =list([True,False])

count_False_staytment = 0 # ведёт подсчёт ложных утверждений
for i in x:
    for j in y:
        for k in z:
            if not(i or j or k) != (not i and not j and not k):
                count_False_staytment +=1
              
print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно при любых значений предикат" \
      if count_False_staytment == 0 else "Утврждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно")   


