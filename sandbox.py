plt.style.use('default')
plt.figure(figsize=(16,7))

plt.plot(df_saude.index(), df_saude['Taxa de mortalidade até 5 anos, no Brasil'])
plt.plot(df_saude.index(), df_saude['Taxa de mortalidade até 5 anos, na Alemanha'])
plt.plot(df_saude.index() ,df_saude['Taxa de mortalidade até 5 anos, em Moçambique'])

plt.xticks(range(2001, 2021))
plt.legend(['Brasil', 'Alemanha', 'Moçambique'])
plt.xlabel('Ano')
plt.ylabel('% total da população')
plt.title('Acesso à eletricidade')
plt.show()