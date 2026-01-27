OK_FORMAT = True

test = {'name': 'q3a', 'points': 2, 'suites': [{'cases': [{'code': ">>> acc = model.score(X_test_sc, y_test)\n>>> assert acc < 0.89 and acc > 0.88, f'Accuracy does not match expected ({int(acc * 100)}%)'\n", 'hidden': False, 'locked': False, 'points': 1}], 'scored': True, 'setup': '', 'teardown': '', 'type': 'doctest'}]}