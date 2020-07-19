# i) Towerof hanoi


def TowerOfHanoi(n, source, destination, auxilliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n-1, source, auxilliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n-1, auxilliary, destination, source)


if __name__ == "__main__":
    n = 4
    TowerOfHanoi(n, 'A', 'B', 'C')
