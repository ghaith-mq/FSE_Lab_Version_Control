from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    st.add(('c', 3))
    val = st.get('c')
    assert val == 3, "The value is different from the one that was added"
    	
def test_remove():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    st.remove(key)
    print("new dictionary")


def test_set():
    st = Storage({'a': 1, 'b': 2})
    key = 'a'
    new_val = 5
    st.set(key, new_val)
    assert st.get(key) == new_val, "Value for the key is not equal to new value"

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
