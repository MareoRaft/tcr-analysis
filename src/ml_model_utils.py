def get_loocv_indices(n):
    ''' Since our LOOCV situation is a bit unique (we want to keep samples in consecutive pairs when removing, I build my own LOOCV index computation. '''
    assert n % 2 == 0
    loocv_indices = []
    # First remove samples 0 and 1, then remove samples 2 and 3, and so on...
    for i in range(n//2):
        print(i)
        # train indices
        train_indices = np.array([i*2, i*2+1])
        # test indices
        test_indices = list(range(n))
        for train_index in train_indices:
            test_indices.remove(train_index)
        test_indices = np.array(test_indices)
        # record
        loocv_indices.append((train_indices, test_indices))
    return loocv_indices
