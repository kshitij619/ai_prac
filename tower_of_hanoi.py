def tower_of_hanoi(n, src, helper, des):
    if n == 1:
        print(f"Transfer disk {n} from tower {src} to {des}")
        return
    tower_of_hanoi(n - 1, src, des, helper)
    print(f"Transfer disk {n} from tower {src} to {des}")
    tower_of_hanoi(n - 1, helper, src, des)

if __name__ == "__main__":
    n = 5
    tower_of_hanoi(n, "S", "H", "D")

