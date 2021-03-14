def main():
    x = input().split()
    n1, n2, n3, n4 = x
    m = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
    print(f'Media: {m:.1f}')
    if m >= 7.0:
        print('Aluno aprovado.')
    if m < 5.0:
        print('Aluno reprovado.')
    if 5.0 <= m <= 6.9:
        print('Aluno em exame.')
        y = float(input())
        print(f'Nota do exame: {y}')
        m2 = (y + m) / 2
        if m2 >=5:
            print('Aluno aprovado.')
            print(f'Media final: {m2:.1f}')
        else:
            print('Aluno reprovado.')
            print(f'Media final: {m2:.1f}')

if __name__ == '__main__':
    main()
