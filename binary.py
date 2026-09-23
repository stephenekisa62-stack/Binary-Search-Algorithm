
def binary_search(list,element):
    middle=0
    start=0
    end=len(list)
    steps=0

    while(start<=end):
        print("step",steps, ":" ,str(list[start:end+1]))
