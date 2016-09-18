import markovify
import os
models = []
#weights = []
print 'a'
for root, dirs, files in os.walk("/home/david/Desktop/Trump"):
    for file in files:
        if file.endswith(".speech"):
            with open(file) as f:
                text = f.read()
            models.append(markovify.Text(text))
#            weights.append
model_combo = markovify.combine(models)
for i in range(2):
    print(model_combo.make_sentence())
