import pickle


def writing(arr):
    with open('quest.pickle', 'wb') as f:
        pickle.dump(arr, f)
