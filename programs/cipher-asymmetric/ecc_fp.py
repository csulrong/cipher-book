def fp(a, b, p):
    y_squared_mod = {x:(x**3 + a*x + b) % p for x in range(p)}
    print(y_squared_mod)
    fp = dict()
    for x, ys in y_squared_mod.items():
        for n in range(p):
            if (n**2) % p == ys:
                fp[x] = [n] if fp.get(x) is None else fp[x] + [n]
    print(fp)
    return fp
    
def csv(data, file):
    with open(file, "w") as f:
        f.write("x\ty\n")
        for x, ys in data.items():
            for y in ys:
                f.write("{}\t{}\n".format(x, y))

if __name__ == "__main__":
    csv(fp(-3, 10, 19), "ecc-fp19.dat")
    csv(fp(-3, 10, 97), "ecc-fp97.dat")
    csv(fp(-3, 10, 127), "ecc-fp127.dat")
    csv(fp(-3, 10, 487), "ecc-fp487.dat")
