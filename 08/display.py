import ipdb


UNIQUES = [2, 4, 3, 7]


def parse(file):
    with open(file) as f:
        return [x for line in f.read().splitlines() for x in line.split(" | ")]


def get_outputs(file):
    with open(file) as f:
        return [x.split(' | ')[1].split() for x in f.read().splitlines()]


def count_uniques_in(output):
    cnt = 0
    for row in output:
        for elem in row:
            if len(elem) in UNIQUES:
                cnt += 1
    return cnt

def decode(signal):
    decoder = {}
    fives = []
    sixes =[]

    for sig in signal:
        if len(sig) == 2: decoder.update({'1': set(sig)})
        if len(sig) == 3: decoder.update({'7': set(sig)})
        if len(sig) == 4: decoder.update({'4': set(sig)})
        if len(sig) == 7: decoder.update({'8': set(sig)})
        if len(sig) == 5: fives.append(set(sig))
        if len(sig) == 6: sixes.append(set(sig))

    for six in sixes:
        if six.issuperset(decoder['4']):
            decoder.update({'9': six})
        elif six.issuperset(decoder['7']):
            decoder.update({'0': six})
        else:
            decoder.update({'6': six})


    for five in fives:
        if five.issuperset(decoder['7']):
            decoder.update({'3': five})
        elif five.issubset(decoder['6']):
            decoder.update({'5': five})
        else:
            decoder.update({'2': five})

    return decoder


def translate(output, decoder):
    result = ''
    for digit in output:
        for key, val in decoder.items():
            if set(digit) == val:
                result += key
    return int(result)


def main():
    #file = '../inputs/test'
    file = '../inputs/08'
    print(f"Part 1: {count_uniques_in(get_outputs(file))}")
    data = parse(file)
    signals = [signal.split() for signal in data[0::2]]
    outputs = [output.split() for output in data[1::2]]
    summa = 0
    for signal, output in zip(signals, outputs):
          decoder = decode(signal)
          answer = translate(output, decoder)
          summa += answer
    print(summa)

if __name__ == "__main__":
    main()
