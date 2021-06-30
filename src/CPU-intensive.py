import math
def cpu_intensive_operation():
    """
    This function is supposed to mock a CPU intensive job
    :return:
    """
    x = 0
    for i in range(1000000000000):
        x += math.sqrt(x)


def main():
    print("Starting the CPU intensive job")
    cpu_intensive_operation()


if __name__ == "__main__":
    main()
