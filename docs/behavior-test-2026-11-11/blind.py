import random, shutil, sys, os, glob
subj = sys.argv[1]
random.seed(int.from_bytes(os.urandom(4), 'big'))
os.makedirs(f'blind/{subj}', exist_ok=True)
lines = []
for kind, src in (('answer', 'answers'), ('sheet', 'sheets')):
    files = sorted(glob.glob(f'{src}/{subj}-*.md'))
    random.shuffle(files)
    for lab, f in zip('ABCDEF', files):
        shutil.copy(f, f'blind/{subj}/{kind}-{lab}.md')
        lines.append(f'{subj} {kind}-{lab} {os.path.basename(f)}')
open('blindkey.txt', 'a').write('\n'.join(lines) + '\n')
print(len(lines), 'files blinded for', subj)
