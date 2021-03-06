def say_Trump(sen):
    import markovify
    import os
    models = []
    weights = []
    for file in os.listdir("./"):
        if file.endswith(".speech"):
            with open(file) as f:
                text = f.read()
            models.append(markovify.Text(text))
            (weight, dot, speech) = file.partition('.')
            weights.append(1/(int(weight)))
    model_combo = markovify.combine(models,weights)
    for i in range(sen):
        print(model_combo.make_sentence())
