def zoek_binair(zoekltem, rij):
    n = len(rij)
    l = 0
    r = n - 1
    
    # Herhalen totdat slechts één element overblijft (l == r)[cite: 57]
    while l != r:
        # Druk de linker- en rechtergrens af als eerste opdracht in de while-lus
        print(f"{l}, {r}")
        
        # Bepaal het midden[cite: 57]
        m = (l + r) // 2
        
        # Zoek verder in de rechter- of linkerhelft[cite: 57]
        if rij[m] < zoekltem:
            l = m + 1
        else:
            r = m
            
    # Controleer of het overgebleven element gelijk is aan het gezochte item[cite: 57]
    if rij[l] == zoekltem:
        index = l
    else:
        index = -1
        
    return index