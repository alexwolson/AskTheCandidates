def say_Trump(sen):
    import markovify
    import os
    models = []
#    weights = []
    for file in os.listdir("/mydir"):
        if file.endswith(".txt"):
            with open(file) as f:
                text = f.read()
            models.append(markovify.Text(text))
#            weights.append
    model_combo = markovify.combine(models)
    for i in range(sen):
        print(model_combo.make_sentence())
