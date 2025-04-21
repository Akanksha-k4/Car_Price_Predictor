scores = []
# for i in range(1000):
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, test_size=0.2, random_state=i)
#     lr = LinearRegression()
#     pipe = make_pipeline(column_trans, lr)
#     pipe.fit(X_train, y_train)
#     y_pred = pipe.predict(X_test)
#     # print(r2_score(y_test, y_pred),i)
#     score = r2_score(y_test, y_pred)
#     scores.append(score)
#     #print(i, score)
#    # print("Best R2 Score:", max(scores))
# print("Best Random State:", scores.index(max(scores)))
