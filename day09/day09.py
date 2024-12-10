import heapq

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip().split('\n')[0]

def parse_input(dense_data):
    sparse_data = []
    empty_heap = []
    id = 0
    for i in range(len(dense_data)):
        if i%2 == 1:
            next_idx = len(sparse_data)
            for j in range(int(dense_data[i])):
                heapq.heappush(empty_heap,next_idx+j)
            sparse_data += [None]*int(dense_data[i])
            continue
        sparse_data += [id]*int(dense_data[i])
        id += 1
    return sparse_data,empty_heap

def parse_input_blocks(dense_data):
    sparse_data = []
    empty_heap = [[] for _ in range(10)]
    id = 0
    for i in range(len(dense_data)):
        if i%2 == 1:
            if int(dense_data[i]) > 0:
                next_idx = len(sparse_data)
                heapq.heappush(empty_heap[int(dense_data[i])],next_idx)
                sparse_data += [None]*int(dense_data[i])
            continue
        sparse_data += [id]*int(dense_data[i])
        id += 1
    return sparse_data,empty_heap
    
def rearrange_data_blocks(sparse_data,empty_heap):
    
    i = len(sparse_data)-1
    while i >= 0:

        next_id = sparse_data[i]
        if next_id is None:
            i -= 1
            continue
        
        next_id_len = 0
        while i >= 0 and sparse_data[i] == next_id:
            next_id_len += 1
            i -= 1

        smallest_idx = 10**18
        best_width = -1
        for width in range(next_id_len,10):
            if empty_heap[width]:

                if empty_heap[width][0] < smallest_idx:
                    smallest_idx = empty_heap[width][0]
                    best_width = width

        if smallest_idx == 10**18 or smallest_idx >= i:
            continue

        heapq.heappop(empty_heap[best_width])

        for j in range(next_id_len):
            sparse_data[smallest_idx + j] = next_id
            sparse_data[i + 1 + j] = None
        
        heapq.heappush(empty_heap[best_width-next_id_len],smallest_idx+next_id_len)


    return sparse_data

def rearrange_data(sparse_data,empty_heap):
    for i in range(len(sparse_data)):
        next_item = sparse_data[-i-1]
        if next_item is None:
            continue
        
        free_idx = heapq.heappop(empty_heap)
        if free_idx >= len(sparse_data) - i:
            return sparse_data 
        
        sparse_data[free_idx], sparse_data[-i-1] = next_item,None
    return sparse_data        

def calculate_checksum(sparse_data):
    checksum = 0
    for i,val in enumerate(sparse_data):
        if val is None:
            continue
        checksum += i*val
    return checksum

if __name__ == ("__main__"):
    file_name = "sample_input"
    data = read_input(file_name)
    sparse_data,empty_heap = parse_input(data)
    sparse_data = rearrange_data(sparse_data,empty_heap)
    checksum = calculate_checksum(sparse_data)
    print(f"Day 9 part 1 answer from {file_name}: {checksum}")
    
    sparse_data,empty_heap = parse_input_blocks(data)
    sparse_data = rearrange_data_blocks(sparse_data,empty_heap)
    checksum = calculate_checksum(sparse_data)
    print(f"Day 9 part 2 answer from {file_name}: {checksum}")
    
    
    file_name = "input"
    data = read_input(file_name)
    sparse_data,empty_heap = parse_input(data)
    sparse_data = rearrange_data(sparse_data,empty_heap)
    checksum = calculate_checksum(sparse_data)
    print(f"Day 9 part 1 answer from {file_name}: {checksum}")
    
    sparse_data,empty_heap = parse_input_blocks(data)
    sparse_data = rearrange_data_blocks(sparse_data,empty_heap)
    checksum = calculate_checksum(sparse_data)

    with open("log",'w') as log_file:
        print(sparse_data,file=log_file)

    with open("log2",'w') as log_file:
        print(empty_heap,file=log_file)

    print(f"Day 9 part 2 answer from {file_name}: {checksum}")
    
    