from myproject import importing, preprocess, process, train_save
import sys

def main(subprogram, *args):
    if subprogram == 'train':
        train_save.train(args[0])
    elif subprogram== 'run':
        value = args[0]
        process.imprime(preprocess.first_word(importing.importing(value)))
    else:
        raise ValueError("Subprogram unknown, available choices: train, run")

#print(__name__)
if __name__ == '__main__':
    main(*sys.argv[1:])