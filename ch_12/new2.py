def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

n = int(input("CODE : "))
print(http_status(n))