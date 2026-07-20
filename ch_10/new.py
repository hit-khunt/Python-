class employee:
    language = "Python" # This is  a class attribute
    salary = 120000

hit = employee()
hit.name = "Hit" # This is an object(instance) attribute
print(hit.name, hit.salary, hit.language)

het = employee()
het.name = "Het"
het.language = "Java"
print(het.salary, het.name, het.language)
