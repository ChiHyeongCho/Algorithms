
# rawdata.dropna(subset [""])
# rawdata[""].fillna(x, inplace = True)

def train_test_split(X, Y):

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, shuffle=False, random_state=1004)
    return X_train, X_test, y_train, y_test