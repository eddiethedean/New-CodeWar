def solution(string,markers):
    l = repr(string)[1:-1].split(chr(92)+'n')
    for m in markers:
        for i, line in enumerate(l):
            index = line.find(m)
            if index != -1:
                l[i] = line[:index]
            l[i] = l[i].rstrip()
    return "\n".join(l)
